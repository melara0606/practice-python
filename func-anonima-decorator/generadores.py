# GENERADORES
# Primera Forma
lista = [1, 3, 5, 7, 9]
l2 = (n ** 2 for n in lista)

def doble_numero(numero):
  i = 1
  while i <= numero:
    n = i * 2
    yield n
    i += 1

for j in doble_numero(5):
  print(j)