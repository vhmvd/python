fileName = input('Enter the name of file: ')
try:
    fileHandle = open(fileName)
except FileNotFoundError:
    print('Unable to open', fileName)
    quit()

count = 0
for line in fileHandle:
    if line.startswith('From:'):
        count += 1
print('There are',count,'words in', fileName)