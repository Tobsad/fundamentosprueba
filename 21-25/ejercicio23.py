#Escribe un programa que calcule la suma de todos los números divisibles por 
# 3 o 5 menores a un numero ingresado en python.

#solicitamos un numero que sera el limite sumar los numeros divisibles entre 3o 5 
print("Ingrese un limite:")
limite=int(input())

#un mensaje de espera
print("Imprimiendo los numeros divisibles de 3 o 5...")
#definimos un acumulador
sum = 0

#en este bucle se analizara los numero que son divisibles entre 3 o 5 y se sumaran en el acumulador que definimos antes.

for i in range(1, limite):
    #aca se realiza el analisis de los numeros     
    if i % 3 == 0 or i % 5 == 0:
      print(i)
      sum += i
#imprimira la suma de los numeros divisibles
print("La suma de los numeros divisibles entre 3 y 5 es:",sum)

