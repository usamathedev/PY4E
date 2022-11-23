#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

score = input("Please enter your socre: ")

try:
    if float(score) >= 0.9 :
        grade = "A"
    elif float(score) >= 0.8 :
        grade = "B"
    elif float(score) >= 0.7 :
        grade = "C"
    elif float(score) >= 0.6 :
        grade = "D"
    elif float(score) < 0.6 :
        grade = "F"
    else :
        print("Please enter correct score!") 

    print(grade)

except:
    print("Bad Score")