pacientTemp = []
tempHour = [3,6,9,12,15,18,21,24]
aboveTemp = []
count = 0
media = 0
pacientTempAboveCount = 0


while count <= 7:
  insert = float(input(f"Horário: {tempHour[count]}:00\ninserir temperatura do paciente:\n").replace(',','.'))
  pacientTemp.append(insert)
  media = media + pacientTemp[count]
  count = count + 1


media = media/count


while count >= 0:
  if pacientTemp[count-1] > media:
    pacientTempAboveCount = pacientTempAboveCount + 1
    aboveTemp.append(tempHour[count-1])
  else:
    pacientTempAboveCount = pacientTempAboveCount
  count = count - 1


count = 0
aboveTemp.reverse()
print(f"\nMédia de Temperatura: {media:.1f} Graus\nQuantas vezes a temperatura ficou acima da média:\n{pacientTempAboveCount} vezes\nAcima da média nos seguintes horários:")



while count <= pacientTempAboveCount-1:
  print(f"{aboveTemp[count]}:00")
  count = count + 1