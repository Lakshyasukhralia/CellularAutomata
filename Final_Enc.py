import cv2
import numpy as np


def Average():
    b = cv2.imread("D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\Blue.png")
    g = cv2.imread("D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\Green.png")
    r = cv2.imread("D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\Red.png")

    bgr_enc = (b+g+r)//3
    print(bgr_enc)
    cv2.imshow("Final Encrypted Image:",bgr_enc)
    cv2.imwrite("D:\\Cellular Automata Stuff\\CellularAutomata\\Generated\\Final_Enc.png",bgr_enc)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
