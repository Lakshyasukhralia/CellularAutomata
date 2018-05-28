from TempRule import HashFunC
import numba as nb

IP = []
H_Time_Dec = []

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   #print(n % 2,end = '')
   IP.append(n%2)

#@nb.jit(nopython=True)
def CY_Num(x,Dec,s,lines):

    if Dec == True:
        b_n = 0
        #print(s)
        convertToBinary(x)

        size = len(IP)
        a_zero = 8 - size

        for i in range(0,a_zero):
            if size<8:
                IP.insert(0,0)

        #print("Val in Binary:",IP)



        if lines == "111True":
            RV = True
            Stage,IV_H = HashFunC(IP,111,RV)
        elif lines == "111False":
            RV = False
            Stage,IV_H = HashFunC(IP,111,RV)
        elif lines == "9True":
            RV = True
            Stage,IV_H = HashFunC(IP,9,RV)
        elif lines == "9False":
            RV = False
            Stage,IV_H = HashFunC(IP,9,RV)
        else:
            RV = False
            Stage,IV_H = HashFunC(IP,9,RV)



        #print(IV_H)

        for i in range(0,8):
            b_n = b_n*10 + IV_H[i]

        b_n = format(b_n,"08")
        #print("Binary ouput of Half Cycle IV:",b_n)

        n = int(b_n,2)
        IP.clear()
        return n

    else:
        IS =[]
        RV = False
        RVR = "False"
        b_n = 0

        if x%2 == 0:
            RV = True
            RVR = "True"
        else:
            RVR = "False"
            pass

        # decimal number
        convertToBinary(x)

        size = len(IP)
        a_zero = 8 - size

        for i in range(0,a_zero):
            if size<8:
                IP.insert(0,0)

        #print("Val in Binary:",IP)
        F_Time,IS = HashFunC(IP,1000,RV)
        #print("Time where recursion starts:",F_Time)

        if F_Time%2 == 0:
            print("Even")
            CTF = True
            H_Time =int(F_Time/2)
            #H_Time_Dec.append(H_Time)
        else:
            print("Odd")
            CTF = False
            H_Time =int((F_Time+1)/2)
            #F_Time = F_Time + 1

        #H_Time =int(F_Time/2)
        #print("Full Time and Half the full time:",F_Time,H_Time)

        Stage,IV_H = HashFunC(IP,H_Time,RV) #Convert this binary num to decimal and replace it in image
        #IV_H = HashFunC(IV_H,H_Time+1,RV)

        if(CTF == True):
            H_Time_Dec.append(H_Time + 2) #Even 111 and else
            #IV_H = HashFunC(IV_H,H_Time+2,RV)
        if(CTF == False):
            H_Time_Dec.append(H_Time + 1) #Odd 9
            #IV_H = HashFunC(IV_H,H_Time+1,RV)
        #print("Decryption List",H_Time_Dec)
    #    print("IV after half cycles to Initial stage is:",IV_H)


        for i in range(0,8):
            b_n = b_n*10 + IV_H[i]

        b_n = format(b_n,"08")
    #    print("Binary ouput of Half Cycle IV:",b_n)

        n = int(b_n,2)
        IP.clear()
        #print(H_Time_Dec)
        with open('D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\test.txt', 'a') as the_file:
            the_file.write(str(H_Time_Dec[s]))
            the_file.write(RVR)
            the_file.write("\n")

        '''if(CTF == True):
            return n*0.5
        else:'''
        return n

#print(CY_Num(218,False,0,9))
#print(CY_Num(88,True,0,"111True"))
#print(H_Time_Dec)
#print(HashFunC([0,1,0,1,1,0,0,0],H_Time_Dec[0],False))
