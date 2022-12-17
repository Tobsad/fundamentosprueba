#Escribir un programa que lea dos números enteros y muestre por pantalla el mayor de ellos.
#Ingresamos el primer numero
num1 = float(input("Ingrese un numero negativo,cero o positivo: \n"))
#Ingresamos el segundo numero
num2 = float(input("Ingrese otro numero negativo,cero o positivo: \n"))
#La secuencia analizara los numeros y mostrara dependiendo del caso
if (num1>num2):
    print("El mayor numero es: ",num1)
if (num2>num1):
    print("El mayor numero es: ",num2)
else:
    print("Ambos numeros son iguales")
