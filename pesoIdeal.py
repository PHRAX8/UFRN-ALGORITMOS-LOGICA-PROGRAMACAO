while True:
  while True:
    try:
      peso = float(input("Informe o Peso em Kilogramas:\n").replace(',','.'))
      altura = float(input("Informe a Altura em Metros:\n").replace(',','.'))
      if (altura == 0):
        raise ValueError
      else:
        break
    except ValueError:
      print("Erro, Insira os dados novamente\n") 
  imc =  peso/(altura ** 2)
  #print(imc)
  print(f'IMC:  {imc:.2f}')
  if (imc > 0 and imc <= 18.5 ):
    print("Abaixo do Peso")
    break
  elif(imc > 18.5 and imc <= 24.9):
    print("Saudável")
    break
  elif(imc > 24.9 and imc <= 29.9):
    print("Sobrepeso")
    break
  elif(imc > 29.9 and imc <= 34.9):
    print("Obesidade Grau 1(Leve)")
    break
  elif(imc > 34.9 and imc <= 39.9):
    print("Obesidade Grau 2(Severa)")
    break
  elif(imc >= 40):
    print("Obesidade Grau 3(Mórbida)")
    break
  else:
    print("Erro, Insira os dados novamente\n")