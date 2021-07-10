import cv2 
import numpy as np


image = cv2.imread("sun.jpeg")


BINARY_THRESHOLD = 20
CONNECTIVITY = 4
CIRCLE_RADIUS = 4


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary_image = cv2.Laplacian(gray_image, cv2.CV_8UC1)
dilated_image = cv2.dilate(binary_image, np.ones((5, 5)))
not_needed, threshhold = cv2.threshold(dilated_image, BINARY_THRESHOLD, 255, cv2.THRESH_BINARY)
components = cv2.connectedComponentsWithStats(threshhold, CONNECTIVITY, cv2.CV_32S)


centers = components[3]
for c in centers:
    cv2.circle(threshhold, (int(c[0]), int(c[1])), CIRCLE_RADIUS, (255), thickness=-2)


cv2.imshow("result", threshhold)
cv2.waitKey(0)
