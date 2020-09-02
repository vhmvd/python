# Since the entire string is read instantly with backspace as \n
# The character count can be done as follows

fileHandle = open('sample.txt')
testString = fileHandle.read()
print(len(testString))