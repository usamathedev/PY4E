# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).


# fhand = open("mbox-short.txt")
# counts = dict()

# for line in fhand :

#     if not line.startswith("From") :
#         continue

#     if len(line) == 1 or line.startswith("From:"):
#         continue

#     words = line.split()
#     print(words)

#     wordDay = words[2]
#     wordCount = words[4]

#     print(line.items())

    # for wordDay,wordCount in line.items() :
        # print(wordDay, wordCount)
        # counts[word] = counts.get(word, 0) + 1

#     counts[words[2]] = int(words[4])

#     print(words[2], words[4])

# print(counts)
    
name = input("Enter file:")
count = {}

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle :
    if not line.startswith("From") or len(line) <= 1 :
        continue
    if line.startswith("From:") :
        continue
        
    words = line.split()
    for word in words :
        if word == words[1] :
            count[word] = count.get(word, 0) + 1


bigword = None
bigcount = None
for word, count in count.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigword = word

print(bigword, bigcount)


    


