# MAPAS
# map devuelve algo en función de una condición

# EJEMPLO 1
# modificamos la lista en función de la condición puesta en lambda
data = [1, 3, 5, 2, 7, 4, 10]
print('data', data)

# apply the lambda function to each element in the list
# using the map function
# suma uno a cada elemento
d1 = list(map(lambda i: i+1, data)) # list porque lo queremos transformar en una lista
# si no ponemos list imprime la dirección de memoria
print('d1', d1)

# EJEMPLO 2
def add_one(x):
    x = x+1
    return x

data1 = [1, 3, 4, 5]
result = list(map(add_one, data1))
print('RESULTADO:\t', result)

data2 = [2, 3, 4]
data3 = [4, 4, 7]
suma = list(map(lambda x, y: x+y, data2, data3))
print(suma)

# EJEMPLO 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
data = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
ages = list(map(lambda p: p.age, data)) # sólo imprime las edades
print(ages)
# para que sólo imprima los nombres:
names = list(map(lambda l: l.name, data))
print(names)


# FILTROS
# hace condiciones para eliminar en base a los valores que no cumplen dicha condición

# EJEMPLO 1
# que te devuelva los valores pares
valores = [1, 3, 5, 4, 6, 10, 2]
print('valores', valores)

pares = list(filter(lambda i: i%2 == 0, valores))
print('pares', pares)


# MEZCLA MAP Y FILTER
# primero filtras y luego modificas
# una lista que sume diez a los valores pares

print("\n\n\nEJERCICIO MEZCLA MAP/FILTER")
numeros = [1,4,5,6,7,10,19,18]
print('numeros', numeros)

numeros_pares = list(map(lambda n: n+10, (filter(lambda p: p%2==0, numeros))))
print('numeros pares',numeros_pares)

# REDUCE
# te suma todos los valores de una lista
# EJEMPLO 1
from functools import reduce
data =[1,2,3,4,5,6,7]
result = reduce(lambda total, value: total+value, data)
print(result)

# EJEMPLO 2
data = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
total_age = reduce(lambda running_total, person: running_total + person.age, data, 0)
average_age = total_age // len(data)
print('Average age:', average_age)
# Alternatve with generator expresssion total_age_alterative = sum(person.age for person in data)

