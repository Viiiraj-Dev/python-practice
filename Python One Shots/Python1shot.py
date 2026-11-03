# #Print Output
# print("Hello World!")
# print("Vir Raj")
# print("Hi", "Vir")

# # Variables & Types
# name = "Viraj"
# age = 23
# cgpa = 8.6
# is_student = True
# print(name, age)

# print(type(name))
# print(type(age))
# print(type(cgpa))
# print(type(is_student))

# # Input
# name = input("Enter your name: ")
# print("Hello", name)
# print("Hello " + name) # String concatenation

# Single Line Comment

# # Exercise 1
# first_name = "Tony"
# last_name = "Stark"
# age = 53
# height = 1.85

# print ("Full Name", first_name + " " + last_name)
# print (first_name + "'s age is", age)
# print (last_name + "'s height is", str(height) + "m")

# superhero_name = input("Enter your Superhero name: ")
# print("SuperHero Name is:", superhero_name)


# # Type Conversion & Type Casting
# age = input("Enter your age: ")
# print(age, type(age))
# #Type Casing - Done by Porgrammer -> explicit
# new_age = int(age) + 1
# print(new_age, type(new_age))
# # Type Conversion - Done by interpreter Automatically  -> implicit
# print(1 + 2.5)

# # Sum Program
# a = input("Enter 1st Number: ")
# b = input("Enter 2nd Number: ")
# sum = int(a) + int(b)
# print("Sum of", a, "+", b , "is:", sum)

# # Strings
# name = "Tony Stark"
# #String operations
# print(name.upper())
# print(name) # Strings are immutable
# print(name.lower())
# print(name.find("ark")) # returns firat index where string is found
# print(name.find('T'))
# print(name.find('X')) # returns -1 if not found
# print(name.replace("Tony Stark", "Iron Man"))
# print('S' in name)
# print('s' in name)

# # Exercise 2
# price1 = float(input("Enter Price 1:"))
# price2 = float(input("Enter Price 2:"))
# price3 = float(input("Enter Price 3:"))
# sum = price1 + price2 + price3

# print("Total Bill Amount: ", sum)
# print("Average Price: ", (sum/3))

# superhero_name = input("Enter SuperHeroName: ")
# print("Starts with S?:", superhero_name.startswith('S'))

# #Arithematic Operator
# print(5+3)
# print(5-3)
# print(5*3)
# print(5/3)
# print(5//3)
# print(5%3)
# print(5**3)

# # Assigment Operator
# cgpa = 8.7
# x =1
# x +=5
# print(x)
# x-=4
# print(x)
# x*=2
# print(x)
# x/=4
# print(x)

# # Operator Precedence
# #()  >  *,/  >  +,-
# # Same precedance -> operates from left to right
# ans = 2+5 * 3
# print(ans)
# ans = (2+5)*3
# print(ans)

# # Comparison Operators
# print(3>2)
# print(3<2)
# print(5>=3)
# print(5<=3)
# print(2==2)
# print(2!=2)

# # Logical Operators
# stt1 = 2 > 3
# stt2 = 5 > 2
# print(stt1 or stt2)
# print(stt1 and stt2)
# print(not stt1)

# # Conditional Statement
# age = 24

# if age>=18:
#     print("You are an Adult")
#     print("You can drive/vote")
# elif age<18:
#     print("You can't vote or drive")

# marks = 89
# if marks>=80:
#     print("Grade A")
# elif marks>=60 and marks<=80:
#     print("Grade B")
# else:
#     print("Grade C")

# # Exercise 3 - Calculator
# num1 = float(input("Enter 1st Number: "))
# num2 = float(input("Enter 2nd Number: "))
# opr = input("Enter Operation to Perform (+,-,*,/,%,**): ")

# if opr=='+':
#     print("Addition: " , (num1+num2))
# elif opr=='-':
#     print("Subtraction: " , (num1-num2))
# elif opr=='*':
#     print("Multiply: " , (num1*num2))
# elif opr=='/':
#     print("Divide: " , (num1/num2))
# elif opr=='%':
#     print("Remainder: " , (num1%num2))
# elif opr=='**':
#     print("Power: " , (num1**num2))
# else:
#     print("Invalid Operator")


# # Range -> range(n) = [0, 1, 2, ... , n-1]
# nums = range(5)
# print(nums)

# nums2 = range(1, 6) # 1,2,3,4,5
# #range(start, stop, step)


# Loops

