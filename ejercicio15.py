#Construir un algoritmo que permita ingresar un número, si el número es mayor de 500, 
# se debe calcular y mostrar en pantalla el 20% de este.
numero=int(input("Digite un numero: \n"))

#Si el numero es mayor que 500 imprimira que este es mayor que 500 y junto al 20% del numero ingresado
porcentaje=0.2*numero

if (numero>500):
    print("El numero es mayor que 500 y su 20 por ciento es igual a ",porcentaje,".")
else:
    print("Su numero es inferior o igual a 500")
