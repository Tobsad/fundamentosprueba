# Pedimos al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Inicializamos una variable para almacenar la palabra modificada
palabra_modificada = ""

# Recorremos cada carácter de la palabra
for c in palabra:
  # Si el carácter es una vocal, lo reemplazamos por la consonante "t"
  if c in "aeiouAEIOU":
    palabra_modificada += "t"
  # Si el carácter es una consonante, lo reemplazamos por la letra "e"
  else:
    palabra_modificada += "e"

# Mostramos la palabra modificada por pantalla
print("Palabra modificada:", palabra_modificada)