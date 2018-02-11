from ImageRet import CY_Num
import cv2
import numpy as np

lines = []
enc_val = 0
Dec = True
img = cv2.imread("test.png",-1)
print(img)

#cv2.imshow("Original Image",img)

#[[j*0 for j in i] for i in img]


with open('test.txt') as f:
    lines = f.read().splitlines()

#print(lines)
k = 0
for i in img:
    x = 0
    for j in i:
            print("-----------------------------------------")
            print("Input Val:",j)
            print(k)
            print(lines[k])
            enc_val = CY_Num(j,Dec,k,lines[k])
            i[x] = enc_val
            x = x+1
            k = k+1
            print("Encrypted Val:",enc_val)
            print("-----------------------------------------")


print(img)
cv2.imwrite("Decrypted.png",img)
cv2.imshow("Decrypted Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
