"""
Write a program that extracts the last three items in the list sports and assigns it 
to the variable last. Make sure to write your code so that it works no matter how many items are in the list.
"""

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
size = len(sports)

last = ''
count = 0
for index in sports:
    count += 1
    if count > size - 3:
        last = last + index

print(last)
print(size)