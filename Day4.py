"""
🏋️ Exercises

Exercise 1: Predict output first, then verify:

python
print(bool(""))
print(bool("False"))
print(bool([]))
print(bool([False]))

Exercise 2: Write a one-liner that checks if a number n is between 10 and 20 (inclusive) using a chained comparison, and prints True/False. Test it with n = 15 and n = 25.
"""

print(bool("")) # False
print(bool("False")) # True
print(bool([])) # False
print(bool([False])) # True

n1 = 15
print(10 <= n1 <=20)
n2 = 25
print(10 <= n2 <= 20)