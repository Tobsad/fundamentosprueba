#Diseñe un algoritmo que lea un número y determine si es o no capicúa.

# leemos el número 
numero= int(input("Inserte un numero:\n"))

# convertimos N a una cadena de caracteres y lo guardamos en la variable texto
texto= str(numero)

# invertimos n_str y lo guardamos en la variable inverted_str
numeroinverso= texto[::-1]

# convertimos inverted_str a un número entero y lo guardamos en la variable inverted_num
numeroinverso = int(numeroinverso)

#Si el numero invertido es igual al numero original imprimieros que es capicua, de no ser asi diremos que no lo es 
if (numero==numeroinverso):
    print("El numero ",numero, " es capicua")
else:
    print("El numero ",numero," no es capicua")
