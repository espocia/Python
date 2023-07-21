"""
Functions:
---------
Think in data transformation -
`take somthing -> give something`

Delegate handling responsibility to the caller function

Tips:
-----
Very usefull pattern for testing
"""
zortan_friend: list[str] = ['Alfre', 'Roger', 'Rafa']


def greeter(friends: list) -> list:
    all_greetings: list[str] = []
    for friend in friends:
        all_greetings.append(f"Zola!! {friend}.")
    return all_greetings
    

def main() -> None:
    returned_value = greeter(zortan_friend)
    print(type(returned_value))

main()
