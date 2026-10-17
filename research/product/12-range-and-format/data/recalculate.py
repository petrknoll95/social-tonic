"""Reproduce illustrative portfolio and channel sensitivities; Python standard library only."""
import csv
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
p = json.loads((ROOT / 'model-inputs.json').read_text())

def save(name, rows):
    with (ROOT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

def rounded(row):
    return {k: round(v, 4) if isinstance(v, float) else v for k, v in row.items()}

window = p['saleable_window_weeks_assumption']
rows = []
for a, q, cost, weekly in itertools.product(p['architectures'], p['run_units_per_sku'], p['unit_manufactured_costs'], p['total_weekly_demand_scenarios']):
    assert a['skus'] == len(a['shares']) and abs(sum(a['shares']) - 1) < 1e-8
    inventory = a['skus'] * q * cost
    fixed = a['formulas'] * p['fixed_cost_per_formula'] + a['skus'] * p['fixed_cost_per_sku']
    unsold = sum(max(0, q - weekly * s * window) for s in a['shares'])
    rows.append(rounded(dict(architecture=a['id'], formulas=a['formulas'], skus=a['skus'], run_units_per_sku=q,
        manufactured_cost_per_can_czk=cost, total_initial_cans=q*a['skus'], inventory_cash_czk=inventory,
        illustrative_fixed_cost_czk=fixed, modelled_cash_subtotal_czk=inventory+fixed,
        total_weekly_demand_assumed=weekly, slowest_sku_weeks_to_clear=q/(weekly*min(a['shares'])),
        saleable_window_weeks=window, required_total_weekly_demand_to_clear_slowest_within_window=q/(window*min(a['shares'])),
        unsold_cans_at_window_end=unsold, manufactured_cost_at_risk_at_window_end_czk=unsold*cost)))
save('inventory-sensitivity.csv', rows)
e = p['unit_economics']
rows = []
for price, cost, route in itertools.product(e['consumer_prices_including_vat'], p['unit_manufactured_costs'], ['direct-to-retailer', 'via-distributor']):
    ex_vat = price/(1+e['vat_assumption'])
    retailer_purchase = ex_vat*(1-e['retailer_margin_of_ex_vat_retail'])
    brand_net = retailer_purchase if route == 'direct-to-retailer' else retailer_purchase*(1-e['distributor_margin_of_ex_vat_retailer_purchase'])
    contribution = brand_net-cost-e['trade_variable_cost_per_can']
    rows.append(rounded(dict(route=route, retail_price_including_vat_czk=price, manufactured_cost_czk=cost,
        net_retail_value_czk=ex_vat, brand_net_sales_czk=brand_net,
        contribution_before_fixed_and_acquisition_czk=contribution,
        maximum_manufactured_cost_for_zero_contribution_czk=brand_net-e['trade_variable_cost_per_can'])))
save('trade-economics-sensitivity.csv', rows)
rows=[]
for unit_price, pack, cost, subscription in itertools.product(e['dtc_prices_per_can_including_vat'], e['dtc_pack_sizes'], p['unit_manufactured_costs'], [False, True]):
    gross=unit_price*pack*(1-e['subscription_discount_of_gross_price'] if subscription else 1)
    net=gross/(1+e['vat_assumption'])
    fee=gross*e['dtc_payment_rate_of_gross_revenue']
    reserve=net*e['dtc_damage_refund_reserve_of_ex_vat_revenue']
    contribution=net-pack*cost-fee-reserve-e['dtc_pick_pack_per_order']-e['dtc_net_delivery_cost_paid_by_brand_per_order']
    rows.append(rounded(dict(base_price_per_can_including_vat_czk=unit_price, pack_cans=pack,
        manufactured_cost_per_can_czk=cost, subscription_10_percent_discount=subscription,
        customer_goods_total_including_vat_czk=gross, net_sales_ex_vat_czk=net,
        contribution_before_acquisition_fixed_czk=contribution, contribution_per_can_czk=contribution/pack,
        maximum_first_order_cac_for_zero_contribution_czk=contribution)))
save('dtc-pack-sensitivity.csv',rows)
print('Generated 180 inventory, 24 trade and 54 DTC scenarios.')
