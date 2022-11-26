# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.



largest = None
smallest = None
while True:
  #Get input from user  
  num = input("Enter a number: ")

  #Terminate loop if value is "done"
  if num == "done":
    break

  #check the largest and smallest number
  try:
    #change type of input from "str" to "int"
    numint = int(num)
    if largest == None or numint > largest:
      largest = numint
    if smallest == None or numint < smallest:
      smallest = numint
  #in case of traceback
  except:
    print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)