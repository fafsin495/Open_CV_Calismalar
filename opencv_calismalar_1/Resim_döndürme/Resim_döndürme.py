import cv2 as cv
import numpy as np

image = cv.imread("cat.png",0)

row,col = image.shape

matrix = cv.getRotationMatrix2D((col/5,row/3),180,1)


warp = cv.warpAffine(image,matrix,(row,col))

cv.imshow("warpt",warp)
cv.waitKey(0)
cv.destroyAllWindows()
