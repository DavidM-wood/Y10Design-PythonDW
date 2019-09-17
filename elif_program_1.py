# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Davi Wood
# Upper Canada College

# Put down some options for the user to choose from...
# This program is a modification to allow users to request usful information from me
print("What do you want to know?")
print("1. Classes")
print("2. Weather")
print("3. After school activities")
print(" ")
print("Choose one of the options above")

myrequest = int(input("What do you want? \n")) # newline character

if myrequest == 1:
    print("coding, french, gym, geo")
elif myrequest == 2:
    print ("Its fine")
elif myrequest == 3:
    print ("You got some puck and stick after school")
else:
    print ("This is not a valid choice")

   


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
