"""
Variable Scope:
--------------

Scopes cab be `Global` or `Local`
"""

number = 10

def print_global_number():
    print(f"Global number is {number}")
print_global_number()

def print_num():
    number = 20
    print(f"Local num is {number}")
print_num()

def inc_number():
    global number
    number += 2

inc_number()
print(number)
