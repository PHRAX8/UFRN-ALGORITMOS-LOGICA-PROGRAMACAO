import os
import json
from pathlib import Path

#função loadFile: segmento destinado a carregar o conteudo do arquivo parkingAreas.json no dicionário parkingAreas, caso não exista o dicionário permanece em branco.

def loadFile():
  path = Path('parkingAreas.json')
  parkingAreas = dict()
  if path.is_file():
    with open("parkingAreas.json","r") as infile:
      parkingAreas = json.load(infile)
  else:
    print()
  return parkingAreas

#Função cls: para fechar o programa usando o import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Função saveFile: utilizada para salvar o estado atual do dicionário no arquivo parkingAreas.json, caso o arquivo não exista ele o cria quando inicializado pela primeira vez

def saveFile(parkingAreas):
  with open('parkingAreas.json', 'w') as openfile:
    json.dump(parkingAreas, openfile)
  parkingLot()

#Função insertInfo: utilizada para registrar as informações da vaga de estacionamento(usada nas funções registerCar e updateCar), possui restrição na quantidade de caracteres, insere letras maiusculas em nomes próprios ou tornar todas as letras em caixa alta em determinados segmentos(alguns exigem certos padrões como restrição de alguns caracteres ou checagem se a string possui apenas números)

def insertInfo(parkingAreas,info):
  
  parkingAreas[info]['carBrand'] = str(input("New Car Brand:\n")[:50]).title()
  
  parkingAreas[info]['carModel'] = str(input("New Car Model:\n")[:30]).title()
  while True:
    carYear = str(input("New Car Year:\n")[:4])
    if carYear.isalnum():
      parkingAreas[info]['carYear'] = carYear
      break
    else:
      print("Invalid Year")
    
  parkingAreas[info]['carPlate'] = str(input("New Car Plate:\n")[:7]).upper()
  
  while True:
    VIN = str(input("New Car VIN:\n")[:17]).upper()
    if "I" in VIN or "O" in VIN or "Q" in VIN:
      print("Wrong VIN Inserted")
    else:
      parkingAreas[info]['carVIN'] = VIN
      break
  
  parkingAreas[info]['driverName'] = str(input("New Driver Name:\n")[:120]).title()
  
  while True:
    phone = str(input("New Phone Number:\n")[:9])
    if len(phone) == 9 and phone.isnumeric() == True:
      parkingAreas[info]['phoneNumber'] = phone[:5]+"-"+phone[5:9]
      break
    elif phone.isnumeric() == False:
      print("Invalid Phone Number, insert one with only numbers.")
    else:
      print("Invalid Phone Number, insert one with 9 numbers.")
    
#função registerCar: cria uma nova entrada no dicionário, chamando as funções insertInfo e saveFile para completar o procedimento
  
def registerCar(parkingAreas):
  register = str(input("Insert the Choosen Area\n"))
  if register.isnumeric() == True:
    parkingAreas[register] = {"carBrand": "","carModel": "","carYear": "","carPlate": "","carVIN": "","driverName": "","phoneNumber": ""}
    insertInfo(parkingAreas,register)
    saveFile(parkingAreas)
  else:
    print("Insert only numbers!")
    exit = input("enter to go back to the main menu")
  parkingLot()

#função searchCar: destinado a procurar a vaga de estacionamento com o número informado, caso ocupada, mostra o conteúdo, caso desocupada, informa que está vázio

def searchCar(parkingAreas):
  search = str(input(f"There's {len(parkingAreas)} parking areas occupied\ninsert an area number...\n"))
  if search.isnumeric() == True:
    if search in parkingAreas:
      print(json.dumps(parkingAreas[search], indent=4))
    elif not search in parkingAreas:
      print("This parking area is empty")
    exit = input("enter to go back to the main menu")
    parkingLot()
  else:
    print("Insert only numbers!")
    exit = input("enter to go back to the main menu")
  parkingLot()

#função updateCar: tem com objetivo atualizar todos os dados de uma vaga ocupada

