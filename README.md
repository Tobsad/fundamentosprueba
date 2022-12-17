# Fundamentos

---

## Semana N°05

---

1. Estructuras secuenciales para algoritmos en pseudocodigos y en Python
2. Estructura deasignación, de salida para algoritmos en pseudocódigos y en Python

Crea estructura de entrada:formato.

Crea diseña estructura de salida:formato.

Ejercicio 1

```python
#Solicitar nombre, apellido y codigo del estudiante

nombre=input("Inserte su nombre: \n" )

apellido=input("Inserte su apellido: \n")

codigo=input("Inserte su codigo de estudiante \n")

print("***************************")
print("Su nombre es ",nombre, ".")
print("Su apellido es ",apellido ,"." )
print("Su codigo de estudiante es", codigo,".")
```

Ejercicio 2

```python
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas=int(input("Ingrese las horas trabajadas:\n"))

pagoPorHora=int(input("Ingrese el costo por hora trabajada: \n"))

total=horasTrabajadas*pagoPorHora

print("Su pago es de ",total, "soles, por sus",horasTrabajadas,"horas trabajas. Con la paga de ",pagoPorHora," soles por hora.")
```

Ejercicio 3

```python
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
```

Ejercicio 4

Aquí tienes dos ejemplos de entrada y salida de datos más complejos en Python:

1. Dado un número entero N, imprima el número invertido.
    
    ```python
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
    ```
    

Ejercicio 5

1. Ejemplo de entrada y salida de una cadena de texto:
    
    ```python
    # Solicitamos al usuario que ingrese una lista de números
    lista = input("Ingresa una lista de números separados por espacios: ")
    
    # Convertimos la cadena de texto ingresada por el usuario en una lista de números
    lista = [int(x) for x in lista.split()]
    
    # Imprimimos la lista de números ingresada por el usuario
    print("La lista de números que ingresaste es: ", lista)
    
    ```
    

## Semana N°06

---

Estructuras selectivas simple, doble y múltiple para algoritmos en pseudocódigosy en Python  (simple , doble y multiple)

1. **Problema:** Dado un número entero N, determine si es par o impar.
    
    ```python
    # leemos el número entero N
    N = int(input("Ingrese un numero entero:\n"))
    
    # usamos una selección doble para determinar si N es par o impar
    if N % 2 == 0:
      print("par")
    else:
      print("impar")
    
    #en este caso el problema es con el 0.
    ```
    
2. **Problema:** Dado un número entero N, determine si es divisible por 3 y por 5.
    
    ```python
    # leemos el número entero N
    N = int(input("Ingrese un numero entero \n"))
    
    # usamos una selección doble para determinar si N es divisible tanto por 3 como por 5
    if N % 3 == 0 and N % 5 == 0:
      print("divisible")
    else:
      print("no divisible")
    
    ```
    
3. **Problema:** Dado un número entero N, determine si es divisible por 2, 3, 4 o 5.
    
    ```python
    # leemos el número entero N
    N = int(input("Ingrese un numero entero \n"))
    
    # usamos una selección múltiple para determinar si N es divisible por 2, 3, 4 o 5
    if N % 2 == 0:
      print("divisible por 2")
    elif N % 3 == 0:
      print("divisible por 3")
    elif N % 4 == 0:
      print("divisible por 4")
    elif N % 5 == 0:
      print("divisible por 5")
    else:
      print("no divisible")
    
    ```
    
4. **Problema**: Dado un número entero N, determine si es negativo, cero o positivo
    
    ```python
    #Problema: Dado un número entero N, determine si es negativo, cero o positivo
    
    # leemos el número entero N
    N = int(input())
    
    # usamos una selección múltiple para determinar si N es negativo, cero o positivo
    if N < 0:
      print("negativo")
    elif N == 0:
      print("cero")
    else:
      print("positivo")
    ```
    
