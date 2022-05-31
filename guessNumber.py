'''import random

def tryAgain(randomNumber):
  global tryNow
  tryNumber = int(input("Inserir Tentativa(entre 1 e 9): "))
  if(randomNumber == tryNumber):
    print(messagePrint[tryNow])
    restart()
  elif(randomNumber > tryNumber):
    print("DIGITE UM NÚMERO MAIOR")
    tryNow += 1
  else:
    print("DIGITE UM NÚMERO MENOR") 
    tryNow += 1




def restart():
  global tryNow
  answer = int(input("Digite 1 para continuar, qualquer outro botão vai terminar a aplicação: "))
  if(answer == 1):
    main()
  else:
    print("Fechando...")
    exit()




def main():
  randomNumber = random.randint(1,9)
  boo = True
  global tryNow 
  tryNow = 0
  
  while boo:
    if(tryNow > 1):
      boo = False
    else:
      tryAgain(randomNumber)
  
  tryNumber = int(input("Inserir Última Tentativa(entre 1 e 9): "))
  if(randomNumber == tryNumber):
    print(messagePrint[tryNow])
    restart()
  else:
    print(messagePrint[tryNow+1])
    restart()




messagePrint = ["VOCÊ TEVE MUITA SORTE","VOCÊ JOGA BEM, MAS AINDA CONTOU SORTE","VOCÊ É UM EXCELENTE ESTRATEGISTA","ANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE"]
main()'''



import random

def tryAgain(randomNumber):
  global tryNow
  global minRange
  global maxRange
  
  tryNumber = int(input(f"Inserir Tentativa(entre {minRange}  e {maxRange}): "))
  if(tryNumber >= minRange and tryNumber <= maxRange):
    if(randomNumber == tryNumber):
      print(messagePrint[tryNow-1],"\n")
      print(f"Palpite Necessários para acertar: {tryNow}")
      print(f"Pontuação: {110-(tryNow*10)}/100\n")
      restart()
    elif(randomNumber > tryNumber):
      print("DIGITE UM NÚMERO MAIOR\n")
      minRange = tryNumber
      tryNow += 1
    else:
      print("DIGITE UM NÚMERO MENOR\n") 
      maxRange = tryNumber
      tryNow += 1
  else:
    print("Perdeu por digitar uma jogada fora da margem\n")
    restart()




def restart():
  global tryNow
  answer = int(input("Digite 1 para continuar, qualquer outro botão vai terminar a aplicação: \n"))
  if(answer == 1):
    main()
  else:
    print("Fechando...")
    exit()




def main():
  randomNumber = random.randint(1,100)
  boo = True
  global tryNow
  global minRange
  global maxRange
  minRange = 1
  maxRange = 100
  tryNow = 1
  
  while boo:
    print(f"Tentativa {tryNow}")
    if(tryNow > 9):
      boo = False
    else:
      tryAgain(randomNumber)
  
  tryNumber = int(input(f"Inserir Tentativa(entre {minRange}  e {maxRange}):"))
  if(tryNumber >= minRange and tryNumber <= maxRange):
    if(randomNumber == tryNumber):
      print(messagePrint[tryNow-1],"\n")
      print(f"Palpite Necessários para acertar: {tryNow}")
      print(f"Pontuação: {110-(tryNow*10)}/100\n")
      restart()
  
    else:
      print(messagePrint[tryNow],"\n")
      restart()
  else:
    print("Perdeu por digitar uma jogada fora da margem\n")
    restart()




messagePrint = ["VOCÊ TEVE MUITA SORTE","VOCÊ TEVE MUITA SORTE","VOCÊ TEVE MUITA SORTE","VOCÊ JOGA BEM, MAS AINDA CONTOU COM A SORTE","VOCÊ JOGA BEM, MAS AINDA CONTOU COM A SORTE","VOCÊ JOGA BEM, MAS AINDA CONTOU COM A SORTE","VOCÊ JOGA BEM, MAS AINDA CONTOU COM A SORTE","VOCÊ É UM EXCELENTE ESTRATEGISTA","VOCÊ É UM EXCELENTE ESTRATEGISTA","VOCÊ É UM EXCELENTE ESTRATEGISTA","ANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE"]
main()