#Problema: Dado un número entero N, determine si es divisible por 3 y por 5.
# leemos el número entero N
N = int(input("Ingrese un numero entero:\n"))

# usamos una selección doble para determinar si N es divisible tanto por 3 como por 5
if N % 3 == 0 and N % 5 == 0 and N!=0:
  print("divisible")
else:
  print("no divisible")
