"""
Zortan is under attach!!! Thano has arrived!
--------------------------------------------

Since Zortan is under attach, Louis calls his Avenger friends from earth.
Avengers receives his call sends 4 Avengers to save Zortan.

1. Ironman = 250
2. Spiderman = 190
3. Hulk = 300
4. Black Widow = 250

thanos_life = 1500

Each avenger has its attacking power and they have to fight Thanos
to save Zortan.

Avengers can attach only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill the avengers and we lose the game.
"""
from typing import Final

ATTACK_POWERS: Final[dict] = {"ironman": 250, "spiderman": 190, "hulk":300, "widow": 250}
thanos_life: int = 1500

def attribute_selector(pair_selector):
    selector = ""
    match pair_selector:
        case 1:
            selector = "ironman"
        case 2:
            selector = "spiderman"
        case 3:
            selector = "hulk"
        case 4:
            selector = "widow"
    return selector

def pair_selection_validate(selection):
    
    valid_selection: list = ["1", "2", "3", "4"]
    
    while selection not in valid_selection:
        print("Input is not in the selection please try again")
        selection = input("new input: ")
        
    return int(selection)

def hero_selector():
    MSG = """

    Zortan is under attack select your pair
    ---------------------------------------
    1. Ironman 
    2. Spiderman
    3. Hulk 
    4. Black Widow
    ---------------------------------------

    """
    print(MSG)
    total_damage: int = 0
    choices: list = [0, 0]

    while total_damage <= 300:
        while True:
            print("""
            Please choose 2 different heroes
            --------------------------------
            """)
            if total_damage <= 0:
                pair_selection = input("Select your first hero: ")
                choices[0] = pair_selection_validate(pair_selection)
                total_damage += ATTACK_POWERS[attribute_selector(choices[0])]
            else:
                pair_selection = input("Select your second hero: ")
                choices[1] = pair_selection_validate(pair_selection)
                total_damage += ATTACK_POWERS[attribute_selector(choices[1])]
                
                
            if choices[0] == choices[1]:
                print("Invalid: Duplicate heroes, please Try again!")
                total_damage = 0
            elif choices[0] != choices[1] and (choices[0] != 0  and choices[1] != 0):
                return total_damage

def main_game(thanos):
    for i in range(3):
        attack_power: int = hero_selector()
        thanos -= attack_power
        
        print(f"""
        --------------------------------------------------
        Your Hero's combined attack damage: {attack_power}
        Thano's life remaining:             {thanos}
        Rounds:                             {i+1} of 3
        --------------------------------------------------
        
        """)
        
        if i + 1 == 3 and thanos > 0:
            print("You lost")
        elif thanos <= 0:
            print("we won!")
            
main_game(thanos_life)
