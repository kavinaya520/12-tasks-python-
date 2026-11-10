# Task 1 - Understand the Problem and Identify the Data

## Inputs
| Input | Type | Reason |
|---|---|---|
| Farmer ID | string | may contain letters or leading zeros |
| Litres | float | can be fractional |
| Fat % | float | decimal precision needed |
| SNF % | float | decimal precision needed |
| Shift | string | "Morning" or "Evening" |

## Outputs
Rate per litre (float), payment per entry (float), ten-day total (float).
A Boolean `is_valid` flag is used internally for validation.

## Named constants
BASE_RATE = 30.00, STANDARD_FAT = 3.5, STANDARD_SNF = 8.5, FAT_STEP_VALUE = 0.40,
SNF_STEP_VALUE = 0.30, STEP_SIZE = 0.1, MIN_FAT = 2.0, MAX_FAT = 7.0, PAYOUT_CYCLE_DAYS = 10

## Validation rules
- Litres must be 0 or more
- 2.0 <= fat <= 7.0
- SNF within a realistic range (7.0 to 10.0)
- Farmer ID must not be empty
- Shift must be Morning or Evening

## Assumptions
- Fat and SNF come to one decimal place from the clerk (two decimals from Task 12).
- A farmer has at most two entries a day (morning and evening).
- The rate may fall below 30.00 when fat or SNF is below standard; the formula allows it.

## Additional question: separate variables vs list of records
| Aspect | Separate variables (litres1, fat1, ...) | List of tuples/dicts |
|---|---|---|
| Time for n entries | O(n) lines of code, cannot be written as a loop | O(n) with one loop |
| Space | O(n) values but O(n) unique names to manage | O(n), indexed |
| Scalability | breaks down beyond a few dozen farmers | works for 300, 6,000 and 150,000 |

A list of records is far more scalable because the same loop and functions work for any n.
