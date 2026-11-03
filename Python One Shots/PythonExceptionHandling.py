# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     #print(e)
#     print("Invalid Input!")

# print("Some imp lines of code")
# print("End of program")

# try: 
#     num = int(input("Enter an integer: "))
#     a= [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Index Error!!!")

# """
# try:
#     #statements which could generate exception
# except:
#     #solution of generated exception
# finally:
#     #block of code which is going to execute in any situation
# """

# try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except:
#     print("Some error occurred")
# finally:
#     print("I am always executed")

# def func1():
#     try:
#         l = [1, 5, 6, 7]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occurred")
#         return 0
#     finally:
#         print("I am always executed")

# x = func1()
# print(x)


# Custom Error
a = int(input("Enter any value between 5 and 9: "))
if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

q = input("Enter any integer: ")

try:
    if q=="quit":
        print("Quit")
    elif int(q)<5 or int(q)>5:
        raise ValueError("Value should be between 5 and 9")
except Exception as e:
    print(e)