"""
Exercise 1: Given nums = [4, 2, 9, 1, 5], without using .sort(), write code to find and print the largest and smallest values using only built-in functions (max(), min()).

Exercise 2: Predict the output first, then verify:

python
a = [1, 2, 3]
b = a
c = a.copy()

b.append(4)
c.append(5)

print(a)
print(b)
print(c)
"""

nums = [4, 2, 9, 1, 5]
print(max(nums))
print(min(nums))

a = [1, 2, 3]
b = a
c = a.copy()

b.append(4) # [1, 2, 3, 4]
c.append(5) # [1, 2, 3, 5]

print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4]
print(c) # [1, 2, 3, 5]

# Part 3
n = int(input("Enter the Number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
