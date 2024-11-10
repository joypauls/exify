import os
from fractions import Fraction


def get_file_name_from_path(path: str) -> str:
    return os.path.basename(path)


def decimal_to_fraction(decimal: float) -> str:
    # TODO: create cleaner fraction with numbers like 1/3
    return str(Fraction(decimal).limit_denominator())
