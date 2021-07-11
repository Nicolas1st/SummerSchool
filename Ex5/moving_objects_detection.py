import numpy as np
import cv2
  

filepath = input('path to the file')
cap = cv2.VideoCapture(filepath)
fgbg = cv2.createBackgroundSubtractorMOG2()
  
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

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 6)

    # drawing the bouding boxes,
    # the following colors are used
    # red - contours
    # green - point from which the bouding box is drawn 
    # blue - the bounding box itself
    for cnt in contours:
        rect = cv2.boundingRect(cnt)
        central_x = rect[0]
        central_y = rect[1]
        width = rect[2]
        height = rect[3]
        start_point = (central_x + height, central_y + width)
        end_point = (central_x, central_y)
        frame = cv2.rectangle(frame, start_point, end_point, (255, 0, 0), 5)
        frame[central_y-10:central_y+10,central_x-10:central_x+10] = (0, 255, 0)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # press ESC to quit
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break
  

cap.release()
cv2.destroyAllWindows()
