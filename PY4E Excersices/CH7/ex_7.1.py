# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:


filename = input("Enter File Name: ")

try: 
    fhand =  open(filename)
except: 
    print("File Not Found!")
    exit()

for line in fhand :
    print(line.upper())