def updateCar(parkingAreas):
  while True:
    update = str(input("Insert the Area Number to Update it\n"))
    if update.isnumeric() == True:
      if update in parkingAreas:
        insertInfo(parkingAreas,update)
        saveFile(parkingAreas)
      elif not update in parkingAreas:
        print("This parking area is empty")
        exit = input("enter to go back to the main menu")
        break
    else:
      print("Insert only numbers!")
      exit = input("enter to go back to the main menu")
      break
  parkingLot()

#função deleteCar: desocupa uma vaga no estacionamento

def deleteCar(parkingAreas):
  while True:
    delete = str(input("Insert the Area Number to Free it\n"))
    if delete.isnumeric() == True:
      if delete in parkingAreas:
        del parkingAreas[delete]
        saveFile(parkingAreas)
      elif not delete in parkingAreas:
        print("This parking area is empty")
        exit = input("enter to go back to the main menu")
        break
    else:
      print("Insert only numbers!")
      exit = input("enter to go back to the main menu")
      break
  parkingLot()

#função printParkingLot: mostra as vagas ocupadas acima do menu de opções

def printParkingLot(parkingAreas):
  PA = []
  if len(parkingAreas) == 0:
    print("All Parking Areas are empty")
  for i in parkingAreas:
    if parkingAreas[i] != None:
      PA.append(i)
  PA.sort()
  print(f"{PA} => Occupied Lots\n")
  return PA

#função listAllCar: mostra todas as vagas ocupadas do estacionamento e suas informações registradas

def listAllCar(parkingAreas,PA):
  try:
    for i in PA:
      if i in parkingAreas:
        print(f"{i}\n",json.dumps(parkingAreas[i], indent=4,))
        print("\n")
    exit = input("enter to go back to the main menu")
    parkingLot()
  except Exception:
    print("Parking Lot is Empty")
    exit = input("enter to go back to the main menu")
    parkingLot()

#função changeArea: utilizada para trocar informações de uma area ocupada, denominada old, e uma area vaga, denominada new.

def changeArea(parkingAreas):
  while True:
    old = str(input("Insert the Old Area Number\n"))
    new = str(input("Insert the New Area Number\n"))
    if old.isnumeric() == True and new.isnumeric() == True:
      if old in parkingAreas and not new in parkingAreas:
        parkingAreas[new] = parkingAreas[old]
        del parkingAreas[old]
        saveFile(parkingAreas)
        break
      elif not old in parkingAreas or new in parkingAreas:
        print("The Old parking area is empty or the New area is Occupied")
        exit = input("enter to go back to the main menu")
        break
    else:
      print("Insert only numbers!")
      exit = input("enter to go back to the main menu")
      break
  parkingLot()

#função parkingLot: função principal que mostra todas as opções disponiveis no programa

def parkingLot():
  parkingAreas = loadFile()
  PA = printParkingLot(parkingAreas)
  cls()
  printParkingLot(parkingAreas)
  print("\nParking Lot\n")
  print("1 - Fill Available Area")
  print("2 - Search Parking Areas")
  print("3 - Update an Area")
  print("4 - Free an Area")
  print("5 - List All Areas")
  print("6 - Change an Old Area to a New Empty Area")
  print("Any Other Input - Exit/Credits\n")
  choice = input("Choose one:\n")
  if choice == "1":
    registerCar(parkingAreas)
  elif choice == "2":
    searchCar(parkingAreas)
  elif choice == "3":
    updateCar(parkingAreas)
  elif choice == "4":
    deleteCar(parkingAreas)
  elif choice == "5":
    listAllCar(parkingAreas,PA)
  elif choice == "6":
    changeArea(parkingAreas)
  else:
    print("Devenloped by:\n  Professor: Flavius da Luz e Gorgonio\n  Student: Pedro Henrique Ribeiro Alves\n  ID: 20220034818")
    print("Closing aplication...")
    raise Exception

#segmento de código utilizado para iniciar e captar erros no programa(quando um erro é captado o programa se encerra)

end = False
while end == False:
  try:
    parkingLot()
  except Exception:
    print("Programa Encerrado...")
    break