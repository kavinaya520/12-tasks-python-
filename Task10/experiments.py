"""Task 10: compare float and Decimal, rounding strategy, and rate table."""
import os
import sys
import time
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Task07"))
from milkrate import rate_per_litre, BASE_RATE   # noqa: E402,F401

SAMPLES = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (7.3, 3.9, 8.6), (15.2, 4.6, 8.9)]


def make_entries(n):
    """Build n entries by cycling through the sample entries."""
    return [SAMPLES[i % len(SAMPLES)] for i in range(n)]


def total_float(entries):
    """Total using floats with no rounding of each payment."""
    return sum(l * rate_per_litre(f, s) for l, f, s in entries)


def total_decimal(entries):
    """Total using exact Decimal arithmetic."""
    total = Decimal("0")
    for l, f, s in entries:
        total += Decimal(str(l)) * Decimal(str(rate_per_litre(f, s)))
    return total


def timed(func, *args):
    """Return (result, seconds) using time.perf_counter()."""
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start


print("float vs Decimal totals")
print(f"{'n':>8} | {'float total':>22} | {'Decimal total':>16} | {'float s':>8} | {'Decimal s':>9}")
for n in (300, 6000, 150000):
    entries = make_entries(n)
    tf, sf = timed(total_float, entries)
    td, sd = timed(total_decimal, entries)
    print(f"{n:>8} | {tf!r:>22} | {str(td):>16} | {sf:8.4f} | {sd:9.4f}")

print("\nRounding each payment vs rounding only the final total (n = 300)")
entries = make_entries(300)
exact = [Decimal(str(l)) * Decimal(str(rate_per_litre(f, s))) for l, f, s in entries]
each = sum(x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) for x in exact)
final = sum(exact).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("  round each payment, then add :", each)
print("  add exactly, round the total :", final)
print("  (a bank pays each farmer a rounded amount, so rounding each payment matches the bank)")

print("\nRate table (dictionary) vs recalculation, 150,000 entries")
entries = make_entries(150000)
table = {}
def with_table(entries):
    """Look up each (fat, snf) rate in a dictionary, calculating it once."""
    total = 0.0
    for l, f, s in entries:
        key = (f, s)
        if key not in table:
            table[key] = rate_per_litre(f, s)
        total += l * table[key]
    return total
def recalc(entries):
    """Recalculate the rate for every entry."""
    return sum(l * rate_per_litre(f, s) for l, f, s in entries)
_, t_table = timed(with_table, entries)
_, t_calc = timed(recalc, entries)
print(f"  dictionary lookup : {t_table:.4f} s   (k = {len(table)} distinct pairs stored)")
print(f"  recalculation     : {t_calc:.4f} s")
