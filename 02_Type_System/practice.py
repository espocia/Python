"""
Louise wants to open a Pizza Shop and needs to write
a program for accepting orders.

Tip -
-----
Always Visualize First, Then Start Coding.
"""

# ---------------------#
# Variable Declecation #
# ---------------------#

customer: str = "Cece"
pizza_base: str = "Thin"
pizza_size:  int = 12
pizza_toppings: str = "Olives"
extra_cheese: bool = True
price: float = 8.99

#--------------------------------#
# Alternative 1 - Using Function #
#--------------------------------#

print(f"Recieved Order From: {customer}")
print(f"Pizza Base: {pizza_base}")
print(f"Pizza Size: {pizza_size} inches")
print(f"Pizza Topping: {pizza_toppings}")
print(f"Extra Cheese: {extra_cheese}")
print(f"Bill: {price}")

#-----------------------------------------#
# Alternative 1 - Using Formating Strings #
#-----------------------------------------#

order_details: str = f""" 
Recieved order from : {customer}
Pizza Base          : {pizza_base}
Pizza Size          : {pizza_size}
Pizza Topping       : {pizza_toppings}
Extra Chees         : {extra_cheese}
Bill                : {price}
"""

print(order_details)


#----------------------------------------------------#
# Alternative 3 - Using Formating Strings in `print` #
#----------------------------------------------------#

print(f""" 
Recieved order from : {customer}
Pizza Base          : {pizza_base}
Pizza Size          : {pizza_size}
Pizza Topping       : {pizza_toppings}
Extra Chees         : {extra_cheese}
Bill                : {price}
"""
)
