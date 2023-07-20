"""
First Bug
---------

Undersired behavior in programming is called as `Bugs`.

Python is dynamically typed language so it's easy to introduce a bug.

"""

box = "Balloons"
print(f"Box contains: {box}")

box = 10
print(f"Box contains: {box}")

#-----------------------------------------------------------------------------#
# Introducing `Type Hinting` -Optional Static Checking in Python Using `Mypy` #
#-----------------------------------------------------------------------------#

name: str = "Louise"
food: str = "Milk"
print(f"{name} is going to drink {food}")

food = "Eggs"
print(f"{name} is going to drink {food}")

food = False
print(f"{name} is going to drink {food}")

