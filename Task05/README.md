# Task 5 - Input and Type Conversion

- input() returns a string because the keyboard gives text; the program must convert it.
- try/except ValueError converts and handles bad input in one step (EAFP style).
- String-method validation (isdigit) checks before converting (LBYL style).

| Text | try/except float() | strip + isdigit check |
|---|---|---|
| "8,5" | invalid (ValueError) | invalid |
| " 8.5 " | 8.5 (float() ignores spaces) | 8.5 after strip() |
| "eight" | invalid | invalid |

Both are O(L) per entry where L is the length of the text. try/except is shorter and handles
cases like "1e3" or "-2.5" automatically; the string check needs extra rules for each format.
