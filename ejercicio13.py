#Se pide ingresar una letra del alfabeto y mostrar si dicha letra es vocal o si es otro tipo de dato.
letra=str(input("Ingrese una letra del alfabeto:\n").upper()) 

#Se le agrego el .upper para que la letra ingresada se transforme en mayuscula 
# ahora pasara a analizar la letra si es un vocal sea minuscula o mayuscula imprimira es un vocal.
# de caso contrario dira que es una consonante. 

if (letra=="A")or(letra=="E")or(letra=="I")or(letra=="O")or(letra=="U"):
    print("Es una vocal")
else:
    print("Es una consonante,numero o caracter especial.")