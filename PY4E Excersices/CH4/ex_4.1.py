# Exercise 4: What is the purpose of the “def” keyword in Python?
# a) It is slang that means “the following code is really cool”
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true
# e) None of the above

## ANSWER: D

# Exercise 5: What will the following Python program print out?
# def fred():
#    print("Zap")

# def jane():
#    print("ABC")

# jane()
# fred()
# jane()

## ANSWER: ABC Zap ABC


# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

def computepay(hours, rate) :
    pay = float(hours) * float(rate)
    
    if float(hours) > 40 :
        extraHours = float(hours) - 40
        extraHourpay = float(extraHours) * (float(rate) * .5)
        pay = pay + extraHourpay
    
    return pay


try :
    print(computepay(hours, rate))
except:
    print("Value should be numerical")
