#Escribir un programa que imprima por pantalla los números del 1 al numero insertado

numero=int(input("Ingrese un numero:\n"))


print("Empezando a contar...")

if (numero==10):
    for i in range(1,numero+1):
        print(i)
        if (i==2):
            print("Freddy viene por ti!")
        elif (i==4):
            print("mejor cierra la puerta!")
        elif (i==6):
            print("coge tu crucifijo!")
        elif (i==8):
            print("mejor que te quedes despierto hasta tarde!")
        elif (i==10):
            print("¡nunca volverás a dormir!")
else:
    for i in range(1,numero+1):
        print(i)

    
