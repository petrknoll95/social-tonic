#!/usr/bin/env python3
"""Rebuild transparent planning scenarios; stdlib only, no network calls."""
import csv,json,copy
from pathlib import Path
D=Path(__file__).resolve().parent
m=json.loads((D/'model-inputs.json').read_text())
def save(name,rows):
    with (D/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)
def score(vals,weights):return sum(v*w/5 for v,w in zip(vals,weights.values()))
def calc(geo,benefit,scenario,overrides=None):
    c=m['countries'][geo];b=m['benefits'][benefit];s=copy.deepcopy(m['scenarios'][scenario]);s.update(overrides or {})
    venues,per_venue,digital,overlap=c['reach'][scenario]
    pool=venues*per_venue+digital-overlap
    assert 0<=overlap<=min(venues*per_venue,digital)
    reach=s.get('unique_pool',pool)*s.get('qualification',b['qualification'])
    buyers=reach*s['trial_rate']; repeat=buyers*s['repeat_rate']
    trial_units=buyers*s['trial_units']; repeat_units=repeat*s['repeat_orders']*s['repeat_units']
    units=trial_units+repeat_units;price=s.get('net_price_eur',c['net_price_eur'][scenario]*b['price_factor'])
    return dict(geo=geo,benefit=benefit,scenario=scenario,planned_venues=venues,annual_unique_adults_per_venue=per_venue,digital_unique_adults=digital,cross_channel_duplicate_adults=overlap,union_unique_adults=s.get('unique_pool',pool),occasion_qualification=s.get('qualification',b['qualification']),reachable_qualified_adults=reach,paid_trial_rate=s['trial_rate'],first_paid_buyers=buyers,repeat_buyer_rate=s['repeat_rate'],repeat_buyers=repeat,first_purchase_units=s['trial_units'],repeat_orders_per_repeater_within_horizon=s['repeat_orders'],units_per_repeat_order=s['repeat_units'],trial_units=trial_units,repeat_units=repeat_units,total_units=units,net_price_eur=price,net_revenue_eur=units*price)
countries=[];combos=[];scenarios=[]
for g,c in m['countries'].items():
    cp=score(c['scores'],m['country_weights'])
    countries.append(dict(geo=g,country=c['name'],**dict(zip(m['country_weights'],c['scores'])),country_points_out_of_45=cp,country_score_out_of_100=cp/45*100))
    for b,v in m['benefits'].items():
        bp=score(v['scores'][g],m['benefit_weights']); base=calc(g,b,'base')
        combos.append(dict(geo=g,benefit=b,**dict(zip(m['benefit_weights'],v['scores'][g])),country_points=cp,benefit_points=bp,total_score_out_of_100=cp+bp,base_reachable_qualified_adults=base['reachable_qualified_adults'],base_first_paid_buyers=base['first_paid_buyers'],base_repeat_buyers=base['repeat_buyers'],base_units=base['total_units'],base_net_revenue_eur=base['net_revenue_eur']))
        for s in m['scenarios']:scenarios.append(calc(g,b,s))
save('country-scorecard.csv',sorted(countries,key=lambda r:-r['country_score_out_of_100']))
save('category-country-scorecard.csv',sorted(combos,key=lambda r:-r['total_score_out_of_100']))
save('demand-scenarios.csv',scenarios)
base=calc('CZ','focus-workday-alertness','base');sens=[]
tests={'unique_pool':[7000,14000,28000],'qualification':[0.3,0.6,0.8],'trial_rate':[0.04,0.08,0.12],'repeat_rate':[0.15,0.35,0.55],'repeat_orders':[3,6,9],'repeat_units':[3,6,12],'trial_units':[1,2,6],'net_price_eur':[0.85,1.10,1.35]}
for k,vals in tests.items():
    for val in vals:
        r=calc('CZ','focus-workday-alertness','base',{k:val});sens.append(dict(parameter=k,value=val,units=r['total_units'],net_revenue_eur=r['net_revenue_eur'],change_from_base_pct=(r['net_revenue_eur']/base['net_revenue_eur']-1)*100))
