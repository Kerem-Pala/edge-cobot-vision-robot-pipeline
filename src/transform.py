import cv2 as cv
import numpy as np


def transormRedCoordinates(x, y):
    coordinates = np.array([[[x, y]]], dtype=np.float32)

    soruce_pixels = np.array([[224,204], [721,99], [1209, 469], [605,679]],np.float32)
    goal_mm = np.array([[0,0], [210,0], [210, 297], [0,297]],np.float32)

    h, m = cv.findHomography(soruce_pixels, goal_mm)

    result = cv.perspectiveTransform(coordinates,h)
    return(result[0][0][0], result[0][0][1])
