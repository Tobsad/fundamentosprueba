#Escriba un programa que solicite al usuario números decimales 
#mientras que el usuario escriba números mayores al primero que se ingresó.
#Por ejemplo: si el usuario ingresa como primer número un 3.1, y luego ingresa un 4,
#el programa debe solicitar nuevamente un número.
#el programa continuará solicitando valores sucesivamente mientras los valores ingresados sean mayores que 3.1,
#caso contrario, el programa finaliza.

#solicitamos 2 numeros decimales al usuario
print("Ingrese 2 numeros decimales")
num1 = float(input("Ingresa el #1 numero:\n"))
num2 = float(input("Ingresa el #2 numero:\n"))

#como dice el ejercicio mientras el primer numero sea menor que el segundo 
#seguira pidiendo otro numero, asi hasta que el segundo numero sea menor que el primero
while (num1<num2):
    num2 = float(input("Ingresa otro numero:\n"))
print("Salio del bucle, ingreso un numero menor al primero.")
    