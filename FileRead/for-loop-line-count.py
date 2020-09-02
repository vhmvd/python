# \n is treated as a character and for loops takes it as a newline similar to <Enter> in normal typing

fileHandle = open('sample.txt')
count = 0
for varible in fileHandle:
    count += 1

print(count)