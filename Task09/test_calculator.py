"""Task 9: manual test table and automated assert tests."""
from decimal import Decimal
from calculator import validate_entry, entry_payment, ten_day_total

# (name, input, expected payment)
VALID_CASES = [
    ("above standard",     (8.5, 4.2, 8.7),  Decimal("283.90")),
    ("below standard",     (12, 3.1, 8.3),   Decimal("333.60")),
    ("boundary 3.5/8.5",   (10, 3.5, 8.5),   Decimal("300.00")),
    ("lowest fat 2.0",     (5, 2.0, 8.0),    Decimal("112.50")),
    ("highest fat 7.0",    (20, 7.0, 9.0),   Decimal("910.00")),
]
INVALID_CASES = [
    ("text input",         ("F1", "eight", 3.5, 8.5)),
    ("negative litres",    ("F1", -5, 3.5, 8.5)),
    ("fat too low",        ("F1", 10, 1.9, 8.5)),
    ("fat too high",       ("F1", 10, 7.1, 8.5)),
]

print(f"{'Test':<18}{'Expected':>10}{'Actual':>10}  Status")
failures = 0
for name, (litres, fat, snf), expected in VALID_CASES:
    actual = entry_payment(litres, fat, snf)
    ok = actual == expected
    failures += not ok
    print(f"{name:<18}{str(expected):>10}{str(actual):>10}  {'PASS' if ok else 'FAIL'}")
for name, args in INVALID_CASES:
    errors = validate_entry(*args)
    ok = bool(errors)
    failures += not ok
    print(f"{name:<18}{'rejected':>10}{'rejected' if errors else 'accepted':>10}  {'PASS' if ok else 'FAIL'}")

# Five-entry sample whose total was calculated by hand: 300 + 283.90 + 333.60 + 112.50 + 910 = 1940.00
sample = [c[1] for c in VALID_CASES]
assert ten_day_total(sample) == Decimal("1940.00")
print("Five-entry total 1940.00: PASS")
assert failures == 0
print("All tests passed")
