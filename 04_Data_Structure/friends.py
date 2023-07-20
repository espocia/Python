"""
List:
-----
Louis has been making good progress in Zortan and has made
new friends. All of them are meeting today and Louis wants
to write a program that can greet all of them.

In Zortan, people greet with saying "Zola"

Info:
-----
Lists are mutable data structures, that means the data inside can be mutated
Index always start from 0.
"""

# It's convinient to group all friends together using a `List`
# and then greet them
friends: list[str] = ["Cece", "Roko", "Chiko", "Niko"]
# List  with index   [   0,      1,      2,       3  ]
print(friends)

#------------------------------------------------------
# Time to greet friends using a for-loop
#------------------------------------------------------

for friend in friends:
    print(f"Zoral {friend}")

# Louis wants to count his nuumber of friends 
for i, friend in enumerate(friends):
    print(f"{i+1}: {friend}")
print(f"Louis has {len(friends)} friends")

#------------------------------------------------------
# Louis had a fight with Niko and wants to unfriend him
#------------------------------------------------------

unfriend = friends.pop()
print(f"""
unfriend = {unfriend}
friends  = {friends}
""")

#------------------------------------------------------
# Louis makes a new friend "Ziko"
#------------------------------------------------------

newfriend = "Ziko"
friends.append(newfriend)
print(f"""
new friend = {newfriend}
friends    = {friends}
""")

#------------------------------------------------------
# Louis wants to check who is 3rd in his friend list
#------------------------------------------------------

print(f"{friends[2]} is the 3rd friend")

#------------------------------------------------------
# Oh-no Louis again had a a fight, this time with Roko
#------------------------------------------------------

removed_friend = "Roko"
friends.remove(removed_friend)
print(f"""
removed friend = {removed_friend}
friends        = {friends}
""")

#------------------------------------------------------
# Louis and Roko are friends again
#------------------------------------------------------

friends.insert(1, removed_friend)
print(f"""
added friend = {removed_friend}
friends      = {friends}""")

#------------------------------------------------------
# Louis want to confirm is Roko is in the friend list
#------------------------------------------------------

print(f"{removed_friend} is in the friend list: {removed_friend in friends}")

#---------------------------------------------------------
# Louis want to sort his friends in an alphabethical order
#---------------------------------------------------------

friends.sort()
print(f"sorted to alphabethical order: {friends}")

#---------------------------------------------------------------
# Louis doesn't like this odering and wants to reverse the order
#---------------------------------------------------------------

friends.reverse()
print(f"sorted in reverse: {friends}")
