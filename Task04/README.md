# Task 4 - Expressions

    fat_steps = round((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / STEP_SIZE)
    rate_per_litre = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    payment = litres * rate_per_litre

- `**` has the highest precedence and is right-associative: 2 ** 3 ** 2 = 512.
- `-2 ** 2` is -4 because ** binds tighter than unary minus.
- (4.2 - 3.5) / 0.1 is not exactly 7 (my Python 3.12 run gave 7.000000000000002), so round() is used.
- For 3.1% fat the raw value is -3.999999999999999: round() and floor() give -4 steps but int()
  gives -3, so the rate becomes 28.80 instead of 28.40 (see output.txt). int() truncates toward zero,
  floor() goes toward negative infinity, round() goes to the nearest whole number.
- Comparison chaining `2.0 <= fat <= 7.0` means `2.0 <= fat and fat <= 7.0`.
- Complexity: round(), int() and math.floor() are all O(1) time and O(1) space.
