#curly braces makes for dictionary
#init key value pair obj with the contructor
bag = dict()

#left side is key and right side is value

bag['money'] = 23
bag['chocolate'] = 32
bag['gun'] = 1

print(bag)

#to find the specific the specific item

print(bag['gun'])

#dictionary contents are mutable therefore they can be changed

bag['gun'] = bag['gun'] + 419
print(bag)