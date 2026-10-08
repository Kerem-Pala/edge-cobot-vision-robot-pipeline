import cv2 as cv
import numpy as np



lower_red1 = np.array([0,160,100])
upper_red1 = np.array([10,255,255])


lower_red2 = np.array([170,160,100])
upper_red2 = np.array([180,255,255])



def findRed(frame):
    kernel = np.ones((5,5), np.uint8) 

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)

    mask = cv.bitwise_or(mask1, mask2)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN,kernel)

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    biggest_contour = max(contours, key=cv.contourArea, default=None)



    if biggest_contour is not None:
        biggest_area = cv.contourArea(biggest_contour)

        x, y, w, h = cv.boundingRect(biggest_contour)

        cX = int(x + w/2)
        cY = int(y + h/2)

        cv.rectangle(frame, (x,y),(x + w, y+ h), (0, 255,0),3)
        cv.circle(frame, (cX, cY,),5,(0,255,0),-1)

        return (cX, cY)
    

   


