# iterador = capacidad de hacer una secuencia en un objeto
# iteración secuencia en base de un patrón
# CLASES:

class Evens(object):
    def __init__(self, limit):
        self.limit = limit
        self.val = 0

    # makes this class iterable (lo ponemos siempre)
    def __iter__(self):
        return self

    # makes this class an iterator
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            return_val = self.val
            self.val += 2
            return return_val

it = Evens(4)   # creas un objeto it de la clase Evens, con valor 4
print(next(it))
print(next(it))
print(next(it))

# cuando haya un problema que printee end, en vez de que salte el error, haciendo un bucle
try:
    print(next(it))
except StopIteration:
    print("end")


# no todos los iteradores son clases, también pueden ser LISTAS:
shopping_list = ['ham', 'spam', 'jam']
it = iter(shopping_list)
# como es una lista ya sabemos el patrón, next simplemente imprime el siguiente elemento
for i in range(len(shopping_list)):
    print(it.__next__())


# los for se consideran iterables
# recorren algo (una secuencia) para realizar un proceso en función de una condición
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
"""
for line in open("myfile.txt"):
    print(line, end='')
"""

# clase que pases un string y lo devuelva al revés
class Reverse():
    def __init__(self, cadena):
        self.cadena = cadena
        self.longitud = len(cadena)

    # makes this class iterable (lo ponemos siempre)
    def __iter__(self):
        return self

    # makes this class an iterator
    def __next__(self):
        if self.longitud == 0:
            raise StopIteration
        else:
            self.longitud = self.longitud-1
            return self.cadena[self.longitud]

sucesion = Reverse('abcde')   # creas un objeto it de la clase Evens, con valor 4
print(next(sucesion))
print(next(sucesion))
print(next(sucesion))
print(next(sucesion))
print(next(sucesion))



# GENERADORES
def f(m, d):
    a = 0
    for i in range(m):
        yield a
        a+=d

g = f(5,2)
print(next(g))
print(next(g))

# le podemos enviar un valor
# g.send(10)


def f(accum, m):
    for i in range(m):
        rcv = yield accum
        if rcv is None:
            accum -=1
        else:
            accum =rcv

g = f(0,4)
next(g)         # devuelve 0 y se queda en el yield
next(g)         # la del yield se resuelve a None (porque esta igualado en una variable
# como es None se mete en el if
g.send(10)      # vuelve a empezar el bucle con el valor que le quieras asignar

