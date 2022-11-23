#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input("Enter hours: ")
rate = input("Enter Hourly Rate: ")

try: 
    pay = float(hours) * float(rate)

    if float(hours) > 40 :
        extraHours = float(hours) - 40
        extraHoursPay = float(extraHours) * (float(rate) * .5)
        pay = pay + extraHoursPay

    print(pay)

except:
    print("Error! Please enter numeric input")

