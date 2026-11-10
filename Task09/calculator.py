"""Task 9: complete milk payment calculator with validation."""
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Task07"))
from milkrate import rate_per_litre   # noqa: E402

MIN_FAT, MAX_FAT = 2.0, 7.0
MIN_SNF, MAX_SNF = 7.0, 10.0
SHIFTS = ("Morning", "Evening")


def validate_entry(farmer_id, litres, fat, snf, shift="Morning"):
    """Return a list of error messages (empty list means the entry is valid)."""
    errors = []
    if not str(farmer_id).strip():
        errors.append("Farmer ID is empty")
    for name, value in (("litres", litres), ("fat", fat), ("snf", snf)):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{name} is not a number")
    if errors:
        return errors
    if litres < 0:
        errors.append("litres cannot be negative")
    if not MIN_FAT <= fat <= MAX_FAT:
        errors.append("fat must be between 2.0 and 7.0")
    if not MIN_SNF <= snf <= MAX_SNF:
        errors.append("snf must be between 7.0 and 10.0")
    if shift not in SHIFTS:
        errors.append("shift must be Morning or Evening")
    return errors


def money(value):
    """Round a number to 2 decimals (half up) and return a Decimal."""
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def entry_payment(litres, fat, snf):
    """Payment for one entry as an exact Decimal."""
    return money(Decimal(str(litres)) * Decimal(str(rate_per_litre(fat, snf))))


def ten_day_total(entries):
    """Exact total of a list of (litres, fat, snf) entries; raises on invalid data."""
    total = Decimal("0")
    for litres, fat, snf in entries:
        errors = validate_entry("X", litres, fat, snf)
        if errors:
            raise ValueError("; ".join(errors))
        total += entry_payment(litres, fat, snf)
    return total


if __name__ == "__main__":
    sample = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (5, 2.0, 8.0), (20, 7.0, 9.0)]
    for litres, fat, snf in sample:
        print(f"{litres:5} L fat {fat} snf {snf}  rate {rate_per_litre(fat, snf):6.2f}"
              f"  pay {entry_payment(litres, fat, snf):9}")
    print("Total:", ten_day_total(sample))
