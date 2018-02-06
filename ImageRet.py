from TempRule import HashFunC

IP = []

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   #print(n % 2,end = '')
   IP.append(n%2)


def CY_Num(x):
    b_n = 0
    # decimal number
    convertToBinary(x)

    size = len(IP)
    a_zero = 8 - size

    for i in range(0,a_zero):
        if size<8:
            IP.insert(0,0)

    print("Val in Binary:",IP)
    F_Time = HashFunC(IP,1000)
    print("Time where recursion starts:",F_Time)

    if F_Time%2 == 0:
        pass
    else:
        F_Time = F_Time + 1

    H_Time =int(F_Time/2)
    print("Half the full time:",H_Time)


    IV_H = HashFunC(IP,H_Time) #Convert this binary num to decimal and replace it in image
    print("IV after half cycles to Initial stage is:",IV_H)

    for i in range(0,8):
        b_n = b_n*10 + IV_H[i]

    b_n = format(b_n,"08")
    print("Binary ouput of Half Cycle IV:",b_n)

    n = int(b_n,2)
    IP.clear()
    return n
