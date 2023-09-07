import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    l_lim = hsvC[0][0][0] - 10,100,100
    u_lim = hsvC[0][0][0] - 10,255,255
    
    l_lim = np.array(l_lim, dtype=np.uint8)
    u_lim = np.array(u_lim, dtype=np.uint8)

    return l_lim, u_lim