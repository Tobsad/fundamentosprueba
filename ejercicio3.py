#Pedir al usuario que ingrese el valor del radio de una circunferencia. 
#Y calcular y mostrar por pantalla el área y perímetro.
import math

print("**************************************")
print("Hallando el perimetro area y perimetro")
print("**************************************")

radio=float(input("Ingrese el radio \n"))

p=math.pi
area=p*(radio**2)
perimetro=2*radio*p

print("El area con radio:",radio,"es: ",area)
print("El perimetro con radio",radio,"es: ",perimetro)