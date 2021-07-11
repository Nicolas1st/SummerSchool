import numpy as np
import cv2
from copy import copy
  

filepath = input('path to the file: ')
cap = cv2.VideoCapture(filepath)
fgbg = cv2.createBackgroundSubtractorMOG2()
detector = cv2.SimpleBlobDetector(cv2.SimpleBlobDetector_Params())

  
while True:

    ret, frame = cap.read()       
  
    fgmask = fgbg.apply(frame)  

    # some transformation that when working together remove the noise from the image
    blur = cv2.GaussianBlur(fgmask,(5,3), 5) 
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(fgmask, kernel, iterations = 5)
    dilated = cv2.dilate(eroded, kernel, iterations = 8)

    lower_black = np.array([120], dtype = "uint8")
    upper_black = np.array([255], dtype = "uint8")
    mask = cv2.inRange(dilated, lower_black, upper_black)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # press ESC to quit
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break
  

cap.release()
cv2.destroyAllWindows()
