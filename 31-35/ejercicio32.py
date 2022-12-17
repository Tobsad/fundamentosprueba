#Se debe realizar un programa que:
# 1 Pida por teclado un número entero positivo.
# 2 Pregunte al usuario si desea introducir o no otro número.
# 3 Repita los pasos 1o y 2o mientras que el usuario no responda n/N no.
# 4 Muestre por pantalla la suma de los números introducidos por el usuario.


#Ingresamos el primer numero
num1 = int(input("Ingresa un numero:\n"))

#Solicitamos si desea ingresar otro numero 
rpta=str(input("Desea ingresar otro numero? (s/n):\n")).upper()

#Creamos le asignamos la letra s o S como verdadero y la letra n o N como falso
S=True
N=False

#Creamos un acumulador que guardar la suma de los numeros ingresados:
aculumador=0
aculumador+=num1

#mientras que la respuesta sea s o S le seguiremos solicitando numeros al usuario hasta que digite n o N
while (rpta=='S'):
    num1 = int(input("Ingresa otro numero:\n"))
    rpta2=str(input("Desea ingresar otro numero? (s/n): ")).upper()
    rpta=rpta2
    aculumador+=num1
    
#imprimimos la suma de los numero
print("La suma de numeros ingresados es:",aculumador)