a = 'abc'
b = 'abc'

print(a is b)
print(a == b)
print(hex(id(a)))
print(hex(id(b)))

a1 = ['1', 12]
b1 = ['1', 12]

print(a1 is b1) #a1 is not b1 because they are at different location in memory
print(a1 == b1)
print(hex(id(a1)))
print(hex(id(b1)))