"""
Higher Order Functions:
----------------------
Please note thatt thtis is an advanced topic, so it may take a couple of attempts
to understand this concepts.

Functions under the hood are just `Objects` they can be passed to other
function and functions can also return functions!

This data type is called a `Callable` one which can be called invoked.

Note:
-----
Till now we have been sending data to our functions, but sending data everytime
can be expensive, instead we can send functions to the data!
"""

from typing import Callable

def hello() -> None:
    print("Hello World.")
    
hello2 = lambda name: f"Hello two {name}"
print(hello2('josh'))

# hello is just a regular object or class of type 'function'
print(hello)
print(id(hello))
print(type(hello()))

# We can assign functions to variables
greet: Callable[[], None]= hello # just assign the object 'hello' to greet variable
greet() # we ca invoke/call the functions using `()` at the end

# --------------------------------------------------------------

"""
Let's try to create a universal greeter that can greet a person in multiple
ways
"""
def zola(name: str) -> str:
    return f"Zola, {name}"

def good_morning(name: str) -> str:
    return f"Good morning, {name}"

def goodbye(name: str) -> str:
    return f"Goodbye {name}"

def universal_greeter(name: str, greet: Callable[[str],str]):
    msg = greet(name)
    print(msg)

universal_greeter('josh', zola)

"""
Functions returning Functions!!!
-----------------------------
"""

def add_by_5(num: int) -> Callable[[], int]:
    
    def by_5() -> int:
        return num + 5
    return by_5

print(add_by_5(5)())

# function returning function

def universal_adder(num1: int) -> Callable[[int], int]:
    
    def adder(num2: int) -> int:
        return (num1 + num2) - 1
    return adder

print(universal_adder(5)(5))

"""
lambda:
-------
Perhaps the most neglected, but very powerful technique to work with functions
Again, dont spend too much time mastering it, iit will come naturally!

The way in which we declare function are very verbose, we can condense them
in a single statement.

Let's try to create a calculator from scratch
"""

data_type = Callable[[int, int], int]
add: data_type = lambda num1, num2: num1 + num2
sub : data_type = lambda num1, num2: num1 - num2
mult: data_type = lambda num1, num2: num1 * num2
div: Callable[[int, int], float]= lambda num1, num2: num1 / num2

def calc(num1: int, num2: int, operation: Callable[[int, int], int | float]):
    return operation(num1, num2)

print(calc(10,5,sub))
