# Functions 
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Vir"))
print(greet("Vir", greeting="Hi"))

# Returning multiple values(it's really a tuple)
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([4, 2, 9])
print(low, high)

# *args and **kwargs
def total(*args): # any number of positional args -> tuple
    return sum(args)

def show(**kwargs): # any number of keyword args -> dict
    for k, v in kwargs.items():
        print(k, v)

total(1, 2, 3)
show(name="Vir", age = 25)

# Lambda (tiny one-line functions)
square = lambda x: x*x
print(square(5))
people = [("A", 30), ("B", 25)]
people.sort(key=lambda p:p[1]) # sort by age
print(people)


# Comprehensions (very Pythonic)
squares = [x*x for x in range(5)]
print(squares)
evens = [x for x in range(10) if x%2 == 0]
print(evens)
lengths = {w: len(w) for w in ["hi", "hello"]}
print(lengths)
unique_lens = {len(w) for w in ["hi", "yo", "hey"]}
print(unique_lens)



# Mutable default argument trap
# def add(item, items=[]): # the same list is reused across calls
#     items.append(item)
#     return items

# add(1)
# add(2)
# add(3)
# print(add(4))

def add(item, items=None): # the same list is reused across calls
    if items is None:
        items = []
    items.append(item)
    return items

add(1)
add(2)
add(3)
print(add(4))

n = [2,3,4]
add(1, n)
print(n)
add(2)
add(3)
print(add(4))


"""
Exercise 1: Write a function is_even(n) that returns True or False. Then use a list comprehension and is_even to build a list of the even numbers from 1 to 20.

Exercise 2: Write a function word_count(text) that returns the dictionary from yesterday’s Exercise 1, 
Exercise 3: Write a function stats(*nums) that accepts any number of numbers and returns (minimum, maximum, average). Call it as stats(4, 8, 15, 16, 23, 42) and unpack the result into three variables.
"""

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

evn_lst = [x for x in range(1,20) if is_even(x)]
print(evn_lst)

def word_count(text):
    lst=text.split()
    dct = {}
    for i in lst:
        dct[i] = dct.get(i, 0) + 1
        
    return dct

text = "the quick brown fox jumps over the lazy dog the end"
print(word_count(text))

def stats(*args):
    return min(args), max(args), sum(args)/len(args)

a , b, c = stats(4, 8, 15, 16, 23, 42)

print(a, b, c)