#del keyword - Used to delete object properties or object itself

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Raj")
# # print(s1)
# # del s1
# # print(s1)
# print(s1.name)
# del s1.name
# print(s1.name)


# # Private(like) attributes & methods - Conceptual Implementation
# # Private Attributes & methods are meant to be used only within the class and are not accessible from outside the class
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass) # Can access inside class

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# #print(acc1.__acc_pass) # Cannot access outside class
# acc1.reset_pass()

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello Person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# #p1.__hello() # Gives error as not accessible out side class
# p1.welcome()



# Inheritance - 
# When one class(child/derived) derives the properties & methods of another class(parent/base)

# # Single Level
# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# # Multilevel Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.brand)
# car1.start()

# # Multiple Inheritance
# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


# # Super method - super() method is used to access methods of the parent class
# class Car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.brand = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("Prius", "Electric")
# print(car1.type)


# # Class Method - A class method is bound to the class & recieves the class as an implicit first argument
# # Note - static method can't access or modify class state & generally for utility
# class Person:
#     name = "Anonymous" # class attribute
    
#     # def changeName(self, name):
#     #     self.name = name # creates new name for object
#     #     # self.__class__.name = name
#     #     # Person.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)


# # Property - We use @property decorator on any method in the class to use the method as a property
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
#         #percentage
    
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"


# s1 = Student(97, 98, 99)
# print(s1.percentage)

# s1.phy = 95
# print(s1.phy)
# print(s1.percentage)


# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

# print(1+2)
# print("apna" + "college")
# print([1,2,3] + [4,5,6])

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img,"j")

#     def add(self, num1):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2):
#             newReal = self.real - num2.real
#             newImg = self.img - num2.img
#             return Complex(newReal, newImg)
        

# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

# num4 = num3+num2
# num4.showNumber()

# num5 = num4 - num1
# num5.showNumber()


#Exercise 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area: ", (3.14*self.radius*self.radius) ) 

    def perimeter(self):
        print("Perimeter: ", (2*3.14*self.radius))

c1 = Circle(2)
c1.area()
c1.perimeter()

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Department:", self.dept, "Role:", self.role, "Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, r, d, s):
        self.name = name
        self.age = age
        super().__init__(r,d,s)

    def showEmpDetails(self):
        super().showDetails()
        print("Name:", self.name, "Age:", self.age)

e1 = Engineer("Vir", 23, "Developer", "RefData", 15000)
e1.showEmpDetails()


#Exercise 2
class Order:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    def __gt__(self, o2):
        if(self.price>o2.price):
            return True
        else:
            return False

o1 = Order("Apple", 101)
o2 = Order("Orange", 205)
print("Apple costlier then Orange? ", o1>o2)