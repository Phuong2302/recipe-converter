from fractions import Fraction


def convert_ingredient_volume_to_mass(line: str) -> str:
    return "foo"


def fraction_to_float(fraction: str) -> float:
    """Convert string representation of a fraction to float

    Args:
        fraction (str): String representation of fraction, ie. "3/4", "1 1/2", etc.

    Returns:
        float: Converted fraction
    """
    return float(sum(Fraction(s) for s in fraction.split()))
