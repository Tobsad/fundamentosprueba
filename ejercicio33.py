#Se pide escribir un programa que calcule la suma de los N primeros números pares. Es
#decir, si ingresamos el número 5 como valor de N, el algoritmo nos debe realizar la suma
#de los siguientes valores: 2+4+6+8+10.

# Pedimos al usuario que ingrese el valor de N
n = int(input("Ingrese el valor de N: "))

# Inicializamos la variable acumuladora en 0
suma = 0

# Recorremos los N primeros números pares
for i in range(1, n+1):
  # Si el número es par, lo sumamos a la variable acumuladora
  if i % 2 == 0:
    suma += i

# Mostramos el resultado
print("La suma de los N primeros números pares es:", suma)