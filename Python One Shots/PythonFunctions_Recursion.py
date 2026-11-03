# Functions in Python
# Block of statements that perform a specific task.

# #Function Definition
# def calc_sum(a, b): # parameters
#     return a+b

# print(calc_sum(1, 2)) # function call; arguments
# print(calc_sum(4, 5))

# def print_hello():
#     print("Hello")

# print_hello()

# print(print_hello()) # If any function returns nothing, then print for it returns None

# # average of 3 numbers
# def calc_avg(a, b, c):
#     print("Average of", a, b, c, "is:", (a+b+c)/3)

# calc_avg(1,2,3)
# calc_avg(94, 95, 96)

# # Types of Functions in Python - Built in Function, User Defined Function
# print("apnacollege", end = " ") # sep = " "
# print("shraddhakhapra") # end = "\n"


# # Default Parameter - Assigning a default value to parameter, which is used when no argument is passed
# def cal_prod(a=1, b=1): 
#     print(a*b)

# cal_prod()
# cal_prod(4,2)
# cal_prod(4)

# # def cal_prod(a=1, b) # Error - Default values are set from right, always from last
# # def cal_prod(a, b=1) # Valid 

# # Practice
# def calc_length(lst):
#     len = 0
#     for i in lst:
#         len+=1
#     print("Length:", len)

# calc_length([1,2,3])
# calc_length([5,6,7,8,9])

# def print_list(lst):
#     print("List: [",   end = " ")
#     for i in lst:
#         print(i, end = " ")
#     print("]")

# print_list([5,6,7,8,9])

# def factorial(n):
#     fact=1
#     while n>=1:
#         fact*=n
#         n-=1
#     print("Factorial:", fact)
    
# factorial(5)
# factorial(4)

# def usd_to_inr(rs):
#     print("USD:", rs, " =  INR:", rs*94.85)

# usd_to_inr(2)
# usd_to_inr(10)

# def odd_even(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")

# odd_even(2)
# odd_even(5)
# odd_even(8)


# # Recursion: When a function calls itself repeatedly
# def show(n):
#     if(n==0): # Base case
#         return
#     print(n)
#     show(n-1)

# show(5)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))
# print(factorial(4))
# print(factorial(3))


# Practice
def print_sum(n):
    if n==0:
        return 0
    return n+print_sum(n-1)

print(print_sum(5))
print(print_sum(3))
print(print_sum(10))

def print_list(lst, idx):
    if idx==len(lst):
        return
    print(lst[idx])
    print_list(lst, idx+1)

print_list([1,2,3,4], 0)
