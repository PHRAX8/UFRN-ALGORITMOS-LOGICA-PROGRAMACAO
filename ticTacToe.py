import os
import random

#clear
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def ticTacToePrint():
  cls()
  print("Turno: ",turns)
  print("Tabuleiro\n")
  print("Colunas")
  for i in range(3):
    for j in range(3):
      print(ticTacToe[i][j], end=' ')
      if i == 1 and j == 2:
        print(" Linhas", end=' ')
    print()



#Player
def player():
  global playerType
  global indexPlayer
  
  while True:
    try:
      print(f"\nVez do Jogador {playerType[indexPlayer]}")
      i = int(input("Informe a linha: "))
      j = int(input("Informe a coluna: "))
      if i == 0 or j == 0:
        raise IndexError 
      elif ticTacToe[i-1][j-1] == '_':
        ticTacToe[i-1][j-1] = playerType[indexPlayer]
        return ticTacToePrint()
      else:
        raise IndexError 
    except IndexError:
      print("Digite uma posição válida")



#Enemy
def enemy():
  global playerType
  global turns
  i = 0
  j = 0
  
  
  print(f"\nVez do Inimigo {playerType[1]}")
  if turns >= 0:
    if turns == 4: 
      i = random.randint(0,2)
      j = random.randint(0,2)
      if ticTacToe[1][1] == playerType[1] and ticTacToe[0][0] == playerType[0] and ticTacToe[2][2] == playerType[0] and (i == 2 and j == 0) or (i == 0 and j == 2):
        ticTacToe[1][0] = playerType[1]
        return ticTacToePrint()
      elif ticTacToe[1][1] == playerType[1] and ticTacToe[0][2] == playerType[0] and ticTacToe[2][0] == playerType[0] and (i == 2 and j == 2) or (i == 0 and j == 0):
        ticTacToe[0][1] = playerType[1]
        return ticTacToePrint()
          
    for i in range(3):
      if (ticTacToe[i][0] == ticTacToe[i][1]) and (ticTacToe[i][1] == playerType[1] and ticTacToe[i][2] == '_'):
        ticTacToe[i][2] = playerType[1]
        return ticTacToePrint() 
      elif (ticTacToe[i][1] == ticTacToe[i][2]) and (ticTacToe[i][2] == playerType[1] and ticTacToe[i][0] == '_'):
        ticTacToe[i][0] = playerType[1]
        return ticTacToePrint()
      elif (ticTacToe[i][2] == ticTacToe[i][0]) and (ticTacToe[i][0] == playerType[1] and ticTacToe[i][1] == '_'):
        ticTacToe[i][1] = playerType[1]
        return ticTacToePrint()
      elif (ticTacToe[0][i] == ticTacToe[1][i]) and (ticTacToe[1][i] == playerType[1] and ticTacToe[2][i] == '_'):
        ticTacToe[2][i] = playerType[1]
        return ticTacToePrint()
      elif (ticTacToe[1][i] == ticTacToe[2][i]) and (ticTacToe[2][i] == playerType[1] and ticTacToe[0][i] == '_'):
        ticTacToe[0][i] = playerType[1]
        return ticTacToePrint()
      elif (ticTacToe[2][i] == ticTacToe[0][i]) and (ticTacToe[0][i] == playerType[1] and ticTacToe[1][i] == '_'):
        ticTacToe[1][i] = playerType[1]
        return ticTacToePrint()

      elif i == 2:
        if (ticTacToe[0][0] == ticTacToe[1][1]) and (ticTacToe[1][1] == playerType[1] and ticTacToe[2][2] == '_'):
          ticTacToe[2][2] = playerType[1]
          return ticTacToePrint()
        elif (ticTacToe[1][1] == ticTacToe[2][2]) and (ticTacToe[2][2] == playerType[1] and ticTacToe[0][0] == '_'):
          ticTacToe[0][0] = playerType[1]
          return ticTacToePrint()
        elif (ticTacToe[2][2] == ticTacToe[0][0]) and (ticTacToe[0][0] == playerType[1] and ticTacToe[1][1] == '_'):
          ticTacToe[1][1] = playerType[1]
          return ticTacToePrint()
        elif (ticTacToe[0][2] == ticTacToe[1][1])  and (ticTacToe[1][1] == playerType[1] and ticTacToe[2][0] == '_'):
          ticTacToe[2][0] = playerType[1]  
          return ticTacToePrint()
        elif (ticTacToe[1][1] == ticTacToe[2][0])  and (ticTacToe[2][0] == playerType[1] and ticTacToe[0][2] == '_'):
          ticTacToe[0][2] = playerType[1]
          return ticTacToePrint()
        elif (ticTacToe[2][0] == ticTacToe[0][2])  and (ticTacToe[0][2] == playerType[1] and ticTacToe[1][1] == '_'):
          ticTacToe[1][1] = playerType[1]     
          return ticTacToePrint()
      
    for i in range(3):
      if (ticTacToe[i][0] == ticTacToe[i][1]) and (ticTacToe[i][1] == playerType[0] and ticTacToe[i][2] == '_'):
        ticTacToe[i][2] = playerType[1]  
        return ticTacToePrint()
      elif (ticTacToe[i][1] == ticTacToe[i][2]) and (ticTacToe[i][2] == playerType[0] and ticTacToe[i][0] == '_'):
        ticTacToe[i][0] = playerType[1]     
        return ticTacToePrint()
      elif (ticTacToe[i][2] == ticTacToe[i][0]) and (ticTacToe[i][0] == playerType[0] and ticTacToe[i][1] == '_'):
        ticTacToe[i][1] = playerType[1]
        return ticTacToePrint()
      elif (ticTacToe[0][i] == ticTacToe[1][i]) and (ticTacToe[1][i] == playerType[0] and ticTacToe[2][i] == '_'):
        ticTacToe[2][i] = playerType[1]    
        return ticTacToePrint()
      elif (ticTacToe[1][i] == ticTacToe[2][i]) and (ticTacToe[2][i] == playerType[0] and ticTacToe[0][i] == '_'):
        ticTacToe[0][i] = playerType[1]
        return ticTacToePrint()
      elif (ticTacToe[2][i] == ticTacToe[0][i]) and (ticTacToe[0][i] == playerType[0] and ticTacToe[1][i] == '_'):
        ticTacToe[1][i] = playerType[1]  
        return ticTacToePrint()

      elif i == 2:
        if (ticTacToe[0][0] == ticTacToe[1][1]) and (ticTacToe[1][1] == playerType[0] and ticTacToe[2][2] == '_'):
          ticTacToe[2][2] = playerType[1]    
          return ticTacToePrint()
        elif (ticTacToe[1][1] == ticTacToe[2][2]) and (ticTacToe[2][2] == playerType[0] and ticTacToe[0][0] == '_'):
          ticTacToe[0][0] = playerType[1]    
          return ticTacToePrint()
        elif (ticTacToe[2][2] == ticTacToe[0][0]) and (ticTacToe[0][0] == playerType[0] and ticTacToe[1][1] == '_'):
          ticTacToe[1][1] = playerType[1] 
          return ticTacToePrint()
        elif (ticTacToe[0][2] == ticTacToe[1][1])  and (ticTacToe[1][1] == playerType[0] and ticTacToe[2][0] == '_'):
          ticTacToe[2][0] = playerType[1]       
          return ticTacToePrint()
        elif (ticTacToe[1][1] == ticTacToe[2][0])  and (ticTacToe[2][0] == playerType[0] and ticTacToe[0][2] == '_'):
          ticTacToe[0][2] = playerType[1]
          return ticTacToePrint()
        elif (ticTacToe[2][0] == ticTacToe[0][2])  and (ticTacToe[0][2] == playerType[0] and ticTacToe[1][1] == '_'):
          ticTacToe[1][1] = playerType[1]
          return ticTacToePrint()
      
    while True:
      i = random.randint(0,2)
      j = random.randint(0,2)
      
      if ticTacToe[1][1] == '_' and ticTacToe[1][1] != (playerType[0] or playerType[1]):
        ticTacToe[1][1] = playerType[1]
        return ticTacToePrint()
     
      elif turns == 3:  
        if ticTacToe[1][1] == playerType[1] and ticTacToe[0][0] == playerType[0] and (i == 2 and j == 2):
          ticTacToe[i][j-1] = playerType[1]
          return ticTacToePrint()
        elif ticTacToe[1][1] == playerType[1] and ticTacToe[2][2] == playerType[0] and (i == 0 and j == 0):
          ticTacToe[i][j+1] = playerType[1]
          return ticTacToePrint()
        elif ticTacToe[1][1] == playerType[1] and ticTacToe[0][2] == playerType[0] and (i == 2 and j == 0):
          ticTacToe[i-1][j] = playerType[1]
          return ticTacToePrint()
        elif ticTacToe[1][1] == playerType[1] and ticTacToe[2][0] == playerType[0] and (i == 0 and j == 2):
          ticTacToe[i+1][j] = playerType[1]
          return ticTacToePrint()

      
      elif ticTacToe[i][j] == '_' and ticTacToe[i][j] != (playerType[0] or playerType[1]):
        ticTacToe[i][j] = playerType[1]
        return ticTacToePrint()
      else:
        print()



