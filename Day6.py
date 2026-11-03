# # Dictionaries -> key value pair

# user = {"name":"Vir", "age":25}
# print(user["name"])
# print(user.get("city", "N/A")) # safe access
# user["city"] =  "Pune"
# print(user)
# del user["age"]
# print(user)
# for key, value in user.items():
#     print(key, value)
# print(user.keys(), user.values())
# print("name" in user)


# # Tuple - Immutable list
# point = (1, 2)
# x, y = point # unpacking
# print(point[0])
# #point[0] = 5 # Type Error
# single = (5,)
# print(single)


# # Sets - Unique & Unordered
# nums = {1,2,2,3}
# print(nums)
# nums.add(4)
# nums.discard(10) # No error if not present
# print(nums)
# a, b = {1,2,3}, {2,3,4}
# print(a & b)
# print(a | b)
# print(a-b)
# unique = list(set([1,1,2,3,3]))
# print(unique)


# # While loops
# count =0
# while count<=3:
#     print(count)
#     count+=1

# while True:
#     answer = input("Enter q to quit: ")
#     if answer=="q":
#         break


"""
Exercise 1: Given text = "the quick brown fox jumps over the lazy dog the end", count how often each word appears and store it in a dictionary. Print each word with its count. (Hint: .split(), a for loop, and .get(word, 0) + 1.)

Exercise 2: Given nums = [1, 2, 2, 3, 4, 4, 5], print the duplicates-removed list and the count of unique values using a set.

Exercise 3: Write a number-guessing game using while. The secret number is 7. Keep asking the user to guess, print “Too high” or “Too low” after each wrong guess, and stop with “Correct!” when they get it.
"""

text = "the quick brown fox jumps over the lazy dog the end"
lst = text.split()
dct = {}
for val in lst:
    dct[val]=lst.count(val)

for key, value in dct.items():
    print(key, value)

nums = [1, 2, 2, 3, 4, 4, 5]
print(list(set(nums)))
print(len(list(set(nums))))

while True:
    num = int(input("Enter the Secret Number: "))
    if num==7:
        print("Correct!")
        break
    elif num<7:
        print("Too low")
    else:
        print("Too High")