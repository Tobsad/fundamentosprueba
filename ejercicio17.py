#Escribir un programa que calcule la suma de los números pares del 1 al numero insertado

#Solicitamos el limite de la cadena de numeros:
limite=int(input("Ingrese un numero:\n"))

# Inicializamos una variable para almacenar la suma
suma = 0

# Recorremos los números del 1 al numero insertado
for i in range(1, limite+1):
  # Si el número es par, lo sumamos a la variable suma
  if i % 2 == 0:
    suma += i

# Mostramos la suma por pantalla
print(suma)