"""
Louis wants to drive a car and he hears that in planet
Zortan there is not age limit for getting a license

"""

age: int = 16
planet: str = "Zortan"

#--------------------#
# And / Or statement #
#--------------------#

if age < 16 and planet == "Earth":
    print("You are NOT eligible for a license on Earth.")
elif age >  16 and planet == "Earth":
    print("You can apply for license on Earth.")
elif age < 16 or planet  == "Zortan":
    print("You can apply for license on Zortan")

