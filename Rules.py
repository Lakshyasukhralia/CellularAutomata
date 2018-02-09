#RULES
import itertools
#RULE90

def XOR(x,y,z):
    if x!=z:
        return 1
    else:
        return 0

def NOT(x):
    if x == 1:
        return 0
    else:
        return 1

def R90(p,q,r): #Working
    return XOR(p,q,r)

def R102(p,q,r): #Working
    return XOR(p,q,r)

def R153(p,q,r):
    return NOT(q)*NOT(r) + q*r

def R254(p,q,r):
    return 1 - (1 - p)*(1 - q)*(1 - r)

def R250(p,q,r):
    return p + r - p * r


def R30(p,q,r): #Working
    return (p + q + r + q * r)% 2

def R110(p,q,r):
    return ((1 + p) * q * r + q + r)

def R130(p,q,r):
    return NOT(p)*NOT(q)*r + p*q*r

def R156(p,q,r):
    return NOT(p)*q + p*q*r + p*NOT(q)*NOT(r)

def R51(p,q,r):
    a = NOT(q)
    return a

#{51,51,51,102,153,153,51,156}

#print(R156(0,1,1))

'''
a = 5
b =int(input("Enter"))
c = a+b
print(c)
d = c%2
print(d)
'''

'''
R90 = R90(1,0,1)
R30 = R30(1,0,1)
Fun_R = [R90,R30]
a = [1,2,3,4]
b = []
sum = 0

for i in range(1,len(a)+1):
   b.append(list(itertools.combinations(a,i)))

for i in b:
    for k in i:
        for j in k:
            sum = sum + j
            print(sum)

print(b)
'''
