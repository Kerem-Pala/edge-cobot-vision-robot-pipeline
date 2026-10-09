from src.transform import transormRedCoordinates
from src.vision import findRed
from src.robot_interface import robotInterface

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('./data/video.mp4')
robot = robotInterface()
x,y= (0,0)

if not cap:
    print("no cam")
    exit()


while True:
    ret, frame = cap.read()

    if not ret:
        print("cant recieve frame")
        break

    centerCoordinate = findRed(frame=frame)

    if centerCoordinate is not None:
        x,y = transormRedCoordinates(centerCoordinate[0], centerCoordinate[1])
        robotInterface.sendCommand(robot, x=x, y=y)

    cv.putText(frame, f"x:{int(x)}, Y: {int(y)}",(int(x),int(y)),1,1.0,(0,255,0),1)
    #cv.imshow('frame', frame)
    


    #if cv.waitKey(1) == ord('q'):
    #    break
    


cap.release()
cv.destroyAllWindows()


