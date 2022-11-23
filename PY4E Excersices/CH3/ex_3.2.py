#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input("Enter hours: ")
rate = input("Enter Hourly Rate: ")

try: 
    if float(hours) > 40 :
        rate = float(rate) * 1.5

    pay = float(hours) * float(rate)
    print(pay)

except:
    print("Error! Please enter numeric input")

