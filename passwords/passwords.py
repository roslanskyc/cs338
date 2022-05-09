import hashlib
import binascii


f = open('words.txt')

words = [line.strip().lower() for line in f]
hashed1 = [line.strip().lower() for line in open('passwords1.txt')]


for x in range(len(hashed1)):
    hashed1[x] = hashed1[x].split(':')

for x in range(len(words)):
    password = words[x].encode('utf-8')
    hash = hashlib.sha256(password)
    digest = hash.digest() 
    digest_as_hex = binascii.hexlify(digest) 
    digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
    words[x] = [words[x], digest_as_hex_string]



print(words[2000])
print(hashed1[2110])