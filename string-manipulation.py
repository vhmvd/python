""" 
Personal Notes
Ahmed Nadeem
ahmed210899@gmail.com
"""

#Lower case is > upper case a>A in string comparison


anyString = 'RandOm sTrinG'

#Lower case
zap = anyString.lower()
print(zap)

#Print in specified range
print(anyString[2:7])

#Alternative Method
print(anyString.lower())
print("Hey There".lower())

#Upper case
zap = anyString.upper()
print(zap)

#Capitalise first letter only
print(anyString.capitalize())
print("Hey There".capitalize())

#searching a string for position
position = anyString.find("sT")
print(position)
#not found = -1
position = anyString.find("z")
print(position)

#lstrip() removes ws from left rstrip() removes from right and strip() removes from both side

#confirms what the string starts from
print(anyString.startswith('R'))
print(anyString.startswith('r'))
print(anyString.startswith('RandO'))
print(anyString.startswith('Rando'))

#Shows available manipulation methods in chevron prompt
type(anyString)
dir(anyString)