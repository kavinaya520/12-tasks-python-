"""Task 4: correct expressions for steps, rate and payment."""
import math
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Task03"))
from constants import *   # noqa: E402,F401


def steps(value, standard):
    """Number of 0.1% steps between value and the standard, as a whole number."""
    return round((value - standard) / STEP_SIZE)


def rate_and_payment(litres, fat, snf):
    """Return (rate per litre, payment) using round() for the step counts."""
    fat_steps = steps(fat, STANDARD_FAT)
    snf_steps = steps(snf, STANDARD_SNF)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2), round(litres * rate, 2)


if __name__ == "__main__":
    print("Precedence")
    print("  2 ** 3 ** 2 =", 2 ** 3 ** 2, "(right-associative)")
    print("  -2 ** 2     =", -2 ** 2, "(** binds tighter than unary minus)")
    print("  (-2) ** 2   =", (-2) ** 2)

    print("\nFloating-point step error")
    print("  (4.2 - 3.5) / 0.1        =", (4.2 - 3.5) / 0.1)
    print("  round((4.2 - 3.5) / 0.1) =", round((4.2 - 3.5) / 0.1))

    print("\nround() vs int() vs math.floor()")
    for x in (-2.5, -2.4, -2.6, 2.5):
        print(f"  {x:5}: round={round(x)}  int={int(x)}  floor={math.floor(x)}")

    print("\nFat steps and rate for 4.2% and 3.1% (SNF 8.5, 10 litres)")
    for fat in (4.2, 3.1):
        raw = (fat - STANDARD_FAT) / STEP_SIZE
        r, i, f = round(raw), int(raw), math.floor(raw)
        print(f"  fat {fat}: raw={raw!r}  round={r}  int={i}  floor={f}")
        for name, n in (("round", r), ("int", i), ("floor", f)):
            rate = BASE_RATE + n * FAT_STEP_VALUE
            print(f"     {name:5} -> rate {rate:.2f}  payment {10 * rate:.2f}")

    print("\nComparison chaining and Boolean operators")
    fat = 4.2
    print("  2.0 <= fat <= 7.0           :", 2.0 <= fat <= 7.0)
    print("  fat >= 2.0 and fat <= 7.0   :", fat >= 2.0 and fat <= 7.0)
    print("  not (2.0 <= 7.5 <= 7.0)     :", not (2.0 <= 7.5 <= 7.0))
    print("\nExample:", rate_and_payment(10.5, 4.2, 8.8))
