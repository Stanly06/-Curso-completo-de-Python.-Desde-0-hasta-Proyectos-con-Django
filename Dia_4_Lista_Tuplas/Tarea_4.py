#1. Escriba un programa que almacene en una Lista los cursos que has cursado o los que te gustaría cursar en Udemy
# Luego muestre la lista por consola.

cursos = ["Google Data Analytics", "Power Bi and Bussines intelligent", "SQL", "Data science with Python"]

print("Los cursos que has cursado o te gustaría cursar en Udemy son:")
for curso in cursos:
    print(curso)

#2. Escriba un programa que almacene personas en una lista,
#  luego que le muestre por pantalla el mensaje de ‘Su nombre es ‘nombre’

personas = ["Juan", "María", "Pedro", "Luisa"]

print("Su nombre es", personas[0])
print("Su nombre es", personas[1])
print("Su nombre es", personas[2])
print("Su nombre es", personas[3])

#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} 
# Luego pregunte al usuario por una divisa y muestre en consola el símbolo o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Introduzca una divisa: ")

if divisa in divisas:
    print("El símbolo de", divisa, "es", divisas[divisa])
else:
    print("La divisa", divisa, "no se encuentra en el diccionario")

#4. En una tupla coloque los siguientes
#valores: números enteros, decimales, String, colecciones. Luego muestre en consola

tupla = (10, 3.14, "Hola", [1, 2, 3], {"nombre": "Juan", "edad": 30})

print(tupla)
