"""Task 5: read clerk entries and convert types safely."""


def to_float_try(text):
    """Convert text to float using try/except ValueError. Return None if invalid."""
    try:
        return float(text)
    except ValueError:
        return None


def to_float_checked(text):
    """Validate with string methods first, then convert. Return None if invalid."""
    cleaned = text.strip()
    if cleaned.replace(".", "", 1).isdigit():
        return float(cleaned)
    return None


def read_entry():
    """Read one entry from the clerk (input() always returns a string)."""
    farmer_id = input("Farmer ID : ").strip()
    litres = to_float_try(input("Litres    : "))
    fat = to_float_try(input("Fat %     : "))
    snf = to_float_try(input("SNF %     : "))
    return farmer_id, litres, fat, snf


if __name__ == "__main__":
    print("int() and float() conversions")
    print(int("12"), float("8.5"), int(float("12.0")))

    print("\nHandling invalid input")
    print(f"{'text':>10} | {'try/except':>10} | {'str methods':>11}")
    for text in ("8.5", " 8.5 ", "8,5", "eight"):
        print(f"{text!r:>10} | {str(to_float_try(text)):>10} | {str(to_float_checked(text)):>11}")

    print("\nFormatted output with f-strings")
    amount = 283.9
    print(f"Amount: {amount:8.2f}")
    print(f"{'F001':<6}{10.0:>7.1f} L{300.0:>10.2f}")
