import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

nameList = ['flavius', 'fabricio']
phoneList = ['99999-1111', '99999-2222']
emailList = ['flavius@ufrn.br', 'fabricio@ufrn.br']
birthList = ['26/11/1970', '08/08/1980']

def register():
  cls()
  choice = "0A6FD2"
  while choice == "0A6FD2":
    name = input("Insert Name:\n")
    name = name.title()
    while True:
      phone = input("Insert Phone Number:\n")
      if len(phone) == 9 and phone.isnumeric() == True:
        phone = phone[:5]+"-"+phone[5:9]
        break
      elif phone.isnumeric() == False:
        print("Invalid Phone Number, insert one with only numbers.")
      else:
        print("Invalid Phone Number, insert one with 9 numbers.")
    while True:
      email = input("Insert Email:\n")
      if "@" in email and "." in email:
        break
      else:
        print("Invalid email, it must contain @ and a dot.")
    while True:
      birthday = input("Insert Birthday:\n")
      if len(birthday) == 8 and birthday.isnumeric() == True:
        birthday = birthday[:2]+"/"+birthday[2:4]+"/"+birthday[4:8]
        break
      elif birthday.isnumeric() == False:
        print("Invalid birthday, insert one with only numbers.")
      else:
        print("Invalid birthday, insert one with 8 numbers(MM/DD/YYYY).")
    nameList.append(name)
    phoneList.append(phone)
    emailList.append(email)
    birthList.append(birthday)
    choice = input("Enter to go back to the main menu\n")
  contactList()

def search():
  cls()
  choice = "0A6FD2"
  while choice == "0A6FD2":
    try:
      index = nameList.index(input("Insert Name to Start Searching:\n"))
      print("\nIndex:",index)
      print("Name:",nameList[index])
      print("Phone:",phoneList[index])
      print("Email:",emailList[index])
      print("Birthday:",birthList[index],"\n")
    except Exception:
      print("Nothing was found...")
    choice = input("Enter to go back to the main menu\n")
  contactList()

def update():
  cls()
  choice = "0A6FD2"
  while choice == "0A6FD2":
    index = int(input("Insert item index to update:\n"))
    if index <= len(nameList):
      nameList[index] = input("Insert New Name:\n").title()
      while True:
        phone = input("Insert New Phone Number:\n")
        if len(phone) == 9 and phone.isnumeric() == True:
          phoneList[index] = phone[:5]+"-"+phone[5:9]
          break
        elif phone.isnumeric() == False:
          print("Invalid Phone Number, insert one with only numbers.")
        else:
          print("Invalid Phone Number, insert one with 9 numbers.")
      while True:
        email = input("Insert New Email:\n")
        if "@" in email and "." in email:
          emailList[index] = email
          break
        else:
          print("Invalid email, it must contain @ and a dot.")
      while True:
        birthday = input("Insert New Birthday:\n")
        if len(birthday) == 8 and birthday.isnumeric() == True:
          birthList[index] = birthday[:2]+"/"+birthday[2:4]+"/"+birthday[4:8]
          break
        elif birthday.isnumeric() == False:
          print("Invalid birthday, insert one with only numbers.")
        else:
          print("Invalid birthday, insert one with 8 numbers(MM/DD/YYYY).")
    else:
      print("Index out of bounds")
    choice = input("Enter to go back to the main menu\n")
  contactList()


def delete():
  cls()
  choice = "0A6FD2"
  while choice == "0A6FD2":
    index = int(input("Insert item index to delete:\n"))
    if index <= len(nameList):
      nameList.pop(index) 
      phoneList.pop(index) 
      emailList.pop(index) 
      birthList.pop(index)
    else:
      print("Index out of bounds")
    choice = input("Enter to go back to the main menu\n")
  contactList()

def listAll():
  cls()
  choice = "0A6FD2"
  while choice == "0A6FD2":
    length = len(nameList)-1
    count = 0
    while count <= length:
      print(f"Index:{count}\nName:{nameList[count]}\nPhone:{phoneList[count]}\nEmail:{emailList[count]}\nBirthday:{birthList[count]}\n\n")
      count = count + 1
    choice = input("Enter to go back to the main menu\n")
  contactList()

def contactList():
  cls()
  print("Contact list\n")
  print("1 - Register New Contact")
  print("2 - Search Contact")
  print("3 - Update Contact")
  print("4 - Delete Contact")
  print("5 - List All Contacts")
  print("0 - Exit\n")
  choice = input("Choose one:\n")
  if choice == "1":
    register()
  elif choice == "2":
    search()
  elif choice == "3":
    update()
  elif choice == "4":
    delete()
  elif choice == "5":
    listAll()
  else:
    print("Closing aplication...")
    raise Exception

end = False
while end == False:
  try:
    contactList()
  except Exception:
    break