
from random import randint
from typing import Final
    
data_type = dict[str,str | int]

# Helper variables
hero_life = 0
villian_life = 0

def inc_hero_life(life: int) -> None:
    global hero_life
    hero_life += life
    
def dec_hero_life(life: int) -> None:
    global hero_life
    hero_life -= life
    
def inc_villian_life(life: int) -> None:
    global villian_life
    villian_life += life
    
def dec_villian_life(life: int) -> None:
    global villian_life
    villian_life -= life



def get_all_superheroes() -> list[data_type]:
# Super Heroes
    IRONMAN: Final[data_type] = {"name": "Ironman", "attack_power": 250, "life": 1000}
    BLACKWIDOW: Final[data_type] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
    SPIDERMAN: Final[data_type] = {"name": "Spiderman", "attack_power": 190, "life": 700}
    HULK: Final[data_type] = {"name": "Hulk", "attack_power": 300, "life": 1100}
    superheroes: list[data_type]= [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]

    return superheroes

def get_all_villian() -> list[data_type]:
# Super Villians
    THANOS: Final[data_type] = {"name": "Thanos", "attack_power": 1500, "life": 1500}
    REDSKULL: Final[data_type] = {"name": "Redskull", "attack_power": 300, "life": 800}
    PROXIMA: Final[data_type] = {"name": "Proxima", "attack_power": 320, "life": 800}

# All super heroes list
    villians: list[data_type]= [THANOS, REDSKULL, PROXIMA]
    return villians

def get_superhero(index: int) -> data_type | None:
    superheroes = get_all_superheroes()

    if index < len(superheroes):
        return superheroes[index]
    return None

def get_villian(index: int) -> data_type | None:
    villians = get_all_villian()

    if index < len(villians):
        return villians[index]
    return None

def attack() -> None:
# Attack
    for attack_number in range(3):
        # each iteration get a new hero and a villian
        random_hero_index = randint(0, len(get_all_superheroes()) - 1)
        random_villian_index = randint(0, len(get_all_villian()) - 1)

        current_hero = get_superhero(random_hero_index)
        current_villian = get_villian(random_villian_index)
        

        if current_villian and current_hero:
            simulate_attack(attack_number, current_hero, current_villian)
        else:
            print("Error!: No superheroes or villians found.")
            
def simulate_attack(attack_number: int, superhero: data_type, villian: data_type) -> None:
        
    inc_hero_life(superhero['life'])
    inc_villian_life(villian['life'])
    
    print(f"attack {attack_number + 1} => {superhero['name']} is attacking {villian['name']}")

    dec_hero_life(villian['attack_power'])
    dec_villian_life(superhero['attack_power'])


def win_or_lose() -> None:
    WIN_MSG: Final[str] = "You Successfully saved Zortan!"
    LOSE_MSG: Final[str] = "Thanos killed the Avengers and captured Zortan!"
    print("=" * 70)
    if hero_life >= villian_life:
        print(WIN_MSG)
    else:
        print(LOSE_MSG)
        
def main() -> None:
    attack()
    win_or_lose()

main()