5. **Problema:** Imprime si eres millenial o no
    
    ```python
    #Imprime si eres millenial o no
    # leemos el número entero N
    fecha= int(input("Escribe tu año de nacimiento: \n"))
    if fecha>=2000:
        print("Eres millenial.")
    
    ```
    

## Semana N°07

---

Algoritmos con estructuras secuenciales y selectivas para algoritmos en pseudocódigos y en Python

1. Dia de la semana =[1,7]
    
    ```python
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
    
    ```
    
2. Imprimir el mayor numero o indicar igualdad.
    
    ```python
    #Escribir un programa que lea dos números enteros y muestre por pantalla el mayor de ellos.
    #Ingresamos el primer numero
    num1 = bool(input("Ingrese un numero negativo,cero o positivo: \n"))
    #Ingresamos el segundo numero
    num2 = bool(input("Ingrese otro numero negativo,cero o positivo: \n"))
    #La secuencia analizara los numeros y mostrara dependiendo del caso
    if (num1>num2):
        print("El mayor numero es: ",num1)
    if (num2>num1):
        print("El mayor numero es: ",num2)
    else:
        print("Ambos numeros son iguales")
    
    ```
    
3. Se pide ingresar una letra del alfabeto y mostrar si dicha letra es vocal o consonante.
    
    ```python
    #Se pide ingresar una letra del alfabeto y mostrar si dicha letra es vocal o si es otro tipo de dato.
    letra=str(input("Ingrese una letra del alfabeto:\n").upper()) 
    
    #Se le agrego el .upper para que la letra ingresada se transforme en mayuscula 
    # ahora pasara a analizar la letra si es un vocal sea minuscula o mayuscula imprimira es un vocal.
    # de caso contrario dira que es una consonante. 
    
    if (letra=="A")or(letra=="E")or(letra=="I")or(letra=="O")or(letra=="U"):
        print("Es una vocal")
    else:
        print("Es una consonante,numero o caracter especial.")
    ```
    
4. Diseñe un algoritmo que lea un número y determine si es o no capicúa.
    
    ```python
    #Diseñe un algoritmo que lea un número y determine si es o no capicúa.
    
    # leemos el número 
    numero= int(input("Inserte un numero:\n"))
    
    # convertimos N a una cadena de caracteres y lo guardamos en la variable texto
    texto= str(numero)
    
    # invertimos n_str y lo guardamos en la variable inverted_str
    numeroinverso= texto[::-1]
    
    # convertimos inverted_str a un número entero y lo guardamos en la variable inverted_num
    numeroinverso = int(numeroinverso)
    
    #Si el numero invertido es igual al numero original imprimieros que es capicua, de no ser asi diremos que no lo es 
    if (numero==numeroinverso):
        print("El numero ",numero, " es capicua")
    else:
        print("El numero ",numero," no es capicua")
    
    ```
    
5. Construir un algoritmo que permita ingresar un número, si el número es mayor de 500, 
# se debe calcular y mostrar en pantalla el 20% de este.
    
    ```python
    #Construir un algoritmo que permita ingresar un número, si el número es mayor de 500, 
    # se debe calcular y mostrar en pantalla el 20% de este.
    numero=int(input("Digite un numero: \n"))
    
    #Si el numero es mayor que 500 imprimira que este es mayor que 500 y junto al 20% del numero ingresado
    porcentaje=0.2*numero
    
    if (numero>500):
        print("El numero es mayor que 500 y su 20% es igual a ",porcentaje,".")
    else:
        print("Su numero es inferior o igual a 500")
    
    ```
    

## Semana N°08

---

Estructuras repetitivas para algoritmos en pseudocódigo y en Python

