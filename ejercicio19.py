#Escribir un programa que imprima por pantalla los números del 1 al 100, con una fila por cada 10 números.

#  Recorremos los números del 1 al 100
for i in range(1, 101):
  # Imprimimos el número
  print(i, end=" ")
  # Si el número es múltiplo de 10, hacemos un salto de línea
  if i % 10 == 0:
    print()