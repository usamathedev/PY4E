# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.



# First function
arr = [1,2,3,4]

def chop(arr1) :
    arr.pop()
    arr.pop(0)

    return None

chop(arr)
print(arr)



#2nd Function
arrTwo = [7,8,9,10,11,1,2,3]

def middle(arr2) :
    arrNew = list(arr2)

    arrNew.pop()
    arrNew.pop(0)
    
    return arrNew


print(middle(arrTwo))
print(arrTwo)