1. Escribir un programa que imprima por pantalla los números del 1 al numero insertado
    
    ```python
    #Escribir un programa que imprima por pantalla los números del 1 al numero insertado
    
    numero=int(input("Ingrese un numero:\n"))
    
    print("Empezando a contar...")
    
    if (numero==10):
        for i in range(1,numero+1):
            print(i)
            if (i==2):
                print("Freddy viene por ti!")
            elif (i==4):
                print("mejor cierra la puerta!")
            elif (i==6):
                print("coge tu crucifijo!")
            elif (i==8):
                print("mejor que te quedes despierto hasta tarde!")
            elif (i==10):
                print("¡nunca volverás a dormir!")
    else:
        for i in range(1,numero+1):
            print(i)
    
    ```
    
2. Escribir un programa que calcule la suma de los números pares del 1 al numero insertado
    
    ```python
    #Escribir un programa que calcule la suma de los números pares del 1 al numero insertado
    
    #Solicitamos el limite de la cadena de numeros:
    limite=int(input("Ingrese un numero:\n"))
    
    # Inicializamos una variable para almacenar la suma
    suma = 0
    
    # Recorremos los números del 1 al numero insertado
    for i in range(1, limite+1):
      # Si el número es par, lo sumamos a la variable suma
      if i % 2 == 0:
        suma += i
    
    # Mostramos la suma por pantalla
    print(suma)
    
    ```
    
3. 1. Escribir un programa que lea una cantidad de números y calcule su promedio.
    
    ```python
    #Escribir un programa que lea una cantidad de números y calcule su promedio.
    
    # Pedimos al usuario que ingrese la cantidad de números
    cantidad = int(input("Ingrese la cantidad de números: "))
    
    # Inicializamos una variable para almacenar la suma de los números
    suma = 0
    
    # Recorremos los números ingresados
    for i in range(cantidad):
      # Pedimos al usuario que ingrese un número
      print("Ingrese el número #",i+1,":")
      num = float(input())
      # Sumamos el número a la variable suma
      suma += num
    
    # Calculamos el promedio
    promedio = suma / cantidad
    
    # Mostramos el promedio por pantalla
    print("El promedio es:", promedio)
    
    ```
    
4. Escribir un programa que imprima por pantalla los números del 1 al 100, con una fila por cada 10 números.
    
    ```python
    # Recorremos los números del 1 al 100
    for i in range(1, 101):
      # Imprimimos el número
      print(i, end=" ")
      # Si el número es múltiplo de 10, hacemos un salto de línea
      if i % 10 == 0:
        print()
    
    ```
    
5. Cambiar vocales por la consonante t y consonantes por la letra e
    
    ```python
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
    ```
    

## Semana N°09

---

Estructuras repetitivas para algoritmos en pseudocódigos y enPython (hasta for) y acumuladores y contadores

1. Escribir un programa que calcule el factorial de un número.
    
    ```python
    #Escribir un programa que calcule el factorial de un número.
    
    # Pedimos al usuario que ingrese un número
    num = int(input("Ingrese un número: "))
    
    # Inicializamos un acumulador para almacenar el factorial
    factorial = 1
    
    # Recorremos los números del 1 al número ingresado
    for i in range(1, num + 1):
      # Multipilcamos el acumulador por el número actual
      factorial *= i
    
    # Mostramos el factorial por pantalla
    print("El factorial es:", factorial)
    
    ```
    
2. Escribir un programa que lea una lista de números y calcule la suma de los números pares.
    
    ```python
    # Inicializamos una lista de números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Inicializamos un acumulador para almacenar la suma de los números pares
    suma = 0
    
    # Recorremos la lista de números
    for num in numeros:
      # Si el número es par, lo sumamos al acumulador
      if num % 2 == 0:
        suma += num
    
    # Mostramos la suma por pantalla
    print("La suma de los números pares es:", suma)
    
    ```
    
