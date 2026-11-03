## class, object and __init__
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return f"{self.name} says woof!"

# d1 = Dog("Bruno", 3)
# d2 = Dog("Tommy", 5)
# print(d1.bark())
# print(d2.name)


# # Class Attributes vs Instance Attributes
# class Dog:
#     species = "Canis Familiaris"

#     def __init__(self, name):
#         self.name = name

# print(Dog.species)


# # Methods that change state
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <=0:
#             raise ValueError("Deposit must be positive")
#         self.balance+=amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         self.balance-=amount

# acc = BankAccount("Vir", 1000)
# acc.deposit(500)
# print(acc.balance)


# # __str__ : control how an object prints
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Dog({self.name})"

# print(Dog("Bruno"))


"""
Exercise 1: Create a Rectangle class with width and height. Add methods area() and perimeter(), and a __str__ that prints something 
like Rectangle(4 x 5). Create two rectangles and print them with their areas.

Exercise 2: Build a BankAccount class with deposit, withdraw and a __str__ as shown above. Then write a short script that creates an 
account, deposits, withdraws too much inside a try/except ValueError, and prints the final balance.

Exercise 3: Create a Student class with name and a marks list. Add add_mark(mark) and average() methods. average() should return 0 if 
there are no marks, so it doesn’t divide by zero. Create a student, add 3 marks and print the average.
"""

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print(f"Area: {self.l*self.w}")

    def perimeter(self):
        print(f"Perimeter: {2*(self.l + self.w)}")

    def __str__(self):
        return f"Rectangle({self.l} X {self.w})"

r1 = Rectangle(4, 5)
r1.area()
print(r1)
r2 = Rectangle(6, 8)
r2.area()
print(r2)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Holder: {self.owner}, Balance: {self.balance}"

    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Deposit Amount Should be positive")
        self.balance+=amount

    def withdraw(self, amount):
        if amount>self.balance:
            raise ValueError("Insufficient Balance")
        self.balance-=amount

acc = BankAccount("Raj", 1000)

try:
    acc.deposit(500)
    acc.withdraw(300)
    print(acc)
except ValueError as e:
    print(e)


class Student:
    def __init__(self, name, marks=None):
        self.name = name
        if marks == None:
            self.marks = []
        else:
            self.marks= marks

    def add_marks(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks)/len(self.marks)

s1 = Student("Vir")
s1.add_marks(97)
s1.add_marks(85)
s1.add_marks(96)
print(s1.average())
        