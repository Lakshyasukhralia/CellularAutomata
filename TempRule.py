from Rules import RuleSet

IV = [0,0,0,0,1,0,0,0]
IV1 = IV[:]
IV2 = []
x = 0
Rec = False

#Input by user
'''for i in range(0,8):
    j = int(input(""))
    IV.append(j)
'''

print("Generation 0")
print(IV)

for j in range(1,10):
    if Rec == True:
        print("End")
        break
    x = 0
    IV2.clear()
    for i in IV:
        if x == 0:
            a = 0
            b = i
            c = IV[x+1]
            IV2.append(RuleSet(a,b,c))
            x = x+1
        else:
            if x == 7:
                a = IV[x-1]
                b = i
                c = 0
                IV2.append(RuleSet(a,b,c))
                print("Generation",j)
                print(IV2)
                if IV2 == IV1:
                    print("Initial Stage Achieved! \n")
                    Rec = True
                    break
                IV = IV2[:]
                break
            else:
                a = IV[x-1]
                b = i
                c = IV[x+1]
                IV2.append(RuleSet(a,b,c))
                x = x+1