#Win Condition
def winCondition():
  print()
  global turns
  global end
  turns = turns + 1
  if turns >= 5:
    for i in range(3):
      if (ticTacToe[i][0] == ticTacToe[i][1]) and (ticTacToe[i][1] == ticTacToe[i][2]) and (ticTacToe[i][2] != '_'):
        end = True
        print(f"Jogador {ticTacToe[i][2]} Ganhou!")
        raise Exception
        
      elif (ticTacToe[0][i] == ticTacToe[1][i]) and (ticTacToe[1][i] == ticTacToe[2][i]) and (ticTacToe[2][i] != '_'):
        end = True
        print(f"Jogador {ticTacToe[2][i]} Ganhou!")
        raise Exception

    if (ticTacToe[0][0] == ticTacToe[1][1]) and (ticTacToe[1][1] == ticTacToe[2][2]) and (ticTacToe[2][2] != '_'):
      end = True
      print(f"Jogador {ticTacToe[2][2]} Ganhou!")
      raise Exception
      
    elif (ticTacToe[0][2] == ticTacToe[1][1]) and (ticTacToe[1][1] == ticTacToe[2][0]) and (ticTacToe[2][0] != '_'):
      end = True
      print(f"Jogador {ticTacToe[2][0]} Ganhou!")
      raise Exception
      
    elif ticTacToe[0][0] != '_' and ticTacToe[0][1] != '_' and ticTacToe[0][2] != '_' and ticTacToe[1][0] != '_' and ticTacToe[1][1] != '_' and ticTacToe[1][2] != '_' and ticTacToe[2][0] != '_' and ticTacToe[2][1] != '_' and ticTacToe[2][2] != '_':
      end = True
      print("Empate")
      raise Exception

     

#Game Setup 
ticTacToe = [
 ['_', '_', '_'],
 ['_', '_', '_'],
 ['_', '_', '_']
 ]
global turns
global end
global playerType
global indexPlayer
indexPlayer = 0
turns = 1
end = False
playerType = ['X','0']
orderChoice = input("Insira:\n0 -> Computador Começa\n1 -> Jogador Começa\n")
#qualquer digito serve para o jogador começar exceto o 0
ticTacToePrint()

while end == False:
  try:
    indexPlayer = 0
    if orderChoice == '0':
      enemy()
      winCondition()
      player()
      winCondition()
    else:
      player()
      winCondition()
      enemy()
      winCondition()
  except Exception:
    break