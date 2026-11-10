"""Task 12: tests for original and seasonal rates, with and without bonus."""
from decimal import Decimal
from milkrate_v2 import rate_per_litre, payout, bonus, ten_day_total, season_for_month

D = Decimal
rows = [
    ("normal, standard milk",      payout(10, "3.50", "8.50"),               D("300.00")),
    ("normal, 4.25 fat 8.70 snf",  rate_per_litre("4.25", "8.70"),           D("33.60")),
    ("Apr-Jun, standard milk",     payout(10, "3.50", "8.50", "apr_jun"),    D("320.00")),
    ("Apr-Jun, 4.25 fat 8.70 snf", rate_per_litre("4.25", "8.70", "apr_jun"), D("35.98")),
    ("bonus not earned (500 L)",   bonus(500),                               D("0.00")),
    ("bonus earned (600 L)",       bonus(600),                               D("300.00")),
]
print(f"{'Test':<30}{'Expected':>10}{'Actual':>10}  Status")
for name, actual, expected in rows:
    print(f"{name:<30}{str(expected):>10}{str(actual):>10}  {'PASS' if actual == expected else 'FAIL'}")
    assert actual == expected

# ten days: 10 entries of 60 litres at standard milk = 600 L -> 600 * 30 + 300 bonus
ten = [(60, "3.50", "8.50")] * 10
assert ten_day_total(ten) == D("18300.00")
assert ten_day_total(ten[:5]) == D("9000.00")           # 300 L, no bonus
assert ten_day_total(ten, "apr_jun") == D("19500.00")   # 600 * 32 + 300
assert season_for_month(5) == "apr_jun" and season_for_month(8) == "normal"
print("Ten-day totals (with/without bonus, both seasons): PASS")
try:
    rate_per_litre("7.50", "8.50")
except ValueError as err:
    print("Invalid fat rejected:", err)
