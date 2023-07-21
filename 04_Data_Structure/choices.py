"""
ENUM:
-----

This is a very good data structure for creating choices or variaties
"""

from enum import Enum, auto

class PizzaSize(Enum):
    """ Pizza Base Size """

    SMALL = 8
    MEDIUM = 10
    LARGE = 12

choices = PizzaSize.MEDIUM

print(f"One order for {choices.value} inch pizza")

class Color(Enum):
    """T-Shirt variaties"""
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

print(f"One order for {Color.RED.value} T-Shirt")

class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()
print(Role.ASSOCIATE.value)
