"""
10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the 
hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fileHandle = open('mbox-short.txt')
hoursAndCount = dict()
for line in fileHandle:
    if line.startswith('From '):
        lineSplit = line.split()
        time = lineSplit[5]
        timeSplit = time.split(':')
        hoursAndCount[timeSplit[0]] = hoursAndCount.get(timeSplit[0],0) + 1

sortedHoursAndCount = sorted((k,v) for k,v in hoursAndCount.items())
for k,v in sortedHoursAndCount:
    print(k,v)