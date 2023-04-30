# Preguntas de esta tarea
# 1. Escriba un programa que lea dos números por teclado y determine con un valor booleano de True o False estos ejemplos:

# Pedir al usuario que ingrese dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Verificar si los números son iguales
igual = num1 == num2

# Verificar si los números son diferentes
diferente = num1 != num2

# Verificar si el primer número es mayor que el segundo
mayor = num1 > num2

# Verificar si el segundo número es mayor o igual al primero
mayor_igual = num2 >= num1

# Imprimir los resultados
print("Los números son iguales:", igual)
print("Los números son diferentes:", diferente)
print("El primer número es mayor que el segundo:", mayor)
print("El segundo número es mayor o igual que el primero:", mayor_igual)

# Conociendo los operadores lógicos,
# realice una comprobación si una cadena de texto ingresada desde teclado 
# por le usuario tiene la longitud mayor o igual que 4 y a su vez que 7 
# (determinar con un valor booleano True o False)

# Pedir al usuario que ingrese una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Verificar si la longitud de la cadena es mayor o igual a 4 y menor o igual a 7
longitud = len(cadena)
validacion = longitud >= 4 and longitud <= 7

# Imprimir el resultado
print("La cadena de texto tiene longitud mayor o igual a 4 y menor o igual a 7:", validacion)
