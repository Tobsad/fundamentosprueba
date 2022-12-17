#Escriba un programa en el cual se ingrese un número
# y mientras ese número sea mayor que 10, se pedirá el número de nuevo.
num = int(input("Ingresa un numero:\n"))

while (num>10):
    num = int(input("Ingresa otro numero:\n"))
    
print("Saliste del bucle por digitar un numero menor o igual que 10 ")