3. Escribe un programa que calcule la suma de todos los números divisibles por 3 o 5 menores a un numero ingresado en python.
    
    ```python
    #Escribe un programa que calcule la suma de todos los números divisibles por 3 o 5 menores a un numero ingresado en python.
    
    print("Ingrese un limite:")
    
    limite=int(input())
    print("Imprimiendo los numeros divisibles de 3 o 5...")
    sum = 0
    
    for i in range(1, limite):
        
        if i % 3 == 0 or i % 5 == 0:
          print(i)
          sum += i
    
    print("La suma de los numeros divisibles entre 3 y 5 es:",sum)
    
    ```
    
4. #Realiza una tabla de multiplicar del numero que se ingrese:
    
    ```python
    #Realiza una tabla de multiplicar del numero que se ingrese:
    print("La tabla de que numero deseas saber?")
    num=int(input())
    
    print("Hasta que multiplo deseas aprender?")
    
    multiplicar=int(input())
    print("Mostrando tabla del numero",num,"hasta ",multiplicar)
    
    for i in range(1, multiplicar+1):
        print(f"{num} x {i} = {num * i}")
    
    ```
    
5. Escribe un programa que lea una lista de palabras del usuario y luego imprima cada palabra junto con su longitud.
    
    ```python
    #Escribe un programa que lea una lista de palabras del usuario y luego imprima cada palabra junto con su longitud.
    
    words = input("Ingresa una lista de palabras separadas por espacios:\n ").split()
    print()
    for word in words:
        print(f"::{word} tiene {len(word)} letras")
    
    ```
    

## Semana N°10

---

Estructuras repetitivas para algoritmos en pseudocodigos y enPython (mientras while)

1. Escriba un programa que valide si una nota está entre 0 y 10, sino está entre 0 y 10 la nota se pedirá de nuevo hasta que la nota sea correcta.
    
    ```python
    #Escriba un programa que valide si una nota está entre 0 y 10, 
    # sino está entre 0 y 10 la nota se pedirá de nuevo hasta que la nota sea correcta.
    
    nota=nota=int(input("Ingrese una nota: "))
    print("******************")
    
    while (nota>20) or (nota<0) :
        print("ERROR!!...Por favor, ingrese una nota corecta")
        nota=int(input("Nota: "))
    print("Su nota es correcta.")
    
    ```
    
2. Escriba un programa en el cual se ingrese un valor límite positivo, y a continuación solicite números al usuario hasta que la suma de los números introducidos supere el límite inicial.
    
    ```python
    #Escriba un programa en el cual se ingrese un valor límite positivo, y a continuación solicite números al usuario
    # hasta que la suma de los números introducidos supere el límite inicial.
    #Solicitamos el limite 
    limite = int(input("Ingresa un valor límite positivo: "))
    #Declarammos un variable que guardara las suma de los numeros escritos
    suma = 0
    #Se invoca el bucle para que se vayan sumando los numeros a medida que no pase el limite , de pasar el limite 
    #Terminara el bucle
    while suma < limite:
        numeros = int(input("Ingresa un número: "))
        suma += numeros
        print("vas sumando: ",suma)
    #Se imprimira la suma de los numeroes y el limite que se dio
    print(f"La suma de los números introducidos es {suma}, lo cual supera el límite de {limite}.")
    
    ```
    
3. Escriba un programa en el cual se ingrese un número y mientras ese número sea mayor de 10, se pedirá el número de nuevo.
    
    ```python
    #Escriba un programa en el cual se ingrese un número
    # y mientras ese número sea mayor que 10, se pedirá el número de nuevo.
    num = int(input("Ingresa un numero:\n"))
    
    while (num>10):
        num = int(input("Ingresa otro numero:\n"))
        
    print("Saliste del bucle por digitar un numero menor o igual que 10 ")
    
    ```
    
