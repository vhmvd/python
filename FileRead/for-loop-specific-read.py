
fname = 'mbox-short.txt'

fileHandle = open(fname)
for line in fileHandle:
    if line.startswith("From: "):
        print(line)

# We see extra backspaces because print function adds newline itself after reading a line 
# (which also includes \n character)

# This is tackled with rstrip function which strips whitspaces on right

fileHandle = open(fname)
for line in fileHandle:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

print('==================================================')
# Flipped simialr logic with continue but different requirement but full line

fileHandle = open(fname)
for line in fileHandle:
    line = line.rstrip()
    if not "uct" in line:
        continue
    print(line)