import random
import matplotlib.pyplot as plt

tempCount = 0
hourDay = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
tempHour = [0]*24
averageTemp = 0
while tempCount < 24:
  if tempCount <= 6:
    tempHour[tempCount] = random.randint(21, 25)
  elif tempCount <= 12 and tempCount > 6:
    tempHour[tempCount] = random.randint(31, 35)
  elif tempCount <= 18 and tempCount > 12:
    tempHour[tempCount] = random.randint(30, 34)
  elif tempCount <= 24 and tempCount > 18:
    tempHour[tempCount] = random.randint(20, 24)
  averageTemp += tempHour[tempCount]
  tempCount += 1

averageTemp = averageTemp/24
plt.plot(hourDay,tempHour, 'bo')
plt.plot(hourDay,tempHour)
plt.ylabel('Temperatura(°C)')
plt.xlabel(f"{averageTemp:.1f} °C em Média")
plt.show()