# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

num = 0
sum = 0.0

while True:
    #Get value from user
    val = input("Enter a number: ")

    #if done then break the loop
    if val == "done" :
        break    
    
    #Convert the value to float
    
    try :
        floatVal = float(val)
        num = num + 1
        sum = sum + floatVal
    except :
        print("Invalid Input")
        continue


try: 
    print(num, sum, sum/num)
except: 
    print("No Input")
 
    
