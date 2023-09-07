import cv2
from PIL import Image
from util import get_limits

green = [0,255,0] # color in BGR
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    l_lim, u_lim = get_limits(color = green)

    mask = cv2.inRange(hsv_img, l_lim, u_lim)
    
    mask_ = Image.fromarray(mask) # convert numpy array to pilow
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()