#Preguntas de esta tarea
# Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’

def saludar():
    print("¡Hola mundo!")

saludar()


# Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ¡Hola <nombre>!

def saludar(nombre):
    print("¡Hola", nombre + "!")

nombre = input("Ingrese su nombre: ")
saludar(nombre)

# Cree una función que le pida el usuario su nombre y su edad, luego muestre en pantalla los resultados.

def saludar(nombre):
    print("¡Hola", nombre + "!")

nombre = input("Ingrese su nombre: ")
saludar(nombre)

# Definir una función que reciba dos números por parámetros y que luego los sume.
def sumar(a, b):
    resultado = a + b
    return resultado

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
resultado_suma = sumar(numero1, numero2)
print("El resultado de la suma es:", resultado_suma)
