# # Class - blueprint for creating objects
# class Student:
#     name = "karan"

# # Object - Instance of a Class
# s1 = Student()
# print(s1)
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# Constructor -> __init__() function -> All classes have a function called __init__(), which is always executed when the object is being initiated
# class Student:
#     name = "karan"
#     def __init__(self):  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
#         print(self)
#         print("Adding new student in Database...")

# s1 = Student()
# print(s1.name)
# print(s1)

# #Class Attribute & Instance Attributes
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("Adding new student in Database...")

# s1 = Student("Raj")
# print(s1.name)

# s2 = Student("Vir")
# print(s2.name)

## Methods
# class Student:
#     college = "ABC College" # Class Attribute
#     # Default Constructors
#     def __init__(self):
#         pass

#     # Parameterized Constructors
#     def __init__(self, name, marks):
#         self.name = name   # Instance Attribute
#         self.marks = marks

#     # Methods
#     def welcome(self):
#         print("Welcome Student")

#     def get_marks(self):
#         return self.marks

# s1 = Student("Karan", 97)
# print(s1.name, s1.marks)
# print(s1.college)
# print(Student.college)
# s1.welcome()
# print(s1.get_marks())

# ## Exercise 1
# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name =name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3

#     def avg_marks(self):
#         return (self.marks1+ self.marks2+ self.marks3)/3

# s1 = Student("Raj", 98, 99, 100)
# print(s1.avg_marks())

# ## Static Methods - Methods that don't use the self parameter (work at class level)
# class Student:
#     @staticmethod
#     def college():
#         print("ABC College")

#     def __init__(self, name, marks1, marks2, marks3):
#         self.name =name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3

#     def avg_marks(self):
#         return (self.marks1+ self.marks2+ self.marks3)/3

# s1 = Student("Raj", 98, 99, 100)
# print(s1.avg_marks())
# s1.college()

# #Abstraction - Hiding the implementation details of a class and only showing the essential features to the user
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started..")

# car1 = Car()
# car1.start()

# #Encapsulation - Wrapping data and realted functions into a single unit (object)

# Exercise 2
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amt):
        self.balance = self.balance - amt
        print("Amount:", amt, "Debited..")

    def credit(self, amt):
        self.balance = self.balance + amt
        print("Amount:", amt, "Credited..")

    def acc_balance(self):
        print("Account No:", self.acc_no, "Account Balance: ", self.balance)

acc1 = Account(10000, 101)
acc1.credit(2000)
acc1.acc_balance()
acc1.debit(4500)
acc1.acc_balance()