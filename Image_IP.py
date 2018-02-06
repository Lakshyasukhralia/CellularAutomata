from ImageRet import CY_Num
import cv2
import numpy as np

enc_val = 0
img = cv2.imread("image.jpg",0)
print(img)

cv2.imshow("Original Image",img)

#[[j*0 for j in i] for i in img]

for i in img:
    x = 0
    for j in i:
            print("-----------------------------------------")
            print("Input Val:",j)
            enc_val = CY_Num(j)
            i[x] = enc_val
            x = x+1
            print("Encrypted Val:",enc_val)
            print("-----------------------------------------")


print(img)

cv2.imshow("Encrypted Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
