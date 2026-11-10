"""Task 3: named constants, dynamic typing, multiple assignment."""

# Rate card constants (UPPER_CASE by PEP 8 convention)
BASE_RATE = 30.00        # Rs per litre at standard fat and SNF
STANDARD_FAT = 3.5       # % fat baseline
STANDARD_SNF = 8.5       # % SNF baseline
FAT_STEP_VALUE = 0.40    # Rs per litre for every 0.1% fat
SNF_STEP_VALUE = 0.30    # Rs per litre for every 0.1% SNF
STEP_SIZE = 0.1          # size of one step in percent
MIN_FAT = 2.0
MAX_FAT = 7.0
MIN_SNF = 7.0
MAX_SNF = 10.0
PAYOUT_CYCLE_DAYS = 10

# Dictionary version of the rate card (alternative design)
RATE_CARD = {"base": 30.0, "fat": 0.40, "snf": 0.30}

if __name__ == "__main__":
    # Dynamic typing
    value = 42
    print(value, type(value))
    value = "forty-two"
    print(value, type(value))

    # Multiple assignment and swap
    a, b = 5, 10
    print("before:", a, b)
    a, b = b, a
    print("after :", a, b)
