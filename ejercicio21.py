#Escribir un programa que calcule el factorial de un número.

# Pedimos al usuario que ingrese un número
num = int(input("Ingrese un número: "))

# Inicializamos un acumulador para almacenar el factorial
factorial = 1

# Recorremos los números del 1 al número ingresado
for i in range(1, num + 1):
  # Multipilcamos el acumulador por el número actual
  factorial *= i

# Mostramos el factorial por pantalla
print("El factorial es:", factorial)