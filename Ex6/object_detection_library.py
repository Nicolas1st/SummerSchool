import numpy as np
import cv2


def detect_moving_objects(filepath):

    cap = cv2.VideoCapture(filepath)
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while True:

        returned, frame = cap.read()       

        if not returned:
            print("The last frame given was empty")
            break
      
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

        coords = []

        for cnt in contours:

            rect = cv2.boundingRect(cnt)
            left_upper_x = rect[0]
            left_upper_y = rect[1]
            width = rect[2]
            height = rect[3]

            center_x = left_upper_x + width // 2
            center_y = left_upper_y + height // 2
            coords.append((center_x, center_y))

        yield coords
      
    cap.release()




if __name__ == "__main__":

    filename = 'le_video.MOV'

    for object_location in detect_moving_objects(filename):
       print(object_location)
