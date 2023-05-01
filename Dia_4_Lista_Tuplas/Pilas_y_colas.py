fila = ['Jose', 'Maria', 'Raul', 'Paola']
print(fila)

#suponiendo que es una fila en el supermercado y llega un cliente, usamos el metodo "append"
#  para agregar la ultima persona en llegar a la fila
fila.append('Romina')
print(fila)

#acontinuacion tomando el primero que ingresa "Jose" sea el primero en salir de la fila
i = fila.pop(0)
#el metodo "pop" va a eliminar el ultimo de la fila pero al agregarle '0' eliminara el primer indice
print(i)
print(fila)
#ahora quien esta primera en la fila es 'Maria' ya que sacamos a 'Jose' de la fila

#usamos la "f" para poder ingresar la variable "i" en las llaves "{}" y concatenar a "i"
print(f'En este momento estan atendiendo a {i}')
print(fila)

