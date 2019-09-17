# This is a trivia program
# Date: September 16 2019
# Author: David Wood



print("WHAT IS THE CAPITAL OF ONTARIO?")
print("1. Ottawa")
print("2. Toronto")
print("3. Kingston")
print("")

answer1 = int(input("Choose one of the options above \n"))

if answer1 == 1:
	print("Wrong answer")
elif answer1 == 2:
	print("Correct")
elif answer1 == 3:
	print("Wrong answer")
else:
	print("Not a valid answer")
print("")


print("WHEN DID CANADA BECOME A COUNTRY?")
print("1. 1776")
print("2. 1812")
print("3. 1867")

answer2 = int(input("Choose one of the options above \n"))

if answer2 == 1:
	print("Wrong answer")
elif answer2 == 2:
	print("Wrong answer")
elif answer2 == 3:
	print("Correct")
else:
	print("Not a valid answer")

print("")


print("WHAT IS CANADA'S NATIONAL SPORT?")
print("1. Hockey")
print("2. Lacrosse")
print("3. Basketball")
print("")

answer3 = int(input("Choose one of the options above \n"))

if answer3 ==1:
	print("Wrong answer")
elif answer3 == 2:
	print("Correct")
elif answer2 == 3:
	print("Wrong answer")
else:
	print("Not a valid answer")

print("")
print("Thanks for playing!")
print("")




input("Press ENTER to quit the program")