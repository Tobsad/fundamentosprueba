#Hacer un algoritmo para calcular la media de los números pares e impares, sólo se ingresará diez números.

#Para calcular la media de los números pares e impares de un conjunto de diez números, podemos utilizar dos variables acumuladoras, una para sumar los números pares y otra para sumar los números impares. También podemos utilizar dos contadores, uno para llevar el número de números pares y otro para el número de números impares.

# Inicializamos las variables acumuladoras y los contadores
suma_pares = 0
suma_impares = 0
contador_pares = 0
contador_impares = 0  
# Recorremos los 10 números
for i in range(10):
  # Pediremos al usuario que ingrese un número
  num = int(input("Ingrese un número: "))

  # Comprobamos si el número es par o impar
  if num % 2 == 0:
    suma_pares += num
    contador_pares += 1
  else:
    suma_impares += num
    contador_impares += 1

# Calculamos las medias
media_pares = suma_pares / contador_pares
media_impares = suma_impares / contador_impares

# Mostramos los resultados
print("La media de los números pares es:", media_pares)
print("La media de los números impares es:", media_impares)