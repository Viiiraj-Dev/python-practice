# # Reading and writing files

# with open("notes.txt", "w") as f:       # w owerwrites, a appends
#     f.write("line one\n")
#     f.write("line two\n")

# with open("notes.txt", "r") as f:
#     content = f.read()
#     print(content)            # whole file  as one string

# with open("notes.txt") as f:
#     for line in f:
#         print(line.strip())   # line by line (memory-friendly)


# # try/except
# try:
#     n= int(input("Number: "))
#     print(10/n)
# except ValueError:
#     print("That's not a number")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# else:
#     print("No errors happened")  # runs only if try succeeded
# finally:
#     print("Always runs") # cleanup code


# Common Exceptions -> ValueError, TypeError, KeyError, IndexError, FileNotFoundError, ZeroDivisionError


# # Raising your own errors
# def set_age(age):
#     if age<0:
#         raise ValueError("Age can't be negative")
#     return age

# print(set_age(2))
# # set_age(-1)


# # Json
# import json

# data = {"name" : "Vir", "skills" : ["python", "sql"]}
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=2)

# with open("data.json") as f:
#     loaded = json.load(f)
#     print(loaded)


"""
Exercise 1: Fix your guessing game so typing abc prints “Please enter a valid number” and asks again 
instead of crashing.
(Write a number-guessing game using while. The secret number is 7. Keep asking the user to guess, 
print “Too high” or “Too low” 
after each wrong guess, and stop with “Correct!” when they get it.)

Exercise 2: Write a program that reads a filename from the user and prints the number of lines 
and words in it. If the file doesn’t 
exist, print a friendly message instead of crashing. (Create a small .txt file to test with.)

Exercise 3: Build a tiny to-do saver. Keep a list of tasks, let the user add a task in a loop 
(type q to quit), and save the list to 
todos.json on exit. When the program starts, load the existing tasks from the file if it exists.
"""

while True:
    try:
        n = int(input("Guess Your Number: "))
        if n==7:
            print("Correct!")
            break
        elif n<7:
            print("Too low")
        elif n>7:
            print("Too high")
    except ValueError:
        print("Please enter a valid number")

file_name = input("Enter File Name: ")

try:
    with open(file_name, "r") as f:
        no_of_lines = 0
        no_of_words = 0
        for line in f:
            no_of_lines+=1
            no_of_words += len(line.split())
        print("No. of Lines: ", no_of_lines)
        print("No. of Words: ", no_of_words)
except FileNotFoundError:
    print("Create a small .txt file to test with.")


"""
Exercise 3: Build a tiny to-do saver. Keep a list of tasks, let the user add a task in a loop 
(type q to quit), and save the list to 
todos.json on exit. When the program starts, load the existing tasks from the file if it exists.
"""
import json
try: 
    with open("todos.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"ToDos" : []}

while True:
    i = input("Enter Task to Add: ")
    if i=='q' or i=='quit':
        break
    data["ToDos"].append(i)

with open("todos.json", "w") as f:
    json.dump(data, f)






