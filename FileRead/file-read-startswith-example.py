"""
Write a program that prompts for a file name, then opens that file and reads through the
 file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute
 the average of those values and produce an output as shown below. Do not use the sum() function
  or a variable named sum in your solution.
"""

fileName = input('Enter filename: ')
fileHandle = open(fileName)
count = 0
sumVar = 0.0
for line in fileHandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        fileFloat = line[19:]
        sumVar += float(fileFloat)

print('Average spam confidence:',sumVar/count)