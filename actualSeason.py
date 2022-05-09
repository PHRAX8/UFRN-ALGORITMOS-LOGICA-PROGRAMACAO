def hemisphereFunction(northSouth,season):
  if(northSouth == 1):
    print(seasons[season])
  else:
    print(seasons[season+2])
while(True):
  try:
    seasons = ["Primavera","Verão","Outono","Inverno","Primavera","Verão"]
    month30 = [4,6,9,11]
    month31 = [1,3,5,7,8,10,12]
    index = 0
    day = int(input("Inserir Dia:\n"))
    month = int(input("Inserir Mês(Numeral):\n"))
    year = int(input("Inserir Ano:\n"))
    hemisphere = int(input("Inserir Hemisfério(Norte = 1, Sul = 0):\n"))
    while(index < len(month30)):
      if(month == month30[index] and day > 30):
        raise Exception
      else:
        index+= 1
    index = 0
    while(index < len(month31)):
      if(month == month31[index] and day > 31):
        raise Exception
      else:
        index+= 1
    if (day < 1 and day > 31 or month < 1 and month > 12 or hemisphere < 0 and hemisphere > 1 or month == 2 and day > 28 and year % 4 != 0 or month == 2 and day > 29 and year % 4 == 0 and year % 100 != 0 and year % 400 == 0):
      raise Exception
    else:
      break
  except Exception:
    print("Erro - 1, Dados Incorretos\nInsira os dados novamente\n") 
  except NameError:
    print("Erro - 2, Dados Incorretos\nInsira os dados novamente\n") 
if(year % 4 != 0):
  if(month == 3 and day >= 22 or month == 4 or month == 5 or month == 6 and day <= 21):
    hemisphereFunction(hemisphere,0)
  elif(month == 6 and day >= 22 or month == 7 or month == 8 or month == 9 and day <= 21):
    hemisphereFunction(hemisphere,1)
  elif(month == 9 and day >= 22 or month == 10 or month == 11 or month == 12 and day <= 21):
    hemisphereFunction(hemisphere,2)
  else:
    hemisphereFunction(hemisphere,3)
else:
  if(month == 3 and day >= 21 or month == 4 or month == 5 or month == 6 and day <= 20):
    hemisphereFunction(hemisphere,0)
  elif(month == 6 and day >= 21 or month == 7 or month == 8 or month == 9 and day <= 20):
    hemisphereFunction(hemisphere,1)
  elif(month == 9 and day >= 21 or month == 10 or month == 11 or month == 12 and day <= 20):
    hemisphereFunction(hemisphere,2)
  else:
    hemisphereFunction(hemisphere,3)