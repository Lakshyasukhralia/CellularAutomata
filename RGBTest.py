from ImageRet import CY_Num
from Final_Enc import Average
import cv2
import numpy as np

Dec = False
enc_val = 0
lines =[]
img = cv2.imread("image.png",1)
b,g,r = cv2.split(img)

#print(g)
#cv2.imshow("Original Image",g)
#[[j*0 for j in i] for i in img]
def Encrypt(bgr,channel):
    for i in bgr:
        x = 0
        for j in i:
                print("-----------------------------------------")
                print("Input Val:",j)
                enc_val = CY_Num(j,Dec,x,lines)
                i[x] = enc_val
                x = x+1
                print("Encrypted Val:",enc_val)
                print("-----------------------------------------")
    cv2.imwrite("D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\"+channel +".png",bgr)
    cv2.imshow("Encrypted Image:" + channel,bgr)

Encrypt(b,"Blue")
Encrypt(g,"Green")
Encrypt(r,"Red")

Average()

cv2.waitKey(0)
cv2.destroyAllWindows()