# #while
# i=0
# while i<5:
#     print("Shri Ram")
#     i+=1
# j=0
# while j<5:
#     print("*"*j)
#     j+=1

# while j>0:
#     print("*"*j)
#     j-=1

#For Loop
# for i in range(5):
#     print(i)

# for i in range(1, 11):
#     if(i%2==0):
#         print(i)

# for i in range(2, 11, 2):
#     print(i)


# for i in range(3, 50, 3):
#     if(i==21):
#         break
#     print(i)

# for i in range(3, 50, 3):
#     if(i==21):
#         continue
#     print(i)


# # Exercise 4

# #print all odd numbers from 1 to 20
# for i in range(1, 21):
#     if (i%2==1):
#         print(i)

# # print table of 57
# for i in range(1, 11):
#     print("57 X", i , "=", 57*i)

# # Take 2 integers a, b as input, Find and print fisrt number between 1 and 1000 that is divisible by 
# #both numbers
# a = int(input("Enter 1st Number: "))
# b = int(input("Enter 2nd Number: "))

# for i in range(1, 1001):
#     if i%a==0 and i%b==0:
#         print(i)
#         break


# # List - Collection of different items - Mutable

# marks = [98, 99, 97, 95, 93, 'A', 92.5]
# print(marks, type(marks))

# print(len(marks))
# print(marks[0])
# print(marks[2])
# print(marks[-1])
# print(marks[-2])

# #Slicing List - list[start:stop]
# print(marks[0:3])
# print(marks[-3:])
# print(marks[:2])

# for score in marks:
#     print(score)

# marks.append(50)
# print(marks)
# marks.insert(1, 55)
# print(marks)
# print(97 in marks)
# print(100 in marks)

# marks.clear()
# print(marks, len(marks))

# #Tuple - Immutable
# marks = (98, 99, 97, 95, 93, 95, 95)
# print(marks, type(marks))
# print(marks[2])
# print(marks.count(95))
# print(marks.index(95))


# # Sets - Unique collection of items
# marks = {98, 97, 95, 96, 95, 96}
# print(marks, len(marks))
# for score in marks:
#     print(score)

# #Dictionary - key => value

# marks = {"Math": 99, "Physics": 97, "Chemistry": 98}
# print(marks, type(marks))
# print(marks["Physics"])

# marks["Physics"] = 95
# print(marks["Physics"])
# marks["English"] = 88
# print(marks)

# for key in marks:
#     print(key, marks[key])


# # Exercise 5
# # Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll number

# marks_list = [101, 105, 102, 101, 108, 105, 110]
# marks_set = set(marks_list)
# print(marks_set)

# employees = [
#     (101, "Alice", 50000),
#     (102, "Bob", 65000),
#     (103, "Charlue", 45000)
# ]

# num = int(input("Enter Employee ID to get Details: "))

# for i in range(len(employees)):
#     if employees[i][0] == num:
#         print("Name:", employees[i][1], "Salary:", employees[i][2])


# # Functions
# def sum(a, b):
#     print(a+b)

# sum(2, 3)
# sum(5, 4)

# def calculate_gst(price):
#     new_price = price + price*0.18
#     print(new_price)

# calculate_gst(100)
# calculate_gst(200)

# def calculate_gst(price):
#     new_price = price + price*0.18
#     return new_price

# n1 = calculate_gst(111)
# print(n1)
# n2 = calculate_gst(234)
# print(n2)


# import math as m
# print(dir(m))

# print(m.sqrt(9))

# import random
# print(random.random()) # 0 to 1 

# # Exercise
# def odd_even(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")

# odd_even(2)
# odd_even(1)
# odd_even(9)
# odd_even(4)

# def num_of_vowels(st):
#     st = str(st).lower()
#     print("Number of vowels:", (st.count('a') + st.count('e') + st.count('i')+ st.count('o')+ st.count('u')))

# num_of_vowels("Viraj")

# def is_prime(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2, int(n**0.5)+1):
#             if n%i == 0:
#                 return False
#     return True

# print(is_prime(2))

# def avg(marks):
#     print("Average:" , (sum(marks)/len(marks)))

# avg([98, 99, 100])


import random as r

num = r.randint(1, 50)
n= 0
while (num != n):
    n = int(input("Enter your lucky number (1-50): "))
    if(n>num):
        print("Your guess is high")
    else:
        print("Your guess is low")

print("Yay!! you guessed your Lucky Number")