#Realiza una tabla de multiplicar del numero que se ingrese:

#Solicitamos de que numero desea saber su respectiva tabla de multiplicar 
print("La tabla de que numero deseas saber?")
num=int(input())

#Le preguntamos hasta que multiplo desea observar
print("Hasta que multiplo deseas aprender?")
multiplicar=int(input())

#Imprimos el titulo de la tabla de que numero esta observando 
print("Mostrando tabla del numero",num,"hasta ",multiplicar)

#Este bucle imprimira la tabla
for i in range(1, multiplicar+1):
    print(f"{num} x {i} = {num * i}")