#Programar un juego donde la computadora elige un número al azar entre 1 y 10, y a
#continuación el jugador tiene que adivinarlo. La estructura del programa es la siguiente:
#1o) El programa elige al azar un número n entre 1 y 10.
#2o) El usuario ingresa un número x.
#3o) Si x no es el número exacto, el programa indica si n es más grande o más pequeño
#que el número ingresado.
#4o) Repetimos desde 2) hasta que x sea igual a n.
#El programa tiene que imprimir los mensajes adecuados para informarle al usuario qué
#hacer y qué pasó hasta que adivine el número.


import random

# Elegimos un número al azar entre 1 y 10
n = random.randint(1, 10)

# Inicializamos la variable x en 0
x = 0

# Repetimos el bucle hasta que x sea igual a n
while x != n:
  # Pedimos al usuario que ingrese un número
  x = int(input("Ingrese un número entre 1 y 10: "))

  # Comprobamos si el número es correcto
  if x == n:
    print("¡Felicidades, has adivinado el número!")
  elif x < n:
    print("El número que buscas es más grande")
  else:
    print("El número que buscas es más pequeño")