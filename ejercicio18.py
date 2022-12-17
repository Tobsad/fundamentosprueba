#Escribir un programa que lea una cantidad de números y calcule su promedio.

# Pedimos al usuario que ingrese la cantidad de números
cantidad = int(input("Ingrese la cantidad de números: "))

# Inicializamos una variable para almacenar la suma de los números
suma = 0

# Recorremos los números ingresados
for i in range(cantidad):
  # Pedimos al usuario que ingrese un número
  print("Ingrese el número #",i+1,":")
  num = float(input())
  # Sumamos el número a la variable suma
  suma += num

# Calculamos el promedio
promedio = suma / cantidad

# Mostramos el promedio por pantalla
print("El promedio es:", promedio)