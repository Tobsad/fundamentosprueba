#Escribe un programa que lea una lista de palabras del usuario y luego imprima cada palabra junto con su longitud.

#Solicitar palabras separadas por el espaciado
words = input("Ingresa una lista de palabras separadas por espacios:\n ").split()

#dejamos un espaciado para que no se vea muy estrecho
print()

#este bucle imprimira la palabra ingresada mas la cantidad de letras que lleva la respectiva palabras
for word in words:
    print(f"::{word} tiene {len(word)} letras")