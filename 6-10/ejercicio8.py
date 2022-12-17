# leemos el promedio y conducta del alumno:
promedio = int(input("Ingrese su promedio \n"))

# usamos una selección múltiple para determinar en que salon le toca al estudiante.
if promedio >=17 and promedio<=20:
    print("estudias en la seccion A")
elif (promedio >=15) and (promedio <17):
    print("estudias en la seccion B")
elif (promedio >=13) and (promedio <15):
    print("estudias en la seccion C")
elif (promedio >=11) and (promedio <13):
    print("estudias en la seccion D")
elif(promedio >20):
    print("Sigue pensando que con tu veintiquince aprobaste noma")
else:
    print("repetiste de año")
