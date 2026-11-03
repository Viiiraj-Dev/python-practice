"""
Exercise 1: Given sentence = "  Python is Fun and Powerful  ", write code to: strip the whitespace, convert to lowercase, then print only the word "powerful" using slicing (not .split()).

Exercise 2: Predict the output first, then verify:

python
name = "Developer"
print(name[1:5])
print(name[-4:])
print(name[::-1])
"""

s = "  Python is Fun and Powerful  "
print(s.strip())
s1 = s.lower()
print(s1)
print(s1[20:28])

name = "Developer"
print(name[1:5])
print(name[-4:])
print(name[::-1])