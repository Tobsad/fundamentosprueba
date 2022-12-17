#Problema: Dado un número entero N, determine si es negativo, cero o positivo

# leemos el número entero N
N = int(input("Ingrese un numero negativo,cero o positivo: \n"))

# usamos una selección múltiple para determinar si N es negativo, cero o positivo
if N < 0:
  print("negativo")
elif N == 0:
  print("cero")
else:
  print("positivo")