save('sensitivity.csv',sens)
costs=[]
for net in [.85,1.10,1.35]:
    for cost in [.70,.85,1.05]:
        contribution=base['total_units']*(net-cost)
        costs.append(dict(net_price_eur=net,variable_cost_eur=cost,contribution_per_unit_eur=net-cost,base_units=base['total_units'],contribution_before_acquisition_fixed_costs_eur=contribution,contribution_per_trial_buyer_eur=contribution/base['first_paid_buyers'],units_to_cover_15000_fixed_cost=15000/(net-cost) if net>cost else 'not achievable at nonpositive margin'))
save('contribution-sensitivity.csv',costs)
weightcases={
 'founder_learning_default':(m['country_weights'],m['benefit_weights']),
 'demand_first':({'founder_access':10,'spending_context':10,'channel_access':10,'logistics':5,'packaging_admin':5},{'demand_evidence':30,'repeat_plausibility':10,'switch_reason':10,'evidence_and_legal_simplicity':10}),
 'premium_scale':({'founder_access':5,'spending_context':25,'channel_access':10,'logistics':5,'packaging_admin':5},{'demand_evidence':20,'repeat_plausibility':10,'switch_reason':10,'evidence_and_legal_simplicity':10})}
weightrows=[]
for name,(cw,bw) in weightcases.items():
    assert sum(cw.values())+sum(bw.values())==100
    rows=[]
    for g,c in m['countries'].items():
        for b,v in m['benefits'].items():rows.append((score(c['scores'],cw)+score(v['scores'][g],bw),g,b))
    for rank,(pts,g,b) in enumerate(sorted(rows,reverse=True),1):weightrows.append(dict(weight_case=name,rank=rank,geo=g,benefit=b,score=pts,country_weights=json.dumps(cw),benefit_weights=json.dumps(bw)))
save('weight-sensitivity.csv',weightrows)
# Arithmetic/invariant checks that protect against meaningful model errors.
assert len(scenarios)==90 and len(combos)==30
for r in scenarios:
    assert r['repeat_buyers']<=r['first_paid_buyers']<=r['reachable_qualified_adults']<=r['union_unique_adults']
    assert abs(r['total_units']-(r['trial_units']+r['repeat_units']))<1e-7
    assert abs(r['net_revenue_eur']-r['total_units']*r['net_price_eur'])<1e-7
assert abs(base['net_revenue_eur']-10792.32)<.001
print('Rebuilt 90 scenarios, 30 combinations and sensitivity tables; arithmetic checks passed.')
print('CZ base:',base)
print('Top combinations:',[(x['geo'],x['benefit'],x['total_score_out_of_100']) for x in sorted(combos,key=lambda r:-r['total_score_out_of_100'])[:6]])
for name in weightcases:print(name,[r for r in weightrows if r['weight_case']==name][:1])
# Score uncertainty is distinct from weight preference.
score_cases={
 'focus_switch_reason_down_one':('CZ','focus-workday-alertness','switch_reason',2),
 'energy_switch_reason_up_one':('CZ','general-energy','switch_reason',2),
 'czech_local_access_unproven':('CZ',None,None,None)}
sr=[]
for case,(targetg,targetb,criterion,val) in score_cases.items():
    rows=[]
    for g,c in m['countries'].items():
        cs=list(c['scores'])
        if case=='czech_local_access_unproven' and g=='CZ':cs[0]=3;cs[2]=3
        for b,v in m['benefits'].items():
            bs=list(v['scores'][g])
            if g==targetg and b==targetb:bs[list(m['benefit_weights']).index(criterion)]=val
            rows.append((score(cs,m['country_weights'])+score(bs,m['benefit_weights']),g,b))
    for rank,(pts,g,b) in enumerate(sorted(rows,reverse=True),1):sr.append(dict(score_case=case,rank=rank,geo=g,benefit=b,score=pts))
save('score-sensitivity.csv',sr)
economics=[]
for g,c in m['countries'].items():
    r=calc(g,'focus-workday-alertness','base');cost=c['variable_cost_eur'];unit=r['net_price_eur']-cost
    economics.append(dict(geo=g,base_units=r['total_units'],assumed_net_receipt_eur=r['net_price_eur'],assumed_variable_cost_eur=cost,assumed_contribution_per_unit_eur=unit,contribution_before_acquisition_fixed_costs_eur=r['total_units']*unit,contribution_per_first_buyer_eur=r['total_units']*unit/r['first_paid_buyers'],status='Illustrative unquoted costs; cannot establish preferred expansion market'))
save('country-economics-sensitivity.csv',economics)
