import cv2 as cv
import numpy as np

image = cv.imread("images.jpg")

hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)

lower_blue = np.array([10,50,50])
upper_blue = np.array([130,255,255])

masked = cv.inRange(hsv,lower_blue,upper_blue)

cv.imshow("Picture",image)
cv.imshow("Masked",masked)

cv.waitKey(0)
cv.destroyAllWindows()
