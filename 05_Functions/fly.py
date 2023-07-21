"""
Since Zortan has less gravity, residents can fly if they weight
less than or equal to 15 kgs in Zortan Weight

Louis wants to see which of his friends can fly.

Info:
-----
Our functions do only thing at a time, this is called `Single
Responsibility Principle` and important aspect of programming.
"""

from typing import Final


FRIEND_WEIGHT: Final[dict[str,int]]= { 'alan': 45, 'jasper': 55, 'kevin': 60, 'nestor': 200}

def calculate_zortan_weight(earth_weight: int) -> float:
    return (earth_weight + 32) / 8

def friend_can_fly(friends: dict) -> None:
    for friend in friends.keys():
        current_weight = calculate_zortan_weight(friends[friend])
        if current_weight < 15:
            print(f"{friend} can fly in Zortan => {current_weight}kgs")
        else:
            print(f"{friend} wont be flying any times sooner => {current_weight}kgs")

friend_can_fly(FRIEND_WEIGHT)
