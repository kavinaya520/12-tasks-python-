"""Task 12: revised design with seasonal rates, two-decimal readings and bonus."""
from decimal import Decimal, ROUND_HALF_UP

STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
STEP_SIZE = Decimal("0.1")
BONUS_LIMIT_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

# One rate card per season; the season is chosen by a function
RATE_CARDS = {
    "normal": {"base": Decimal("30.00"), "fat": Decimal("0.40"), "snf": Decimal("0.30")},
    "apr_jun": {"base": Decimal("32.00"), "fat": Decimal("0.45"), "snf": Decimal("0.30")},
}


def season_for_month(month):
    """Return 'apr_jun' for months 4 to 6, otherwise 'normal'."""
    return "apr_jun" if 4 <= month <= 6 else "normal"


def validate_reading(fat, snf):
    """Raise ValueError if the analyser readings are outside the allowed range."""
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("fat must be between 2.00 and 7.00")
    if not Decimal("7.0") <= snf <= Decimal("10.0"):
        raise ValueError("snf must be between 7.00 and 10.00")


def money(value):
    """Round to 2 decimals using half-up rounding."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def rate_per_litre(fat, snf, season="normal"):
    """Rate for two-decimal readings (strings or Decimals); fractional steps allowed."""
    fat, snf = Decimal(str(fat)), Decimal(str(snf))
    validate_reading(fat, snf)
    card = RATE_CARDS[season]
    fat_steps = (fat - STANDARD_FAT) / STEP_SIZE
    snf_steps = (snf - STANDARD_SNF) / STEP_SIZE
    return money(card["base"] + fat_steps * card["fat"] + snf_steps * card["snf"])


def payout(litres, fat, snf, season="normal"):
    """Payment for one entry without bonus."""
    return money(Decimal(str(litres)) * rate_per_litre(fat, snf, season))


def bonus(total_litres):
    """Bonus of Rs 0.50 per litre on all litres if the ten-day supply exceeds 500 litres."""
    litres = Decimal(str(total_litres))
    return money(litres * BONUS_PER_LITRE) if litres > BONUS_LIMIT_LITRES else Decimal("0.00")


def ten_day_total(entries, season="normal"):
    """Total for ten days: sum of payments plus bonus. entries = [(litres, fat, snf)]."""
    total = sum((payout(l, f, s, season) for l, f, s in entries), Decimal("0"))
    litres = sum((Decimal(str(l)) for l, _, _ in entries), Decimal("0"))
    return total + bonus(litres)
