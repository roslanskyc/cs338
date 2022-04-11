g = 11
p = 59

A = 57
B = 44

def bruteforce(g,p,A):
    a = 1
    while((g**a) % p != A):
        a += 1
    return a

a = bruteforce(g, p, A)
b = bruteforce(g, p, B)
K = (g**(a*b) % 59)
# K = (a**b) % 59
print("a = " + str(a))
print("b = " + str(b))
print("K = " + str(K))