"""
Gravity wrorks diffrently in Zorta, use the following formula
to see how mych you weight on Zortan.

Zortan Weight = (Earth Weight + 32) / 8
"""

def calculate_zortan_weight(earth_weight) -> float:
    return (earth_weight + 32) / 8

EARTH_WEIGHT: int = 55
zortan_weight = calculate_zortan_weight(EARTH_WEIGHT)
print(f"your earth weigth is {EARTH_WEIGHT} and your Zortan weight is {zortan_weight:.2f}")
