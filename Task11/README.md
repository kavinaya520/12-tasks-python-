# Task 11 - Final Design Recommendation

- Data types: Decimal (built from strings) or integer paise for money; strings for IDs and shifts.
- Rounding: round each payment to 2 decimals (half up) and add the rounded payments.
- Rate revision: change rates in one place (a rate card or rates.json), then re-run Task09 tests
  and Task12 tests before using the new rates. Keep the old card with its start date.
- Limitations: step rounding rules must be agreed with the co-operative, the SNF range is an
  assumption, and a dictionary or file does not check rate values by itself (add validation).
- Scale: processing is O(n) in time and O(1) extra space with a running total. In Task 10,
  150,000 entries took about 0.45 s with Decimal, so district-union scale (150,000 farmers) is
  fine for one calculation run. Storing entries in a database is the next step beyond that.

## Rate card in a JSON file
    rates.json: {"base": 30.0, "fat": 0.40, "snf": 0.30}
Loading it at start-up costs O(t) time and space for t values (tiny). Rate revisions then need
only a file edit instead of editing and redistributing the program, but a bad edit can break
payments, so the loaded values must be validated.
