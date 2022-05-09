while True:
    try:
      height = float(input("Insira a Altura da Queda: ").replace(',','.'))
      gravity = float(input("Insira a Gravidade Atuante: ").replace(',','.'))
      if (gravity == 0):
        raise ValueError
      else:
        break
    except ValueError:
      print("Erro, Insira os dados novamente\n")
timer = float(height/gravity)
print(f'Tempo Total: {timer: .2f}',"segundos")

'''speed = 0.0
timer = 0
while(height > 0):
  height -= gravity
  if(height < 0):
    height = 0
  speed += gravity
  timer += 1
  print("Tempo Atual: ", timer,"s")
  print(f'Altura Atual:  {height: .2f}',"metros")
  print(f'Velocidade Atual: {speed: .2f}',"m/s\n")
speed = 0.0
print("Velocidade Atual: ", speed,"m/s")
print("Tempo Total: ", timer,"segundos")'''