#Dado un número entero N, imprima el número invertido.

# leemos el número entero N
N = int(input("Inserte un numero:\n"))

# convertimos N a una cadena de caracteres y lo guardamos en la variable n_str
n_str = str(N)

# invertimos n_str y lo guardamos en la variable inverted_str
inverted_str = n_str[::-1]

# convertimos inverted_str a un número entero y lo guardamos en la variable inverted_num
inverted_num = int(inverted_str)

# imprimimos el número invertido
print("El numero invertido es:")
print(inverted_num)