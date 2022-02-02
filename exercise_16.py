# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise  
# https://stackoverflow.com/questions/55437419/how-to-use-the-try-except-command-in-a-while-loop-asking-for-user-input

s = 0
# create a for loop that will continue until 5 integers are entered
for x in range(5):
    # allows the try block to always be executed to attempt taking in a user integer
    while True:
        # tries to take in the user input as an int and add that number to the already existing sum if it passes
        try:
            usernumber = int(input("Please enter an integer: "))
            s = s + usernumber
            break
        # if an int isn't entered, it will tell the user to enter another int
        except ValueError:
            print("Invalid input, please enter an integer")
            continue

# prints out the resulting sum
print('Your sum is:', s)