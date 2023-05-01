# Lo que ponemos en un conjunto no se puede repetir el mismo elemento

conjunto = set()
conjunto = {2, 'Python', 'Bryan', True}
conjunto.add('Martin')
conjunto.discard('Bryan')
conjunto.discard(True)
#conjunto.clear()
print('Python' in conjunto)
# esta consulta nos busca la palabra 'Python' en el conjunto y devuelve un valor booleano "True"
print('Marcos' not in conjunto)

#usamos el metodo "clear" para eliminar todos los elementos del conjunto
#usamos el metodo "discard" para eliminar algun elemento del conjunto
#usamos el metodo "add" para agregar un nombre en cuallquier orden del conjunto
#los conjuntos las colecciones no son ordenadas 
#no soporta: diccionario, tuplas o listas


