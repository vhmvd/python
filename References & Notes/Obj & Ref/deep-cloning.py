#done by slicing
a=[23,24,254]
b = a[:]
print(a is b)
print(a == b)
print(hex(id(a)))
print(hex(id(b)))