4. Escriba un programa que solicite dos números enteros (mínimo y máximo). A continuación, se debe pedir al usuario que ingrese números enteros situados entre el máximo y mínimo. Si el #2 es menor que el #1 se le pedira que registre otros 2 numeros hasta que se cumpla lo requerido.
Si el usuario sigue en el bucle imprime "Recuerda que aveces menos es mas"
Si sale del bucle imprimir , "Encontraste la solucion, no lo comentes a nadie."
    
    ```python
    #Escriba un programa que solicite dos números enteros (mínimo y máximo). 
    #A continuación, se debe pedir al usuario que ingrese números enteros situados entre el máximo y mínimo.
    #Si el #2 es menor que el #1 se le pedira que registre otros 2 numeros hasta que se cumpla lo requerido.
    #Si el usuario sigue en el bucle imprime "Recuerda que aveces menos es mas"
    #Si sale del bucle imprimir , "Encontraste la solucion, no lo comentes a nadie."
    
    num1 = int(input("Ingresa el #1 numero:\n"))
    num2 = int(input("Ingresa el #2 numero:\n"))
    
    while (num1>num2):
        print("Recuerda que aveces menos es mas")
        num1 = int(input("Ingresa el #1 numero denuevo:\n"))
        num2 = int(input("Ingresa el #2 numero denuevo:\n"))
    print("Encontraste la solucion: gracias por darte cuenta.")
    
    ```
    
5. Escriba un programa que solicite al usuario números decimales mientras que el usuario escriba números mayores al primero que se ingresó. Por ejemplo: si el usuario ingresa como primer número un 3.1, y luego ingresa un 4, el programa debe solicitar un tercer número. El programa continuará solicitando valores sucesivamente mientras los valores ingresados sean mayores que 3.1, caso contrario, el programa finaliza.
    
    ```python
    
    #Escriba un programa que solicite al usuario números decimales 
    #mientras que el usuario escriba números mayores al primero que se ingresó.
    #Por ejemplo: si el usuario ingresa como primer número un 3.1, y luego ingresa un 4,
    #el programa debe solicitar nuevamente un número.
    #el programa continuará solicitando valores sucesivamente mientras los valores ingresados sean mayores que 3.1,
    #caso contrario, el programa finaliza.
    
    print("Ingrese 2 numeros decimales")
    
    num1 = float(input("Ingresa el #1 numero:\n"))
    num2 = float(input("Ingresa el #2 numero:\n"))
    
    while (num1<num2):
        num2 = float(input("Ingresa otro numero:\n"))
    print("Salio del bucle, ingreso un numero menor al primero.")
    ```
    

## Semana N°11

---

Estructuras repetitivas para algoritmos en pseudocodigos y en Python (hacer-mientras que)

1. Realizar un programa que solicite al usuario su código de usuario (un número entero
mayor que cero) y su contraseña numérica (otro número entero positivo). El programa no
le debe permitir continuar hasta que introduzca como código 1024 y como contraseña
4567. El programa finaliza cuando ingresa los datos correctos.
    
    ```python
    
    #Realizar un programa que solicite al usuario su código de usuario (un número enteromayor que cero)
    #  y su contraseña numérica (otro número entero positivo). 
    # El programa nole debe permitir continuar hasta que introduzca como código 1024 y como contraseña 4567. 
    # El programa finaliza cuando ingresa los datos correctos.
    
    print("Ingrese sus datos:")
    
    usercode= int(input("Ingrese su codigo institucional:\n"))
    password= int(input("Ingrese su contraseña numerica:\n"))
    uservalid=1024
    passvalid=4567
    
    while (usercode!=uservalid):
        usercode= int(input("Ingrese su codigo institucional correctamente:\n"))
        if(usercode==uservalid):
            print("CORRECTO...")
    while (password!=passvalid):
        password= int(input("Ingrese su contraseña numerica correctamente:\n"))
        if(password==passvalid):
            print("CORRECTO...")
    print("Inicio sesion correctamente")
    ```
    
