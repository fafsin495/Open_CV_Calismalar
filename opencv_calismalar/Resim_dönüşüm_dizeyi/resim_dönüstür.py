import cv2 as cv
import numpy as np

image = cv.imread("cat.png",0)

row,column= image.shape


matrix = np.float32([[1,0,50],[0,1,200]])

warpAffine = cv.warpAffine(image,matrix,(row,column))

cv.imshow("warp",warpAffine)

cv.waitKey(0)
cv.destroyAllWindows()

