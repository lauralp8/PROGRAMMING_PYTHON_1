#devolución de múltiples valores
def swap(a: int, b: int):
    return b, a
a=2
b=3
x = swap(a, b)      # devuelve tupla que sea así
print(x)
x, y = swap(a, b)   # acoplas valores/variables
print(x)
print(y)

#cuando no sabes cuantos valores de un parámetro vas a pasar utilizas *
def clase(*nombres):
    for i in nombres:
        print("El alumno es", i)

clase("Laura", "Hugo", "Carlos", "Ana")

#otra forma de hacer el for
#te convierte lo que tu estás pasando en una lista
def clase_for(*animales):
    for i in range(len(animales)):
        print("Su animal es", animales[i])
    return animales

#para imprmir la lista
lista_animales = clase_for("gato", "perro", "cobaya")
print(lista_animales)

#la key del diccionario es la palabra que se va a definir
#value es el valor
#KWARGS (2 ASTERISCOS)
def parametros(**kwargs):       # diccionarios
    for key in kwargs.keys():
        print("Parámetro:", key, "Valor:", kwargs[key])

#creamos el diccionario
parametros(a=1, b=2, c=3)


#al llamar a la función, utilizamos * para no tener que definir también el tamaño de las listas
#función que sume todos los elementos de la lista
def suma(*elementos):
    total = 0
    for i in elementos:
        total += i
    return total

#definimos las listas
lista1=[1,2,3]
lista2=[2,7]
lista3=[1,2,3,4,5]
#con * ponemos los elementos que faltan de la lista como si fuesen 0
print(suma(*lista1, *lista2, *lista3))


# QUEREMOS QUE TENIENDO UN DIC NOS DEVUELVA DOS, UNO CON POSITIVOS Y OTRO CON NEGATIVOS
#diccionarios (pasamos diccionarios de diferente longitud)
def custom_dict(**kwargs):
    # creamos los diccionarios auxiliares:
    p={}
    v={}
    for key in kwargs.keys():
        if type(kwargs[key])==int: # si valor de tipo int
            if(kwargs[key]<=0): # si valor <=0
                p[key] = kwargs[key] # dentro del dic p guardamos el parametro que se igualará al valor
            else:
                v[key] = kwargs[key]
    return p, v

#almacenamos cada diccionario en una variable
p, v= custom_dict(a=1, b=-2, c=3, d='a')
print(p,v)


# LAMBDA
from typing import Tuple
def sorting_criteria(x:Tuple[str, str, int]) :
    return x[2]     # devuelve la 3º posición de la Tupla creada

student_tuples=("hola","laura",2)   #TUPLA PARÉNTESIS
print(student_tuples[1])

#un sorted normal te ordena de menor a mayor (orden ascendente)
# queremos ordenar una lista de tuplas
student_tuples=[
    ('john','A',15),
    ('jane','B',12),
    ('dave','C',10),
]
ordenar=sorted(student_tuples, key=sorting_criteria)
print(ordenar)
# key ordena la tupla en función de lo que devuelva la función que le has pasado
# SIEMPRE USAMOS EL LAMBDA
# simplificas la función, utilizas lambda para para decir con que ordenas
print(sorted(student_tuples, key=lambda x:x[1]))

# EJERCICIO KEY=LAMBDA
class User:
    def __init__(self, name: str, age: int):
        self.name=name
        self.age=age

    def __repr__(self): # haces un return de como quieres que se imprima lo que tu quieras
        return f"User('{self.name}, {self.age})"    #f"" para poner variables dentro de un string

user_list = [User('john', 47), User('peter', 33), User('mary', 10)]
print(sorted(user_list, key=lambda x:x.age)) #accedes a la lista en función de x


# RECURSIÓN
# función que se llama a sí misma dentro de la función
def factorial(n):
    if n==1:
        return 1
    else:
        resultado = n * factorial(n-1)
        return resultado

print(factorial(5))

# HIGHER ORDER FUNTION OBJECT - FUNCIONES DE ORDEN SUPERIOR
# puedes pasar las funciones como parámetros

def apply(x, function):
    result = function(x) # retorna la función que le has pasado de la x que le has pasado
    return result

def mult(y):
    return y*10.0

print(apply(5, mult)) # le pasas la función directamente

def make_function():
    #x =int(input("Introduzca primer número a sumar:\n"))
    #y = int(input("Introduzca segundo número a sumar:\n"))
    def adder(x,y):
        return x+y
    return adder(1,2)   # le pasas el parámetro dentro (cuando la "llamas")

print(make_function())


# EJERICICIO ORDEN SUPERIOR
def update_inventory(x, add_one, mult_by_two):
    result_add = add_one(x)
    result_mult = mult_by_two(result_add)
    return result_mult

def add_one(x):
    for key, value in x.items():
        x[key] = value + 1
    print(x)
    return x

def mult_by_two(x):
    for key, value in x.items():
        x[key] = value * 2
    return x

input_inventory={
    "ham":2,
    "cheese":3,
    "milk":5
}

print(update_inventory(input_inventory, add_one, mult_by_two))

# PARTIAL EXAMPLE
from functools import partial
def multiply(a,b):
    return a * b

# partial llama a una función y la almacena en otra, poniendo un parámetro de base
# double->duplicas la función con el primer parámetro constante (no afecta a multiply)
double = partial(multiply, 2)   # el primer parámetro de multiply va a ser 2 y será constante
doubled = double(3)     # aquí, estás pasando b en multiply
print(doubled)


# EJERCICIO USING_PARTIAL
def euclid(x1, y1, x2, y2):
    return (x1**2-y1**2)+(x2**2-y2**2)
#importamos partial (from functools import partial)
partial_euclid = partial(euclid, 2, 3)
# n = int(input("Introduzca x2:\n"))
# m = int(input("Introduzca y2:\n"))
print(partial_euclid(1,2))
# partial_euclid_2 = partial_euclid(n,m)
# print(partial_euclid_2)


# DECORADORES
# Es una función x que añadade un acción diferente a otra función y
# sin necesidad de reescribir la función (y) a la que se va a llamar.
# Para poder hacer esto hay que meter un inner en la función decoradora.

# 1. pasa de las funciones de primeras porque no se les llama.
def div(func):      # 4. le pasas la función elev
    def inner(x):   # 5. le pasas el cinco de la llamada a la función elev
        x = x/2     # 6. operamos
        func(x)     # 7. llamamos a elev (que es = func) con el 2,5

    return inner

# 3. cuando llamamos a elev, primero nos encontramos a div
@div
def elev(x):
    print("FUNCIÓN ELEV:")
    return print(x**2)  # 8. se va a elev y devuelve la operación con x = 2,5

# 2. llamamos a elev
elev(5)


from typing import Callable
# EJEMPLO DECORADORES
# función que comprueba si son enteros y los devuelve multiplicados en caso de no error
def logged(func: Callable) -> Callable:
    def inner(x, y):
        print('calling ', func.__name__)    # llamando a (nombre de la función que le pasas)
        assert isinstance(x, int)           # compruebas si son enteros
        assert isinstance(y, int)
        func(x, y)
        print('called ', func.__name__)
    return inner

@logged
def multiplication(x: int, y: int):
    return x * y

multiplication(4, 4)



