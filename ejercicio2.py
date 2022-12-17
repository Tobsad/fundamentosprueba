#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas=int(input("Ingrese las horas trabajadas:\n"))

pagoPorHora=int(input("Ingrese el costo por hora trabajada: \n"))

total=horasTrabajadas*pagoPorHora

print("Su pago es de ",total, "soles, por sus",horasTrabajadas,"horas trabajas. Con la paga de ",pagoPorHora," soles por hora.")