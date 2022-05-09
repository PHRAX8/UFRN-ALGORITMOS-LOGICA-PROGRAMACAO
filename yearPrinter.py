from datetime import date
while True:
  try:
    ano = int(input("Ano de seu nascimento:"))
    mes = int(input("Mês de seu nascimento:"))
    dia = int(input("Dia de seu nascimento:"))
    nascimento = date(ano,mes,dia)
    break
  except ValueError:
    print("Erro, Data invalida, Insira os dados novamente:\n")
hoje = date.today()
if(hoje.month == mes and hoje.day >= dia or hoje.month > mes):  
  idade = hoje.year - ano
  print("Idade:",idade,"anos\nJá completou")
else:
  idade = hoje.year - (ano + 1)
  print("Idade:",idade,"anos\nNão completou ainda")