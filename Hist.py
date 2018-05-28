import cv2
import numpy as np
from matplotlib import pyplot as plt

'''img_org = cv2.imread('image.jpg',0)
plt.hist(img_org.ravel(),256,[0,256])
plt.show()'''

img_enc = cv2.imread('D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\test.png',0)
plt.hist(img_enc.ravel(),256,[0,256])
plt.show()
