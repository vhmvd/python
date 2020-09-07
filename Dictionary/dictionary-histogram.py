dictObj = dict()
alphabets = ['a', 'a', 'b', 'c', 'd', 'b', 'a']

print(dictObj)

for itr in alphabets:
    if(itr in dictObj):
        dictObj[itr] = dictObj[itr] +1
    else:
        dictObj[itr] = 1

print(dictObj)