# Task 12 - Day-4 Design Challenge

## A. Impact analysis
- New: analyser gives 2-decimal fat/SNF, April-June base 32.00 and fat step 0.45, and a bonus of
  Rs 0.50 per litre when ten-day supply is above 500 litres.
- Must change: constants (become rate cards per season), the rate function (needs a season),
  the ten-day total (needs the bonus), validation (2-decimal readings).
- Two-decimal readings: a reading like 4.25 is half a step; round() to whole steps would lose it
  (and float errors grow), so fractional steps with Decimal are used.

## B. Evaluation of the original design
The original float design with whole-step rounding does not fit: constants are fixed, there is no
season, and rounding to whole steps changes the amount paid. The module idea (milkrate.py) and
the function structure are still good and are kept.

## C. Revised design
milkrate_v2.py: RATE_CARDS dictionary, season passed as a parameter, a separate bonus() function,
Decimal throughout, half-up rounding to 2 decimals.
Assumption: the bonus applies to all litres once the ten-day total exceeds 500.

## D. Defence and tests
test_v2.py (output_tests.txt) tests original and seasonal rates with and without bonus; all pass.
Decision: modify (not rewrite) the design. Trade-off: Decimal is slower than float but exact,
and the dictionary is slightly slower than constants but handles any number of seasons.
