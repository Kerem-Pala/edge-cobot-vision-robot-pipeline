from pathlib import Path

import cv2 as cv
import numpy as py

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH =  BASE_DIR / "data" / "video.mp4"

cap = cv.VideoCapture(str(IMAGE_PATH))

ret, frame = cap.read()



def onMouse(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"X: {int(x)}, Y: {int(y)}")


while True:
    cv.imshow('frame', frame)

    cv.setMouseCallback('frame', onMouse)
    


    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

