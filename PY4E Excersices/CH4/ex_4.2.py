# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

score = input("Enter score: ")

def computegrade(score) :
    # Converted score from string to float
    score = float(score)
    
    if score >= 0.9 :
        grade = "A"
    elif score >= 0.8 :
        grade = "B"
    elif score >= 0.7 :
        grade = "C"
    elif score >= 0.6 :
        grade = "D"
    elif score < 0.6 :
        grade = "F"

    return grade


try :
    print(computegrade(score))
except: 
    print("Bad Score")