# File I/O in Python - Python can be used to perform operations on a file (read & write data)

# f = open("file_name", "mode)  # mode -> r=read, w=write

f = open("demo.txt", "r")

# data = f.read()
# print(data)
# print(type(data))

#data = f.read(5)
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()

# r -> open for reading (default)
# w -> open for writing, truncating the file first
# x -> create a new file and open for writing
# a -> open for writing, appending to the end of the file if it exists
# b -> binary mode
# t -> text mode (default)
# + -> open a disk file for updating (reading and writing)


# # Writing to a file

# f = open("demo.txt", "w") # Overwrites the content of file

# f.write("I want to learn Python")

# f.close()

# f = open("demo.txt", "a")
# f.write("\nThen I'll move to AWS")
# f.close()

# f = open("sample.txt", "a")  # w/a mode creates the file if not exists
# f.write("Lets Learn Python Development")
# f.close()


# # r+ -> Open for reading and writing. The stream is positioned at the beginning of the file. 
# # It owerwrites
# f = open("demo.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close


# # w+ -> Open for reading and writing, The file is created if it does not exist, 
# # otherwise it is truncated. The stream is positioned at the beginning of the file
# f = open("demo.txt", "w+") # truncates if data exists
# print(f.read())
# f.write("ABC")
# f.close()


# # a+ -> Open for reading and writing. The file is created if it does not exist. The stream 
# # is positioned at the end of the file
# f = open("demo.txt", "a+") #No truncate
# print(f.read())
# f.write("ABC")
# f.close()


# # With Syntax
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("New Data")


# Deleting a File - using the os module
# Module(like a code library) is a file written by another programmer 
# that generally has a functions we can use

# import os
# os.remove("sample.txt")


# Practice

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O \nusing Java.\nI like programming in Java.")

def replace_java(file_name):
    with open(file_name, "r+") as f:
        data = f.read()
        data= data.replace("Java", "Python")
    with open(file_name, "w+") as f:
        f.write(data)

replace_java("practice.txt")

with open("practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") >= 0:
        print("Exists")
    else:
        print("Does Not exists")

def find_learn(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        lst = data.split("\n")
        for i in lst:
            if i.find("learning")!=-1:
                print("Line no:", lst.index(i)+1, "contains data")
                return
        print(-1)
        

find_learn("practice.txt")

with open("numbers.txt", "r") as f:
    data = f.readline()
    lst = data.split(",")
    sum = 0
    for i in lst:
        if int(i)%2==0:
            sum+=int(i)
    print("Sum of even Numbers in file: ", sum)
    

