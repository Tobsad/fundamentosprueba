#Dependiendo el numero que digite informara que dia es:
#Asociando si 1 con lunes , 2 con martes, 3 con miercoles, 4 con jueves,5 con viernes, 6 con sabado y 7 con domingo.
#Si es un numero diferente imprimir ERROR.
#EN EL CASO DE PYTHON NO EXISTE LA ESTRUCTURA SEGUN O SWITCH ASI QUE SE UTILIZARA SECUENCIAS ANIDADAS DE IF. 

dia=int(input("Digite un numero:\n"))

if dia == 1:
  print('lunes')
if dia == 2:
  print('martes')
if dia == 3:
  print('miércoles')
if dia == 4:
  print('jueves')
if dia == 5:
  print('viernes')
if dia == 6:
  print('sábado')
if dia == 7:
  print('domingo')
if dia < 1 or dia > 7:
  print('error')