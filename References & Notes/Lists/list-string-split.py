sentence = 'A random sentence here'
# converts the sentence into list of words
split = sentence.split()
print(split)

sentence2 = 'A;random;sentence;here'
split = sentence2.split()
print(split)

sentence2 = 'A;random;sentence;here'
split = sentence2.split(';')
print(split)