# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says woof"

d = Dog("Bruno", "Labrador")
print(d.speak())
print(d.name)


# Polymorphism
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"

for pet in [Dog("Bruno", "Lab"), Cat("Misty")]:
    print(pet.speak())

# isinstance and issubclass
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(issubclass(Dog, Animal))


# Special (dunder) methods
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"₹{self.amount}"

    def __repr__(self):
        return f"Money({self.amount})"

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __len__(self):
        return self.amount

print(Money(50) + Money(30))
print(Money(5)==Money(5))


# @classmethod, @staticmethod, @property
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return self.PI * self._radius ** 2

    @classmethod
    def from_diameter(cls, d):
        return cls(d/2)

    @staticmethod
    def is_valid_radius(r):
        return r>0

c = Circle.from_diameter(10)
print(c.area)

"""
Exercise 1: Create a Shape parent class with an area() method that raises NotImplementedError. Create Circle and Rectangle 
children that override area() and return the value. Put one of each in a list and loop through it, printing each area. 
(This is polymorphism.)

Exercise 2: Extend your BankAccount into SavingsAccount(BankAccount):

add an interest_rate using super().__init__
add add_interest(), which deposits balance * interest_rate
override withdraw so a savings account can’t go below a minimum balance of 500

Test the successful path and the failure path.

Exercise 3: Create a Vector class with x and y. Implement __str__, __add__ (returns a new Vector), and __eq__. Verify that Vector(1, 2) + Vector(3, 4) prints Vector(4, 6) and that Vector(1, 2) == Vector(1, 2) is True.
"""

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return f"Area of Circle: {3.14159 * self.r ** 2}"

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return f"Area of Rectangle: {self.l*self.w}"

for s in [Circle(2), Rectangle(4, 6)]:
    print(s.area())

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

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.interest_rate = 0.025

    def add_interest(self):
        self.deposit(self.interest_rate*self.balance)

    def withdraw(self, amount):
        if self.balance-amount<500:
            raise ValueError("Savings account can’t go below a minimum balance of 500")
        self.balance-=amount


""""
Exercise 3: Create a Vector class with x and y. Implement __str__, __add__ (returns a new Vector), and __eq__. 
Verify that Vector(1, 2) + Vector(3, 4) prints Vector(4, 6) and that Vector(1, 2) == Vector(1, 2) is True.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x+other.x , self.y+other.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

print(Vector(1, 2) + Vector(3, 4))
print(Vector(1, 2) == Vector(1, 2))