# Programa para verificar contraseña:

# Definir la contraseña
contraseña = "contraseña123"

# Pedir al usuario que ingrese la contraseña
ingreso = input("Ingresa la contraseña: ")

# Verificar si la contraseña ingresada coincide con la guardada en la variable
if ingreso == contraseña:
    print("La contraseña ingresada es correcta.")
else:
    print("La contraseña ingresada es incorrecta.")

#Programa para dividir dos números:

# Pedir al usuario que ingrese dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Verificar si el segundo número es cero
if num2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Realizar la división y mostrar el resultado en la consola
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)

 #Programa para verificar si un número es par o impar:

 # Pedir al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")

#Programa para verificar si una persona puede ingresar a un lugar:

# Pedir al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Verificar si la edad es menor a 19
if edad < 19:
    print("No puedes ingresar.")
else:
    print("Bienvenido.")
