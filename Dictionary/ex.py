"""
9.4 Write a program to read through the mbox-short.txt and figure out who 
has sent the greatest number of mail messages. The program looks for 'From ' 
lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to 
a count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to find 
the most prolific committer.
"""

sender = dict()

fileHandle = open('mbox-short.txt')
for line in fileHandle:
    if line.startswith('From '):
        splitted = line.split()
        sender[splitted[1]] = sender.get(splitted[1], 0) + 1

maxNum = 0
email = ""
for itr in sender:
    if sender[itr] > maxNum:
        maxNum = sender[itr]
        email = itr

print(email, maxNum)