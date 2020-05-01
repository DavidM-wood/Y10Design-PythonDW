# this is a program that is based on how a vending machine works. 
# Author: David Wood
# Upper Canada College
# Date: September 20 2019

numOfChocolatebars = 10
numOfChips = 10
numOfSoda = 10
numOfGatorade = 10
numOfWater = 10

# These are placeholders for the prices of the objects in the machine
price1 = 1.5
price2 = 1.5
price3 = 2.5
price4 = 2.5
price5 = 2.5


# m represents... the money in int form 
# p represents... the purchase
# "inp" represents the option chosedn by the user
# ???? represents the amount of each item we are requesting

# input is examined and we will ignore the $ sign
#
def user_input():
  while True:
    money = input("Enter money: ")
    if money[0] != '$':
      print('Use $ infront of money: ')
    elif money[1:].isdigit() != True:
      print('All numeric values expected: ')
    else:
      m = int(money[1:])
      break
  return m

def item_selection():
  while True:
    print('\n')
    print("1. Chocolate bar $1.50")
    print("2. Chips $1.50")
    print("3. Soda $2.50")
    print("4. Gatorade $2.50")
    print("5. Water $2.50")
    print("Enter item number to purchase:")
 
    inp = input()
    if inp.isdigit() == True:
      inp = int(inp)
      if inp in range (1,6):
        break
      else:
        print('Wrong selection, try again ')
    else:
      print('Wrong selection, try again ')
  return inp


# The function "purchase" takes two values - an input and an amount of money

def purchase (inp, m):
  if inp == 1:
    if m < price1:
      print ("This is not enough money!!!")
    elif m > price1:
      print ("Processing request...grab your item at the bottom")
      print ("your change is " + str(m-price1))
    else:
      NumItems = int(input ("Please enter how may of each item you would like \n"))
      print("You have requested " + str(NumItems) + " items")

      numOfChocolatebars = numOfChocolatebars - NumItems
      print ("We now have " + str(numOfChocolatebars))

  if inp ==2:
    if m < price2:
      print ("This is not enough money!!!")
    elif m > price2:
      print ("Processing request...grab your item at the bottom")
      print ("your change is " + str(m-price2))
    else:
      NumItems = int(input ("Please enter how may of each item you would like \n"))
      print("You have requested " + str(NumItems) + " items")

      numOfChips = numOfChips - NumItems
      print ("We now have " + str(numOfChips))


  if inp == 3:
    if m < price3:
      print ("This is not enough money!!!")
    elif m > price3:
      print ("Processing request...grab your item at the bottom")
      print ("your change is " + str(m-price3))
    else:
      NumItems = int(input ("Please enter how may of each item you would like \n"))
      print("You have requested " + str(NumItems) + " items")

      numOfSoda = numOfSoda - NumItems
      print ("We now have " + str(numOfSoda))



  if inp == 4:
    if m < price4:
      print ("This is not enough money!!!")
    elif m > price4:
      print ("Processing request...grab your item at the bottom")
      print ("your change is " + str(m-price4))
    else:
      NumItems = int(input ("Please enter how may of each item you would like \n"))
      print("You have requested " + str(NumItems) + " items")

      numOfGatorade = numOfGatorade - NumItems
      print ("We now have " + str(numOfGatorade))


  if inp == 5:
    if m < price1:
      print ("This is not enough money!!!")
    elif m > price5:
      print ("Processing request...grab your item at the bottom")
      print ("your change is " + str(m-price5))
    else:
      NumItems = int(input ("Please enter how may of each item you would like \n"))
      print("You have requested " + str(NumItems) + " items")

      numOfWater = numOfWater - NumItems
      print ("We now have " + str(numOfWater))





  

# THis is where the program starts 

while True:
  m = user_input()
  inp = item_selection()
  p = purchase(inp, m)
  if p == 1:
    print("Print 'q' to quit, 'c' to continue ")
    r = input()
    if r == 'q':
      break
    else:
      pass
  else:
    pass

  



  