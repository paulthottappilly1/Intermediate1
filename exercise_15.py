# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
# https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

def repeated_letter_dict(str):
    # turns all the letters in the strings lowercase
    str = str.lower()
    # takes all of the space and removes it
    str = str.replace(" ", "")

    # creates a dictonary to hold all the repeated letters in the string
    repeatdict = {}
    # creates a loop to make x equal to each character within the string
    for x in str:
        # creates an if statement to check if the characters of the string is located within the dictonary
        if x in repeatdict:
            repeatdict[x] = repeatdict[x] + 1
        # if the characters of the string are found in the dictonary 
        # it will then add that character to the dictonary and make it equal to 1
        else:
            repeatdict[x] = 1
    
    print(repeatdict)

# this calls the function
user_string = input("Enter a string: ")
repeated_letter_dict(user_string)
