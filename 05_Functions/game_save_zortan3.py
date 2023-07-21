
"""
Let's convert the game logic into small functions.

Principle:
---------

1.DRY - Dont Repeat Yourself
============================
Try to keep your code as DRY as possible, group commmon functionality into
individual functions

2. SRP - Single Responsibility Principle
========================================
Ideally one function should be for only one operation

Note:
-----
We will also learn global and local scope of varibales (Using scrath pad)
"""
from random import randint
from typing import Final
data_type = dict[str,str | int]


def superheroes() -> list[data_type]:
# Super Heroes
    IRONMAN: Final[data_type] = {"name": "Ironman", "attack_power": 250, "life": 1000}
    BLACKWIDOW: Final[data_type] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
    SPIDERMAN: Final[data_type] = {"name": "Spiderman", "attack_power": 190, "life": 700}
    HULK: Final[data_type] = {"name": "Hulk", "attack_power": 300, "life": 1100}
    superheroes: list[data_type]= [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return superheroes

def villians() -> list:
# Super Villians
    THANOS: Final[data_type] = {"name": "Thanos", "attack_power": 1500, "life": 1500}
    REDSKULL: Final[data_type] = {"name": "Redskull", "attack_power": 300, "life": 800}
    PROXIMA: Final[data_type] = {"name": "Proxima", "attack_power": 320, "life": 800}

# All super heroes list
    villians: list[data_type]= [THANOS, REDSKULL, PROXIMA]
    return villians



WIN_MSG: Final[str] = "You Successfully saved Zortan!"
LOSE_MSG: Final[str] = "Thanos killed the Avengers and captured Zortan!"

def get_random_character(character_list: list[dict]) -> dict:
    random_character_index = randint(0, len(character_list) - 1)
    return character_list[random_character_index]

def character_attribute_variables(character: dict) -> tuple:
    return character['life'], character['attack_power']

# Attack
def check_winner(hero_remaining_life: int, villian_remaining_life: int) -> None:
    print("=" * 70)
    if hero_remaining_life >= villian_remaining_life:
        print(WIN_MSG)
    else:
        print(LOSE_MSG)
        
def main() -> None:
# Helper variables
    hero_life = 0
    villian_life = 0
    for attack in range(3):
        # each iteration get a new hero and a villian
        current_hero = get_random_character(superheroes())
        current_villian = get_random_character(villians())

        hero_life += character_attribute_variables(current_hero)[0]
        villian_life += character_attribute_variables(current_villian)[0]
        
        print(f"Attack {attack + 1} => {current_hero['name']} is attacking {current_villian['name']}")

        hero_life -= character_attribute_variables(current_villian)[1]
        villian_life -= character_attribute_variables(current_hero)[1]

    check_winner(hero_life, villian_life)
    
main()

