"""
Functions:
---------

It's all about data transformation ideally it should
`take somethingg -> give something`

Or else, it causes a `side effect`

Remember people in Zortan greet each other by saying Zola
Louis wants to write a program which can greet any Zortan
""" 

zortan_friend: list[str] = ['Alfre', 'Roger', 'Rafa']

def greeter(friends: list) -> None:
    for friend in friends:
        print(f"Zola!! {friend}.")

def main() -> None:
    greeter(zortan_friend)

main()
