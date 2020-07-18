# class Hello:
#     # __init__ method is the constructor
#     def __init__(self, name="MS Dhoni"):
#         self.name = name
#
#     def greeting(self):
#         print("Hello, %s" % self.name)
#
#
# sajjad = Hello("Sajjad Zahir")
# sunil = Hello("Sunil")
# default = Hello()
#
# sajjad.greeting()
# sunil.greeting()
# default.greeting()


#(2) CODE


# class Student:
#     def __init__(self, name, sid, age):
#         self.name = name;
#         self.sid = sid;
#         self.age = age
#
#
# s = Student("Sajjad", 1001, 34)
# # prints the attribute name of the object s
# print(getattr(s, 'name'))
# #reset the value of attribute age to 23
# setattr(s, "age", 23)
# # prints the modified value of age
# print(getattr(s, 'age'))
# #prints true if the student contains the attribute with name id
# print(hasattr(s, 'sid'))
# # deletes the attribute age
# delattr(s, 'age')
# # this will give an error since the attribute age has been deleted
# print(s.age)


#(3) CODE

#Class and Instance level Variable
# class Shark:
#     # Class variables
#     animal_type = "fish"
#     location = "ocean"
#
#     # Constructor method with instance variables name and age
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # Method with instance variable followers
#     def set_followers(self, followers):
#         print("This user has " + str(followers) + " followers")
#
#
# ts = Shark("test", 23)
# print(Shark.animal_type)
# print(Shark.location)
# print(ts.location)
# print(ts.name)
# print(ts.age)
# print("****************")
# es = Shark("test1", 33)
# print(Shark.animal_type)
# print(Shark.location)
# print(es.name)
# print(es.age)

# (4) CODE

# class Person:
#     '''Represents a person.'''
#     population = 0
#
#     def __init__(self, name):
#         '''Initializes the person's data.'''
#         self.name = name
#         print('(Initializing %s)' % self.name)
#         Person.population += 1
#
#     def __del__(self):
#         '''I am dying.'''
#         print('%s says bye.' % self.name)
#         Person.population -= 1
#         if Person.population == 0:
#             print('I am the last one.')
#         else:
#             print('There are still %d people left.' % Person.population)
#
#     def sayHi(self):
#         print('Hi, my name is %s.' % self.name)
#
#     def howMany(self):
#         if Person.population == 1:
#             print('I am the only person here.')
#         else:
#             print('We have %d persons here.' % Person.population)
#
#
# Sajjad = Person('Sajjad')
# Sajjad.sayHi()
# Sajjad.howMany()
#
# Ajit = Person('Ajit')
# Ajit.sayHi()
# Ajit.howMany()
#
# Sajjad.sayHi()
# Sajjad.howMany()

# (5) CODE

# from datetime import date as dt
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def isAdult(age):
#         if age > 18:
#             return True
#         else:
#             return False
#
#     @classmethod
#     def emp_from_year(emp_class, name, year):
#         return emp_class(name, dt.today().year - year)
#
#     def __str__(self):
#         return 'Employee Name: {} and Age: {}'.format(self.name, self.age)
#
# e1 = Employee('Ram', 25)
# print(e1)
# e2 = Employee.emp_from_year('Ajit', 1987)
# print(e2)
# print(Employee.isAdult(25))

# (6) CODE

# Instance Method Example
# class DecoratorExample:
#     """ Example Class """
#
#     def __init__(self):
#         """ Example Setup """
#         print('Hello, World!')
#         self.name = 'Decorator_Example'
#
#     # Instance methods must have self as a parameter. self is not a keyword
#     def example_function(self):
#         # def example_function(x):
#         """ This method is an instance method! """
#         print('I\'m an instance method!')
#         print('My name is ' + self.name)
#         # print('My name is ' + x.name)
# de = DecoratorExample()
# de.example_function()

# (7) CODE

# class TestClass:
#
#     @staticmethod
#     def StaticMethod():
#         print("static")
#
#     def __init__(self):
#         print("constructor")
#
#     def __del__(self):
#         print("destructor")
#
#
# if __name__ == "__main__":
#     obj = TestClass()
#     # the following both are ok.
#     TestClass.StaticMethod()  # Static Method called by Class Name
#     obj.StaticMethod()  # Static Method called by Object Name
#     del obj

# (8) CODE

# class methodoverload:
#     def product(self, a, b):
#         self.p = a * b
#         print(self.p)
#
#     def product(self, a, b, c):
#         self.p = a * b * c
#         print(self.p)
#
# x = methodoverload()
# # x.product(4, 5)
# x.product(4, 5, 5)

# (9) CODE

# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print('Hello ' + name)
#         else:
#             print('Hello ')
# # Create instance
# obj = Human()
# # Call the method
# obj.sayHello()
# # Call the method with a parameter
# obj.sayHello('Infosys')
# # Here Both call will work

# (10) CODE

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     pass
#
# x = Student("Sajjad", "Zahir")
# print(Student.__mro__)
# x.printname()

# (10) CODE

# class Person:
#     def __init__(self, fname, lname):
#         print("Inside Parent init")
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self, fname, lname, age):
#         print("Inside Student init")
#         Person.__init__(self, fname, lname)
#         # Invoking parent class __init__
#         self.age = age
#
# x = Student("Sajjad", "Zahir", 30)
# x.printname()

# (11) CODE

# class Calculation1:
#     def Summation(self, a, b):
#         return a + b
#
# class Calculation2:
#     def Multiplication(self, a, b):
#         return a * b
#
# class Derived(Calculation1, Calculation2):
#     def Divide(self, a, b):
#         return a / b
#
# d = Derived()
# print(d.Summation(10, 20))
# print(d.Multiplication(10, 20))
# print(d.Divide(10, 20))

# (12) CODE

# class Person:
#     def __init__(self, fname, lname):
#         print("Inside Parent init")
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self, fname, lname,age):
#         print("Inside Student init")
#         Person.__init__(self, fname, lname) #Invoking parent class __init__
#         self.age=age
#
#
# x = Student("Sajjad", "Zahir",30)
# x.printname()

# (13) CODE

#use of super()

# class Person:
#     def __init__(self, fname, lname):
#         print("Inside Parent init")
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self, fname, lname,age):
#         print("Inside Student init")
#         super().__init__(fname, lname) #Invoking parent class __init__
#         #Add Properties
#         self.age=age
#
#
# x = Student("Sajjad", "Zahir",30)
# x.printname()

# (14) CODE

# class A(object):
#     def dothis(self):
#         print('From A class')
#
# class B1(A):
#     def dothis(self):
#         print('From B1 class')
#     pass
#
# class B3(A):
#     def dothis(self):
#         print('From B3 class')
#
# # Diamond inheritance
# class D1(B1, B3):
#     pass
#
# print("for D1 Instance")
# d1_instance = D1()
# d1_instance.dothis()
# print(D1.__mro__)

# (15) CODE

# class A():
#
#     def __init__(self):
#         self.__priv = "I am private from Main"
#         self._prot = "I am protected from Main"
#         self.pub = "I am public from Main"
#
#
# # from attribute_tests import A
# x = A()
# print(x.pub)
# x.pub = x.pub + " and my value can be changed"
# print(x.pub)
# # print(x.prot)
# print(x._prot)
# # print(x.__priv)