2. Se debe realizar un programa que: 
1o) Pida por teclado un número (entero positivo). 
2o) Pregunte al usuario si desea introducir o no otro número. 
3o) Repita los pasos 1o y 2o mientras que el usuario no responda n/N (no). 
4o) Muestre por pantalla la suma de los números introducidos por el usuario.
    
    ```python
    #Se debe realizar un programa que:
    # 1 Pida por teclado un número entero positivo.
    # 2 Pregunte al usuario si desea introducir o no otro número.
    # 3 Repita los pasos 1o y 2o mientras que el usuario no responda n/N no.
    # 4 Muestre por pantalla la suma de los números introducidos por el usuario.
    
    num1 = int(input("Ingresa un numero:\n"))
    
    rpta=str(input("Desea ingresar otro numero? (s/n):\n")).upper()
    
    S=True
    N=False
    
    aculumador=0
    aculumador+=num1
    
    while (rpta=='S'):
        num1 = int(input("Ingresa otro numero:\n"))
        rpta2=str(input("Desea ingresar otro numero? (s/n): ")).upper()
        rpta=rpta2
        aculumador+=num1
        
    print("La suma de numeros ingresados es:",aculumador)
    
    ```
    
3. Se pide escribir un programa que calcule la suma de los N primeros números pares. Es decir, si ingresamos el número 5 como valor de N, el algoritmo nos debe realizar la suma #de los siguientes valores: 2+4+6+8+10.
    
    ```python
    #Se pide escribir un programa que calcule la suma de los N primeros números pares. Es
    #decir, si ingresamos el número 5 como valor de N, el algoritmo nos debe realizar la suma
    #de los siguientes valores: 2+4+6+8+10.
    
    # Pedimos al usuario que ingrese el valor de N
    n = int(input("Ingrese el valor de N: "))
    
    # Inicializamos la variable acumuladora en 0
    suma = 0
    
    # Recorremos los N primeros números pares
    for i in range(1, n+1):
      # Si el número es par, lo sumamos a la variable acumuladora
      if i % 2 == 0:
        suma += i
    
    # Mostramos el resultado
    print("La suma de los N primeros números pares es:", suma)
    
    ```
    
4. Programar un juego donde la computadora elige un número al azar entre 1 y 10, y a continuación el jugador tiene que adivinarlo. La estructura del programa es la siguiente: 
1o) El programa elige al azar un número n entre 1 y 10. 
2o) El usuario ingresa un número x. 
3o) Si x no es el número exacto, el programa indica si n es más grande o más pequeño #que el número ingresado. 
4o) Repetimos desde 2) hasta que x sea igual a n. 
El programa tiene que imprimir los mensajes adecuados para informarle al usuario qué #hacer y qué pasó hasta que adivine el número.
    
    ```python
    #usamos el importrandom para que pueda escoger un numero al alzar 
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
    
    ```
    
5. Hacer un algoritmo para calcular la media de los números pares e impares, sólo se ingresará diez números.
    
    ```python
    #Hacer un algoritmo para calcular la media de los números pares e impares, sólo se ingresará diez números.
    
    #Para hallar la media aritmetica de los números pares e impares de un conjunto de 10 números ingresados, podemos utilizar dos acumuladores, en 1 usaremos sumar los números pares y la otra para sumar los números impares. 
    #También podemos utilizar dos contadores, uno para llevar el número de números pares y le otro impares.
    
    # Inicializamos las variables acumuladoras y los contadores
    suma_pares = 0
    suma_impares = 0
    contador_pares = 0
    contador_impares = 0  
    # Recorremos los 10 números
    for i in range(10):
      # Pediremos al usuario que ingrese un número
      num = int(input("Ingrese un número: "))
    
      # Comprobamos si el número es par o impar
      if num % 2 == 0:
        suma_pares += num
        contador_pares += 1
      else:
        suma_impares += num
        contador_impares += 1
    
    # Calculamos las medias
    media_pares = suma_pares / contador_pares
    media_impares = suma_impares / contador_impares
    
    # Mostramos los resultados
    print("La media de los números pares es:", media_pares)
    print("La media de los números impares es:", media_impares)
    
    ```
    
    ---
