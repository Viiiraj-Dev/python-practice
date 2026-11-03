# # Decorators - gift wrapping for a function
# def say_hello():
#     print("Hello")

# def decorator(func):  # takes a function in
#     def wrapper():
#         print("Before")
#         func()      # runs the original function
#         print("after")
#     return wrapper  # gives back the wrapped version

# @decorator    # this one line applies the wrapper
# def say_hello():
#     print("Hello!")

# say_hello()


# # Handling functions with arguments
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         result = func(*args, **kwargs)
#         print("After")
#         return result
#     return wrapper

# @decorator
# def sum(a,b):
#     return a+b

# print(sum(2,3))


# # Generators = one item at a time
# def count_up(n):
#     for i in range(1, n+1):
#         yield i

# for x in count_up(3):
#     print(x)


# # Exercise 1
# def log_calls(func):
#     def wrapper(*args, **kwargs):
#         print("Calling", func.__name__)
#         result=func(*args, **kwargs)
#         print("Done")
#         return result
#     return wrapper

# @log_calls
# def add(a,b):
#     return a+b

# print(add(2,3))

# # Exercise 2
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a , b = b, a+b

# print(list(fibonacci(10)))


# Optional Task

def read_txt(fl):
    with open(fl, 'r') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            else:
                yield line

for text in read_txt("Day12txt.txt"):
    print(text)


