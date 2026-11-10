# Task 10 - Expectation vs Execution

experiments.py output is saved in output.txt (times depend on the computer).

| n | float total | Decimal total | float time | Decimal time |
|---|---|---|---|---|
| 300 | 101489.4 | 101489.40 | 0.0004 s | 0.0008 s |
| 6,000 | 2029788.0 | 2029788.00 | 0.0068 s | 0.0167 s |
| 150,000 | 50744700.0 | 50744700.00 | 0.2121 s | 0.4545 s |

Observations
- For these sample payments (whole-number-friendly values) the float total looks right, so float
  errors do not always show. They appear with values like 33.40 added many times (Task 2).
  Decimal stays exact and costs about 2x the time, which is still small for 150,000 entries.
- Rounding each payment and rounding only the final total gave the same amount here (101489.40),
  but they can differ when payments have extra decimals (for example a payment of 35.975).
  Because each farmer is paid a whole-paise amount, rounding each payment is the correct rule.
- Rate table: 5 distinct (fat, snf) pairs (k = 5) stored in a dictionary made the run about 3.5x faster
  (0.060 s vs 0.211 s). Lookup is O(1) per entry, extra space is O(k).
