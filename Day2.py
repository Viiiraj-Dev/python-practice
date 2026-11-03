"""
Exercise 1: Take user input (name and age as strings using input()), convert age to an integer, then print: "<name> will turn <age+1> next year".

Exercise 2: What does this print, and why? (Answer without running it first, then verify)

python
x = "10"
y = 5
print(x * y)
"""


name = input("Enter your name: ")
age = input("Enter your age: ")

age_num = int(age)

print(name, "will turn" , (age_num+1), "next year")

x = "10"
y=5
print(x*y)