# counts = dict()
# names = ["scev", "csev", "phill", "scev", "csev", "phll"]


# for name in names :

#     counts[name] = counts.get(name, 0) + 1

#     print(counts.get(name))
#     # if name not in counts :
#     #     counts[name] = 1
#     # else : 
#     #     counts[name] = counts[name] + 1

# print(counts)

# counts = dict()
# print("Enter a line of text")
# line = input('')

# words = line.split()

# print('Words: ', words)

# print('Counting...')
# for word in words :
#     counts[word] = counts.get(word, 0) + 1


# print('Counts', counts)


# print("Enter a line of text!")
# name = input('')
# words = name.split()

# counts = dict()

# for word in words :
#     counts[word] = counts.get(word, 0) + 1


# bigcount = None
# bigword = None

# for word,count in counts.items() :
#     if bigcount is None or count > bigcount :
#         bigword = word
#         bigcount = count


# print(counts)
# print(bigword, bigcount)

# BOOKS EXCERCISE 1

# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary

# fhand = open("words.txt")
# wordsdict = dict()

# for line in fhand :
#     words = line.split()
#     for word in words :
#         wordsdict[word] = len(word)

# print(wordsdict)