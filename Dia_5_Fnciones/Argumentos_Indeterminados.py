# usamos el metodo 'args' para pasar argumentos indeterminados colocamos el *

def sumar (*args):
    for i in args:
        print(i)


sumar('Python', True, 1.2, [1,2,3,4,5], 'Brian')    