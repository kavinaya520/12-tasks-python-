# Task 9 - Implementation and Testing

calculator.py uses the rate function from Task07/milkrate.py, validates every entry, and adds
payments exactly with Decimal. test_calculator.py prints the test table (output_tests.txt):
input, expected result, actual result and PASS/FAIL for every case.

Manual vs automated testing:
- Manual: type inputs and read the output each time; slow and easy to forget cases.
- Automated (function plus assert): all cases run in one command in well under a second, so
  they are re-run after every change at almost no extra effort.
