# Task 2 - Values and Types

Interactive session (annotated):

    >>> type(10)          <class 'int'>
    >>> type(10.0)        <class 'float'>
    >>> type("10")        <class 'str'>
    >>> type(True)        <class 'bool'>
    >>> type([10, 8.5])   <class 'list'>
    >>> 7 / 2             3.5     true division
    >>> 7 // 2            3       floor division
    >>> 7 % 2             1       remainder
    >>> -7 // 2           -4      floor division rounds toward negative infinity
    >>> 0.1 + 0.2 == 0.3  False   the sum is 0.30000000000000004

Why floats are risky for money: they are stored in binary and values like 0.1 have no exact
binary form, so tiny errors build up over many additions.

| Approach | Precision | Ease | Note |
|---|---|---|---|
| Integer paise | exact | needs conversion | fastest, common in payment systems |
| round() | approximate | simple | still float based |
| decimal | exact | a little verbose | best for totals, slower |

Decimal(float(amount)): the float is already inexact, so Decimal copies the error exactly
(total 33400.29999999999857893118278 in my run). Always build Decimal from a string.

Additional question (see output.txt for measured sizes): Decimal 104 bytes, int 28, float 24.
All are O(1) per addition; integer paise is fastest and exact, Decimal is exact but slower,
float with rounding after each addition is fast but not guaranteed exact over large volumes.
