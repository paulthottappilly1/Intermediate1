# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
#https://www.quora.com/How-can-I-make-the-user-input-key-and-value-dictionary-in-Python-e-g-classe_list-input-name-score-wrong-syntax

from operator import itemgetter

# adds dict items with common keys
def get_combined_dict(my_dict_1, my_dict_2):
    # creates empty dictionary
    newdict = {}
    # combines dictionary elements with common key
    for k, v in my_dict_1.items():
        if (k in my_dict_2.keys()):
            newdict[k] = v + my_dict_2[k]
    # returns the new dictionary
    return newdict

# prompts user to enter how many elements they want in the dict
number= int(input("Enter number of elements for the dict: "))

# obtains user input and add them to dict1
dict1 = dict()
for x in range(number): 
    data = input('Enter letter and the number separated by ":" for dict1 ') 
    split = data.split(':') 
    dict1[split[0]] = int(split[1]) 

# obtains user input and add them to dict2
dict2 = dict()
for x in range(number): 
    data = input('Enter letter and the number separated by ":" for dict2 ') 
    split = data.split(':') 
    dict2[split[0]] = int(split[1]) 

# displaying the dictionary 
print('Dictionary 1 is: ') 
print(dict1)
print('Dictionary 2 is: ')
print(dict2)

# calls the function
combined_dict = get_combined_dict(dict1, dict2)
print('The combined dictionary is: ')
print(combined_dict)