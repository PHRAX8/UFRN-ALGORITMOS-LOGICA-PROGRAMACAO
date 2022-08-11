lista = [18,11,84,74,12]
print('1',lista)
print('2',lista)
tam = len(lista)
print('3',lista)
for i in range(1,tam):
  print('4',lista)
  chave = lista[i] 
  print('5',lista)
  k = i
  print('6',lista)
  while (k > 0) and (chave < lista[k-1]):
    print('7',lista)
    lista[k] = lista[k-1]
    print('8',lista)
    k -= 1
    print('9',lista)
  lista[k] = chave
  print('10',lista)

print("\n")

lista = [18,11,84,74,12]
print('Lista Inicial:',lista)
tam = len(lista)
for i in range(1,tam):
  chave = lista[i]
  k = i
  while (k > 0) and (chave < lista[k-1]):
    lista[k] = lista[k-1]
    k -= 1
  lista[k] = chave
  print('i=%d, k=%d, Lista: '%(i,k),lista)
print('Lista Final:',lista)
