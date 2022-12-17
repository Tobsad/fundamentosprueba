# Solicitamos al usuario que ingrese una lista de números
lista = input("Ingresa una lista de números separados por espacios: ")

# Convertimos la cadena de texto ingresada por el usuario en una lista de números
lista = [int(x) for x in lista.split()]

# Imprimimos la lista de números ingresada por el usuario
print("La lista de números que ingresaste es: ", lista)
