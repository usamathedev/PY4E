# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

numbers = list()

while True:
  #Get input from user  
  num = input("Enter a number: ")

  #Terminate loop if value is "done"
  if num == "done":
    break

  #check the largest and smallest number
  try:
    #change type of input from "str" to "int"
    numInt = int(num)
    #add the number to the list
    numbers.append(numInt)

  #in case of traceback
  except:
    print("Invalid input")

#assign new variables to calculate min and max
maxNum = list(numbers)
minNum = list(numbers)

# print("Minimum is", smallest)
print("Maximum is", max(maxNum))
print("Minimum is", min(minNum))


