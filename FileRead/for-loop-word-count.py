fname = 'mbox-short.txt'
count = 0

fileHandle = open(fname)
for line in fileHandle:
    if line.startswith("Received"):
        count += 1

print('Count of the mentioned words were: ',count)