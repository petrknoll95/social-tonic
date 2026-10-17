"""Reproduce claim-eligibility arithmetic; no formula/safety/claim approval."""
from pathlib import Path
from decimal import Decimal as D
import csv

ROOT = Path(__file__).resolve().parent


def write(name, headers, rows):
    with (ROOT / name).open("w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)


nutrients = [
    ("pantothenic-acid-b5", "mg", "6"),
    ("vitamin-b6", "mg", "1.4"),
    ("vitamin-b12", "microgram", "2.5"),
    ("niacin", "mg", "16"),
    ("magnesium-elemental", "mg", "375"),
    ("iodine", "microgram", "150"),
    ("iron", "mg", "14"),
    ("zinc", "mg", "10"),
]
write(
    "nutrient-thresholds.csv",
    ["nutrient", "unit", "nrv", "source-per-100ml", "source-in-250ml-at-that-concentration",
     "source-in-330ml-at-that-concentration", "source-per-genuine-single-portion-pack",
     "high-per-100ml", "high-per-genuine-single-portion-pack", "source-ids"],
    [(name, unit, D(nrv), D(nrv)*D("0.075"), D(nrv)*D("0.075")*D("2.5"),
      D(nrv)*D("0.075")*D("3.3"), D(nrv)*D("0.15"), D(nrv)*D("0.15"),
      D(nrv)*D("0.30"), "CN08;CN16") for name, unit, nrv in nutrients],
)
caffeine_examples = [("40", "250"), ("40", "330"), ("60", "250"), ("75", "250"),
                     ("75", "330"), ("80", "330"), ("37.5", "250"), ("49.5", "330")]
write(
    "caffeine-concentration-examples.csv",
    ["caffeine-mg", "pack-ml", "mg-per-100ml-rounded", "mg-per-litre-rounded",
     "exceeds-150mg-per-litre", "exception-note", "source-ids"],
    [(D(mg), D(ml), (D(mg)/D(ml)*100).quantize(D("0.0001")),
      (D(mg)/D(ml)*1000).quantize(D("0.0001")),
      "yes" if D(mg)/D(ml)*1000 > 150 else "no",
      "Check actual coffee/tea base and name exception; not a claim permission", "CN08")
     for mg, ml in caffeine_examples],
)
write(
    "nutrition-and-serving-examples.csv",
    ["example", "calculation", "result", "unit", "interpretation", "source-ids"],
    [
        ("low-sugars-250ml", "2.5*250/100", D("2.5")*250/100, "g total sugars maximum",
         "Liquid concentration controls; not a target", "LM02;LM04"),
        ("low-sugars-330ml", "2.5*330/100", D("2.5")*330/100, "g total sugars maximum",
         "Liquid concentration controls; not a target", "LM02;LM04"),
        ("sugars-free-250ml", "0.5*250/100", D("0.5")*250/100, "g total sugars maximum",
         "Not absolute chemical absence", "LM02;LM04"),
        ("sugars-free-330ml", "0.5*330/100", D("0.5")*330/100, "g total sugars maximum",
         "Not absolute chemical absence", "LM02;LM04"),
        ("fibre-energy-example", "3/30*100", D("3")/30*100, "g fibre/100kcal",
         "Numerically high fibre; verify EU energy/fibre values; not gut claim", "CS14"),
        ("carbohydrate-recovery-70kg", "4*70", D("4")*70, "g carbohydrate total from all sources",
         "Specific exercise/time conditions; not one-can target", "CS13"),
        ("cbd-provisional-70kg", "0.0275*70", D("0.0275")*70, "mg/day",
         "Only qualifying supplement safety context; not beverage safe dose", "CS04"),
    ],
)
print("Regenerated 8 nutrient, 8 caffeine and 7 serving calculation examples.")
