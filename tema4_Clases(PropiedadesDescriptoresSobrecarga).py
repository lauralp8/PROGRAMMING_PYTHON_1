
# crea new_category=None Tipo curso dentro de la clase departamento
class Department:
    def __init__(self, name:str, department_code: str): # init = constructor de la clase
        self.name = name
        self.deparment_code =department_code
        self.courses = {}          # atributo de objeto que no es necesario pasar al llamar a la función

    def add_course(self, course_description: str,   # adds a course to the department
                   course_code: str,
                   n_credits: int) -> 'Course':     # devuelve un objeto de tipo Course Class
        course = Course(course_description, course_code, n_credits,
                        self.deparment_code)        # con self para pasarle el código del departamento que estas
                                                    # creando en ese momento
        self.courses[course.course_code] = course   # añade curso a la lista
        return course

class Course:
    def __init__(self, course_description: str,
                 course_code: str,
                 n_credits: int, department_code: str):
        self.course_description = course_description
        self.course_code = course_code
        self.n_credits = n_credits
        self.department_code = department_code      # código de departamento
        self.classes = set([])                      # set es un conjunto, es como una lista

    def add_class(self, year: int) -> 'CourseClass':
        """ Adds a course class to a course """
        course_class = CourseClass(self, year)
        self.classes.add(course_class)              # añadir un elemento a un set (a un conjunto)
        return course_class

class CourseClass:
    def __init__(self, course: Course, year: int):
        self.course = course
        self.year = year
        self.students = set([])

    def add_student(self, student: 'Student'):
        """
            Adds a student to the class, adding him/her to the set of students
            :param student:     a Student object to be added to the course class
            :return:            None
        """
        self.students.add(student)

Humanidades = Department('Humanidades', '2302')
Humanidades.add_course('Business Analytics', '2302.1', 68)
Humanidades.add_course('ADE', '2302.7', 65)

print(Humanidades.courses)      # printeamos el conjunto

# preguntar, porque se imprime la direccion de memoria y no el nombre del curso

"""
    __name__ the name of the class 
    __module__ the module (or library) from which it was loaded 
    __bases__ a collection of its base classes (inheritance) 
    __dict__ a dictionary (a set of key-value pairs) containing all the attributes (including methods) 
    __doc__ the documentation string.
    For objects: 
        __class__ the name of the class of the object
"""

# cada objeto tiene sus atributos personales
# pero existen atributos de clase (como un contador) que es común para todos

class Person:
    """ Contador = atributo de clase """
    instance_count = 0

    def __init__(self, name: str, age: int):
        Person.instance_count += 1
        self.name = name
        self.age = age

p1 = Person('Lau', 20)
p2 = Person('Carlos', 21)
p3 = Person('Cristina', 45)

print(Person.instance_count)


# @CLASSMETHOD
# función normal que afecta a todos los elementos de la clase
# se usa sobretodo para jugar con los atributos de clase

# MODIFICAR ATRIBUTOS DE CLASE
class Employee:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):  # cls en vez de self, cls llama a atributos de clase
        cls.instance_count += 1

    def __init__(self, name, age):
        """
        Constructor
        :param name:    name of the employee
        :param age:     age
        """
        Employee.increment_instance_count()
        self.name = name
        self.age = age

e1 = Employee('Jason', 36)
print(Employee.instance_count)          # 1
e2 = Employee('Carol', 21)
print(Employee.instance_count)          # 2
# llamas a la función y le puedes sumar 1 sin necesidad de crear un objeto
Employee.increment_instance_count()     # 3
print(Employee.instance_count)


# @STATIC_METHODS
# son funciones que no reciben ni cls ni self
# no juegan con atributos de dentro de la clase, sino con atributos externos
# suelen crear cosas fijas
# cuando no todos los objetos de la clase lo comparten (no todos los círculos tienen el mismo radio)

