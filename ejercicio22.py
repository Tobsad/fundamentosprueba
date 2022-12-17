# Inicializamos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializamos un acumulador para almacenar la suma de los números pares
suma = 0

# Recorremos la lista de números
for num in numeros:
  # Si el número es par, lo sumamos al acumulador
  if num % 2 == 0:
    suma += num

# Mostramos la suma por pantalla
print("La suma de los números pares es:", suma)