from random import randint
from typing import Final


data_type = dict[str,str | int]
# Super Heroes
IRONMAN: Final[data_type] = {"name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[data_type] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[data_type] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[data_type] = {"name": "Hulk", "attack_power": 300, "life": 1100}

# Super Villians
THANOS: Final[data_type] = {"name": "Thanos", "attack_power": 1500, "life": 1500}
REDSKULL: Final[data_type] = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[data_type] = {"name": "Proxima", "attack_power": 320, "life": 800}

# All super heroes list
superheroes: list[data_type]= [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
villians: list[data_type]= [THANOS, REDSKULL, PROXIMA]

# Helper variables
hero_life = 0
villian_life = 0

WIN_MSG: Final[str] = "You Successfully saved Zortan!"
LOSE_MSG: Final[str] = "Thanos killed the Avengers and captured Zortan!"

# Attack
for attack in range(3):
    # each iteration get a new hero and a villian
    random_hero_index = randint(0, len(superheroes) - 1)
    random_villian_index = randint(0, len(villians) - 1)

    current_hero = superheroes[random_hero_index]
    current_villian = villians[random_villian_index]

    hero_life += current_hero['life']
    villian_life += current_villian['life']
    
    print(f"Attack {attack + 1} => {current_hero['name']} is attacking {current_villian['name']}")

    hero_life -= current_villian['attack_power']
    villian_life -= current_hero['attack_power']


print("=" * 70)
if hero_life >= villian_life:
    print(WIN_MSG)
else:
    print(LOSE_MSG)


    
