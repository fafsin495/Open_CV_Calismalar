import cv2 as cv
import numpy as np


image = cv.imread("b1.png")
image1 = cv.imread("b2.png")

bit_and = cv.bitwise_and(image1,image)
bit_or = cv.bitwise_or(image1,image)
bit_xor = cv.bitwise_xor(image1,image)
bit_not1 = cv.bitwise_not(image1)
bit_not = cv.bitwise_not(image)

cv.imshow("OrginalImage",image)
cv.imshow("OriginalImage1",image1)
cv.imshow("Bit_Or",bit_or)
cv.imshow("Bit_and",bit_and)
cv.imshow("Bit_xor",bit_xor)
cv.imshow("Bit_not1",bit_not1)
cv.imshow("Bit_not",bit_not)


cv.waitKey(0)
cv.destroyAllWindows()
