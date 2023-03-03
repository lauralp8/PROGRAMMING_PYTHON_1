a = []
b = []
# tipo de atributo
print(type(a))
# mira si está en el mismo espacio de memoria
print(a is b)
# mismo espacio de memoria
a = b
print(a is b)


# añade el elemento que quieras al final de la lista que le ordenes
a.append(1)
print(a)
a.append(7)
print(a)

a = [2,3]
print(a)
b = [4,5]
c = (a,b)
print(c)

# te devuelve el tipo del objeto
c[0]
print(type(c[0]))   #lista
print(type(c))      #tupla
print(id(c[0]))     #posicion de memoria
print(c)


#callable: se usa para que una función se pueda llamar desde otra
#el callable se tiene que importar
#el callable devuelve una función que hace que se pueda llamar
from typing import Callable
"""
    crear dos funciones
"""
def f(x)->Callable:
    return 4*(x**2)*3   # hace esto callable

def g(x)->Callable:
    return 2*x+1        # haces esto callable

print(f(4))
print(g(2))

"""
    crear una tercera función que sea la composición de ambas
"""
def fog(x):
    return f(g(x))

print(fog(4))