from math import pi
class Circle:
    def __init__(self, radius: float):
        self.radius =radius

    def properties(self):
        return {'area': Circle.area(self.radius),
                'perimeter': Circle.perimeter(self.radius)}

    @staticmethod
    def area(radius: float):
        return round(pi*radius**2, 2)   # ,2 redondeando a dos decimales

    @staticmethod
    def perimeter(radius: float):
        return round(2*pi*radius, 2)

c = Circle(3)      # le pasas el radio
print(c.properties())


# PROPERTIES
# cuando creas una propiedad creas un:
# propertie con una función con el nombre del atributo y returnesas el self._(nombre)
# si está protegido no se puede llamar desde fuera, sólo se modifica desde la función de dentro (setter)
# setter: asignar valor al atributo protegido
# getter para ver que te devuelve
# deleter: borra el atributo

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self._price = None

    @property
    def price(self):
        return self._price

    @price.setter               # adjudicamos valor
    def price(self, new_price):
        if isinstance(new_price, float) and new_price>0:        # si es un float y > de 0, reasigna el valor
            self._price = new_price
            print("The price has been introduced")
        else:
            print("Please, enter a valid price")

    @price.deleter
    def price(self):        # elimina el valor actual, pero se puede volver a asignar
        del self._price

art1 = Article(9323)
art1.price = 3,89
art2 = Article(9760)
art2.prince = 7

# Añadir un nuevo atributo protegido, que sólo coja uno de los posibles valores:
# ‘book’, ‘electronics’, ‘health’, ‘fashion'
class Articles:
    def __init__(self, id: int, price: int):
        self.id = id
        self.price = price
        self._category = None

    def __str__(self):
        # str transforma el int en una cadena para poder hacer el print
        if self._category != None:  # si existe categoría imprime id, price y category
            return str(self.id) + " " + str(self.price) + " " + self._category
        else:           # si no, imprime id y price
            return str(self.id) + " " + str(self.price)

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, new_category):
        # para que valga en cualquier formato, pasamos todas las letras a min
        new_category = new_category.lower()
        if new_category == 'book' or \
                new_category == 'electronics' or \
                new_category == 'health' or \
                new_category == 'fashion':
            self._category = new_category
            print("The category has been changed")
        else:
            print("Please, enter a correct category")


x = Articles(2355, 2)
print(x)
# x.category = str(input('Introduzca la categoria\n'))


# SOBRECARGA // OVERLOAD
# funciones ya creadas que cuando pones su operador llama automáticamente a esa función
# add, sub, mult, pow, truediv(div), lt, le, eq, ne, gt, ge
# cada clase tiene su operador
# siempre va a tener (self, other)

UNIT_WEIGHT_PEARS = 0.2
UNIT_WEIGHT_ORANGES = 0.3

class Stock:
    def __init__(self, pears, oranges):
        self.pears = pears
        self.oranges = oranges

    def __add__(self, other):
        total_pears = self.pears + other.pears
        total_oranges = self.oranges + other.oranges
        return Stock(total_pears, total_oranges)


    def __lt__(self, other):    # comprueba que pedido es menor (si stock1 o stock2)
        return ((self.pears * UNIT_WEIGHT_PEARS + self.oranges *
                 UNIT_WEIGHT_ORANGES) <
                (other.pears * UNIT_WEIGHT_PEARS + other.oranges *
                 UNIT_WEIGHT_ORANGES))

    # para que lo imprima
    def __str__(self):
        return "Pears: " + str(self.pears) + " Oranges: " + str(self.oranges)

stock_1 = Stock(pears=3, oranges=3)
stock_2 = Stock(pears=5, oranges=2)
stock_3 = stock_1 + stock_2
print(stock_3)
print(stock_1<stock_2)

# comprueba si un número complejo es igual a un imaginario
class Complex:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        return (self.real == other.real and self.imag == other.imag)

a = Complex(1,2)
b = Complex(3,4)
c = Complex(1,2)

print(a==b)
print(a==c)







