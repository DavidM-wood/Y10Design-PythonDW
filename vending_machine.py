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
price1 = 0.0
price2 = 0.0
price3 = 0.0
price4 = 0.0
price5 = 0.0


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

def purchase (inp, m):
  price = 0.0
  if inp == 1:
     price1 = 1.5
  elif inp == 2:
     price2 = 1.5
  elif inp == 3:
     price3 = 2.5
  elif inp == 4:
     price4 = 2.5
  elif inp == 5:
      price5 = 2.5
  else:
     print ("Provide a valid option!!!!!")
 
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

  if m < p:
    print("You do not have sufficient money, try again ")
    #return 0
  else:
    print("Thanks - your change is $",m-p)

  
    print("You have entered $",m)
  
  NumItems = int(input ("Please enter how may of each item you would like \n"))

  

  print("You have requested " + str(NumItems) + " items")

  numOfChocolatebars = numOfChocolatebars - NumItems
  print ("We now have " + str(numOfChocolatebars))



  