from math import ceil, floor

N = 0
def karatsuba(a,b):
    global N
    N = N+1
    #cas d'arrêt
    if a < 10 and b < 10: # le nombre a un seul chiffre
        return a*b

    n =max(len(str(a)),len(str(b)))
    m = ceil(n/2)   

    a1  = floor(a / 10**m)
    a2 = a % (10**m)

    b1 = floor(b / 10**m)
    b2 = b % (10**m)

    # appels récursifs
    R1 = karatsuba(a1,b1)
    R2 = karatsuba(a2,b2)
    e = -1 if (a1 > a2 ) else 1
    e = -e if (b1 > b2 ) else e
    R3 = karatsuba(abs(a2 - a1), abs(b2 - b1))
    print(N,":::",a,':',b)
    return R1*(10**(m*2)) + e*(R1+R2-R3)*(10**m) + R2

def classique(a,b):
    #cas d'arrêt
    if a < 10 and b < 10: # le nombre a un seul chiffre
        return a*b

    n =max(len(str(a)),len(str(b)))
    m = ceil(n/2)   

    a1  = floor(a / 10**m)
    a2 = a % (10**m)

    b1 = floor(b / 10**m)
    b2 = b % (10**m)

    # appels récursifs
    R1 = classique(a1,b1)
    R2 = classique(a2,b2)
    
    R3 = classique(a1,b2)+classique(a2,b1)

    return R1*(10**(m*2)) + R3*(10**m) + R2

l = 2**50
print(karatsuba(l,l))
print(N)