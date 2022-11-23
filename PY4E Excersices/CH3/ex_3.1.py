#Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.


hours = float(input("Enter hours: "))
rate = float(input("Enter Hourly Rate: "))

if hours > 40 :
    rate = rate * 1.5

pay = hours * rate

print(pay)