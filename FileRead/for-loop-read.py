# Sample.txt downloaded from http://25.io/toau/audio/sample.txt


# Returns a handle, for file handling in fileHandle variable
# handle = open(filename, mode)
# mode is optional and should be 'r' for read and 'w' for write

fileHandle = open('sample.txt')
for varible in fileHandle:
    print(varible)