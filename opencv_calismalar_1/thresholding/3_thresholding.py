import cv2 as cv
import numpy as np

image = cv.imread("f16.jpg",0)


ret,th = cv.threshold(image,150,200,cv.THRESH_BINARY)

th1 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,21,2)

th2 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,2)


cv.imshow("Normal_Threshold",th)
cv.imshow("ADAPTIVE_MEAN_Threshold",th1)
cv.imshow("GAUSSIAN_Threshold",th2)


cv.waitKey(0)
cv.destroyAllWindows()
