#Escriba un programa que solicite dos números enteros (mínimo y máximo). 
#A continuación, se debe pedir al usuario que ingrese números enteros situados entre el máximo y mínimo.
#Si el #2 es menor que el #1 se le pedira que registre otros 2 numeros hasta que se cumpla lo requerido.
#Si el usuario sigue en el bucle imprime "Recuerda que aveces menos es mas"
#Si sale del bucle imprimir , "Encontraste la solucion, no lo comentes a nadie."
#Si los 2 numeros son iguales escapara con suerte.

#ingresamos 2 numeros
num1 = int(input("Ingresa el #1 numero:\n"))
num2 = int(input("Ingresa el #2 numero:\n"))

#mientras el primer nuemro sea mayor que el segundo se seguira solicitando 2 numeros 
# Hasta que num1<= num2 
while (num1>num2):
    print("Recuerda que aveces menos es mas")
    num1 = int(input("Ingresa el #1 numero denuevo:\n"))
    num2 = int(input("Ingresa el #2 numero denuevo:\n"))
#si deja de cumplirse la condicion saldra del bucle pero si los 2 numeros son iguales escapara apenas
#sino se le imprimira encontraste la solucion
if (num1==num2):
    print("Ambos numeros son iguales, escapaste con suerte")
else:        
    print("Encontraste la solucion: gracias por darte cuenta.")
