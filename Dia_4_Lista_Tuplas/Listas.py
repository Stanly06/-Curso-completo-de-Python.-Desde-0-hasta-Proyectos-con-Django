personas = ['Martin', 'Maria', 'Gonzalo', 'Raul', 'Pamela']

print(personas[0])
#los indices en cualquier lenguaje de programacion inician a partir del '0

print(personas[-1])

#-para borrar algo de la lista de la variable 'personas' usamos el metodo "del"
#-para agregar una persona a la lista usamos la funcion 'insert' colocamos el indice y el nombre
#-para agregar un valor a la lista al final de esta usamos el metodo 'appen' 
# no es necesario poner el indice

del personas[1]
personas.insert(0,'Matias')
personas.append(10)
print(personas)

#podemos crear una lista dentro de otra lista y usamos los mismo criterios
categorias = ['Martin', 10, True, 
              ['Python','Java', 'C'], 1.0]
print(categorias[3][2])

#si queremos que nos muestre la lista apartir del segundo elemento colocamos 
# el numero 2 seguido de ":"
print(categorias[2:])

