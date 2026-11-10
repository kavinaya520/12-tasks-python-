"""Task 6: payment logic as reusable functions."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
STEP_SIZE = 0.1


def rate_per_litre(fat, snf):
    """Return the price per litre for the given fat and SNF, rounded to 2 decimals."""
    fat_steps = round((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / STEP_SIZE)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment for one entry, rounded to 2 decimals."""
    return round(litres * rate_per_litre(fat, snf), 2)


def ten_day_total(entries):
    """Return the total payment for a farmer; entries is a list of (litres, fat, snf)."""
    total = 0.0
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return round(total, 2)


if __name__ == "__main__":
    # return vs print: payout() returns a value we can reuse; print only shows it
    amount = payout(10, 3.5, 8.5)
    print("returned value reused:", amount * 2)
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    print("ten-day total:", ten_day_total(entries))

    # lambda version (one-line helper)
    square = lambda x: x * x
    print("lambda example:", square(4))

    # Scope: constants are read inside functions, never modified
    counter = 0          # global

    def local_demo():
        """Show that a local variable does not change the global one."""
        counter = 99     # local variable, separate from the global
        return counter

    print(local_demo(), counter)
