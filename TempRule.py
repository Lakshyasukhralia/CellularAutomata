from Rules import *
import numba as nb
#Rec = False

#Input by user
'''for i in range(0,8):
    j = int(input(""))
    IV.append(j)
'''
#@nb.jit(nopython=True)
def HashFunC(L,time,RV):
    j = 0
    IV1 = L[:]
    IV2 = []
    x = 0
    RV = False
    Rec = False
    IV = L[:]
    #print(IV)
    #print(IV)
    #print("Generation 0")
    #print(IV)
    #Cycles should be a minimum of 8 else Error
    for j in range(1,time):
        if Rec == True:
            #print("End")
            return j-1,IV
            break
        x = 0
        IV2.clear()
        for i in IV:
            if x == 0:
                a = 0
                b = i
                c = IV[x+1]
                #print(a,b,c,"-->",R30(a,b,c))
                #print("R90")
                IV2.append(R90(a,b,c))
                x = x+1
            else:
                if x == 7:
                    a = IV[x-1]
                    b = i
                    c = 0
                    #print(a,b,c,"-->",R30(a,b,c))
                    if RV == False:
                        #print("R90")
                        IV2.append(R90(a,b,c))
                    else:
                        #print("R30")
                        IV2.append(R30(a,b,c))
                    #print("Generation",j)
                    #print(IV2)
                    if IV2 == IV1:
                        print("Initial Stage Achieved! \n")
                        #print(IV2)
                        Rec = True
                        IV = IV2[:]
                        break
                    IV = IV2[:]
                    break
                else:
                    a = IV[x-1]
                    b = i
                    c = IV[x+1]
                    #print(a,b,c,"-->",R30(a,b,c))
                    if RV == False:
                        #print("R90")
                        IV2.append(R90(a,b,c))
                    else:

                        if x == 1:
                            #print("R30")
                            IV2.append(R30(a,b,c))
                        elif x == 2:
                            #print("R90")
                            IV2.append(R90(a,b,c))
                        elif x == 3:
                            #print("R30")
                            IV2.append(R30(a,b,c))
                        elif x == 4:
                            #print("R90")
                            IV2.append(R90(a,b,c))
                        elif x == 5:
                            #print("R30")
                            IV2.append(R30(a,b,c))
                        elif x == 6:
                            #print("R90")
                            IV2.append(R90(a,b,c))

                    x = x+1
    return j,IV

#print(HashFunC([0,0,0,0,0,1,1,0],1000000))
#print(HashFunC([1,1,1,1,1,1,1,1],10000000))
