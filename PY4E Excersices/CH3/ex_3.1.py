#Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.


hours = float(input("Enter hours: "))
rate = float(input("Enter Hourly Rate: "))



pay = hours * rate


if hours > 40 :
    extraHours = hours - 40
    extraHoursPay = extraHours * (rate * .5)
    pay = pay + extraHoursPay

    
print(pay)

