from replit import db
import random
#_______________________________________________________
def addNewUser(db):
  print("\033[1;32m\nAdd new user\033[0m\n")
  username = myInputPrint("Username: ")
  password = myInputPrint("Password: ")
  salt = random.randint(1000, 9999)
  newPassword = f"{password} {salt}"
  newPassword = hash(newPassword)
  db[username] = {"password": newPassword, "salt": salt}
  print("\nUser Added\n")
#______________________________________________________
def myInputPrint(text):  #prints input text with green clolor
  result = input(f"""{text} \033[32m""")
  print("\033[0m", end="")
  return result
#______________________________________________________
def logIn(db):
  print("\033[1;32m\nLog in\033[0m")
  username = myInputPrint("Username: ")
  if username not in db:
    print("\nNo such username!\n")
    return
  password = myInputPrint("Password: ")
  salt = db[username]["salt"] 
  newPassword = f"{password} {salt}"
  newPassword = hash(newPassword)
  if newPassword == db[username]["password"]:
    print(f"\nHello {username}, welcome back!\n")
    return
  else:
    print("\nIncorrect password\n")
    return
#################MAIN###################################
print("\033[1;32mLogin system\033[0m\n")
while True:
  try:
    choice = int(myInputPrint("Press 1: Add new user\nPress 2: Login\nPress 3: Exit\n> "))
  except:
    print("\033[1;31mThe choice should be integer.\033[0m\n")
    continue
  if choice == 1:
    addNewUser(db)
  elif choice == 2:
    logIn(db)  
  elif choice == 3:
    print("\033[1;32m\nBye!\033[0m")
    break
  else:
    print("\033[1;31mIncorrect input\033[0m\n")
    continue

