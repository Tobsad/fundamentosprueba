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