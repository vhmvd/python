# mbox-short.txt is copied from http://www.py4inf.com/code/mbox-short.txt


# Returns a handle, for file handling in fileHandle variable
# handle = open(filename, mode)
# mode is optional and should be 'r' for read and 'w' for write

fileHandle = open('mbox-short.txt')
for varible in fileHandle:
    print(varible)