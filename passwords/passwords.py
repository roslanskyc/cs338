
f = open('words.txt')

words = [line.strip().lower() for line in f]
hashed1 = [line.strip().lower() for line in open('passwords1.txt')]


for x in range(len(hashed1)):
    hashed1[x] = hashed1[x].split(':')

print(words[20])
print(hashed1[20])