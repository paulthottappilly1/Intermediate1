# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links used below for exercise 
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
# https://www.w3resource.com/python-exercises/python-functions-exercise-8.php

def get_unique_list(y):
    # creates an empty list
    u = []
    # iterating through the list
    for x in y:
        # appends unique values on to a new list
        if x not in u:
            u.append(x)
    return u

# creates an empty list
my_list = []
z = int(input("Enter number of elements for the list: "))
 
# iterating to the range
for i in range(0, z):
    # enter elements for the list
    element = int(input("Enter element: "))
    my_list.append(element)

print(get_unique_list(my_list))
