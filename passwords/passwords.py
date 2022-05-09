import hashlib
import binascii
import time
import re

from matplotlib import use


f = open('words.txt')

words = [line.strip().lower().encode('utf-8') for line in f]
hashed1 = [line.strip().lower() for line in open('passwords1.txt')]
hashed2 = [line.strip().lower() for line in open('passwords2.txt')]
hashed3 = [line.strip().lower() for line in open('passwords3.txt')]


hash_to_password = {}
username_to_password = {}

def calculate_cracked1():
    for x in range(len(hashed1)):
        hashed1[x] = hashed1[x].split(':')

    for x in range(len(words)):
        password = words[x].encode('utf-8')
        hash = hashlib.sha256(password)
        digest = hash.digest() 
        digest_as_hex = binascii.hexlify(digest) 
        digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
        hash_to_password[digest_as_hex_string] = words[x]
        #words[x] = [words[x], digest_as_hex_string]

    for password in hashed1:
        hash = password[1]
        word = hash_to_password[hash]
        username_to_password[password[0]] = word

def hash_word(word):
    hash = hashlib.sha256(word)
    digest = hash.digest() 
    digest_as_hex = binascii.hexlify(digest) 
    digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
    return digest_as_hex_string

def calculate_cracked2():
    start = time.time()
    password_to_user = {}
    for x in range(len(hashed2)):
        hashed2[x] = hashed2[x].split(':')

        password_to_user[hashed2[x][1]] = hashed2[x][0]
    
    hash_count = 0
    for word in words:
        for word2 in words:
            password = hash_word(word + word2)
            hash_count += 1
            if password in password_to_user.keys():
                username_to_password[password_to_user[password]] = word + word2
                print(f"{password_to_user[password]}: {word + word2} hashes: {hash_count} time: {time.time() - start}")


def calculate_cracked3():
    password_to_user = {}
    for x in range(len(hashed3)):
        hashed3[x] = re.split("[$:]", hashed3[x])
        password_to_user[hashed3[x][4]] = hashed2[x][0]
    
    print(hashed3[200])
    hash_count = 0

    f = open("cracked3.txt", "w")
    
    start = time.time()
    hash_count = 0
    for user in hashed3:
        hash = user[4]
        salt = user[3].encode('utf-8')
        for word in words:
            hash_count += 1
            if hash_word(salt + word) == hash:
                username_to_password[user[0]] = [salt, word]
                f.write(f"{user[0]}:{word}\n")
                print(f"hashcount: {hash_count} {time.time() - start}")
                # print(f"user: {user[0]} salt: {salt} password: {word}")

    print(username_to_password)

def save_passwords(file, password_dict):
    with open(file, "w") as f:
        for username, password in password_dict.items():
            f.write(f"{username}:{password}\n")

if __name__ == "__main__":
    calculate_cracked3()