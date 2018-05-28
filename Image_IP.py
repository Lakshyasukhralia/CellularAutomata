from ImageRet import CY_Num
import cv2
import numpy as np

Dec = False
enc_val = 0
lines =[]
img = cv2.imread("image.png",0)
print(img)

cv2.imshow("Original Image",img)

#[[j*0 for j in i] for i in img]

for i in img:
    x = 0
    for j in i:
            print("-----------------------------------------")
            print("Input Val:",j)
            enc_val = CY_Num(j,Dec,x,lines)
            i[x] = enc_val
            x = x+1
            print("Encrypted Val:",enc_val)
            print("-----------------------------------------")


print("------------------------------------------------------------------\n\n")
print(img)

cv2.imwrite("D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\test.png",img)
cv2.imshow("Encrypted Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
