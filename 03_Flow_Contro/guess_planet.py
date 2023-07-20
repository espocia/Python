"""
Friends from Earth want to know where is Louis, so Louis decides to
write a program that will make his friends guess the name of planet.
"""
guess_planet: str = ""
louis_planet: str = "Zortan"

while True:
    guess_planet = input("Guess where Louise is: ")

    if guess_planet.lower() == louis_planet.lower():
        print("You got it!")
        break
    print("Try Again! ")
