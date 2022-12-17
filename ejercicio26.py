#Escriba un programa que valide si una nota está entre 0 y 10, 
# sino está entre 0 y 10 la nota se pedirá de nuevo hasta que la nota sea correcta.

#Pedimos la nota del usuario o estudiante
nota=nota=int(input("Ingrese una nota: "))
print("******************")

#mientras que la nota no sea  encuentre entre el 0 al 20
#se imprimira un mensaje de error y solicitara ingresar nuevamente una nota correcta
while (nota>20) or (nota<0) :

    print("ERROR!!...Por favor, ingrese una nota corecta")
    nota=int(input("Nota: "))

#al insertar una nota correcta, saldra del bucle 
print("Su nota es correcta. Usted tiene ", nota," como nota.")