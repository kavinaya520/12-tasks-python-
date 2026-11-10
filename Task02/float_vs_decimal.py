"""Task 2: float vs Decimal for money (TODO 1 completed)."""
import sys
from decimal import Decimal

# 1,000 payments of Rs 33.40 and three adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    """Add the amounts using binary floats."""
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    """Add the amounts exactly using Decimal built from strings."""
    total = Decimal("0")
    for amount in items:
        total += Decimal(amount)
    return total


def total_paise(items):
    """Add the amounts as integer paise (exact and fastest)."""
    total = 0
    for amount in items:
        total += int(Decimal(amount) * 100)
    return total


def total_float_rounded(items):
    """Add floats, rounding to 2 decimals after every addition."""
    total = 0.0
    for amount in items:
        total = round(total + float(amount), 2)
    return total


if __name__ == "__main__":
    print("float  :", total_float(payments))
    print("Decimal:", total_decimal(payments))
    print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
    print()
    print("Integer paise      :", total_paise(payments), "paise")
    print("float + round each :", total_float_rounded(payments))
    print()
    print("sys.getsizeof (bytes)")
    print("  Decimal :", sys.getsizeof(Decimal("33.40")))
    print("  int     :", sys.getsizeof(3340))
    print("  float   :", sys.getsizeof(33.40))
    print()
    # The 'change' asked in the task: Decimal(float(amount))
    wrong = Decimal("0")
    for amount in payments:
        wrong += Decimal(float(amount))
    print("Decimal(float(amount)) total:", wrong)
