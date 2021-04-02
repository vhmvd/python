dictObj = dict()
alphabets = ['a', 'a', 'b', 'c', 'd', 'b', 'a']

print(dictObj)

for itr in alphabets:
    dictObj[itr] = dictObj.get(itr, 0) + 1

print(dictObj)