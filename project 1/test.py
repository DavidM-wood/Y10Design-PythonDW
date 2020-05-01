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
    print("2. chips $1.50")
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
     price = 1.5
  elif inp == 2:
     price = 1.5
  elif inp == 3:
     price = 2.5
  elif inp == 4:
     price = 2.5
  else:
     price = 2.5
 
  if m < price:
    print("You do not have sufficient money, try again ")
    return 0
  else:
    print("Thanks - your change is $",m-price)
    return 1


while True:
  m = user_input()
  print("You have entered $",m)
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


input("Press ENTER to end program")


