#Escriba un programa en el cual se ingrese un valor límite positivo, y a continuación solicite números al usuario
# hasta que la suma de los números introducidos supere el límite inicial.
#Solicitamos el limite 
limite = int(input("Ingresa un valor límite positivo: "))
#Declarammos un variable que guardara las suma de los numeros escritos
suma = 0
#Se invoca el bucle para que se vayan sumando los numeros a medida que no pase el limite , de pasar el limite 
#Terminara el bucle
while suma < limite:
    numeros = int(input("Ingresa un número: "))
    suma += numeros
    print("vas sumando: ",suma)
#Se imprimira la suma de los numeroes y el limite que se dio
print(f"La suma de los números introducidos es {suma}, lo cual supera el límite de {limite}.")
