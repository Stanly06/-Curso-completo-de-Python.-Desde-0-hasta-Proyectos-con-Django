#para crear un diccionario usamos llaves "{}" tenemos una lista de clave y valor seprados por ":"
personas = {'Stanly':27, 'Maria':22, 'Martin':66, 'Patricia':55}
print(personas)

#podemos consultar el valor de una clave de esta manera:
print(personas['Stanly'])

#para insertar o modificar una clave o valor al diccionario:
personas['Jose'] = 42
personas['Stanly']=30

#tambien podemos eliminar una clave usando el metodo "del"
del personas['Martin']

print(personas)
