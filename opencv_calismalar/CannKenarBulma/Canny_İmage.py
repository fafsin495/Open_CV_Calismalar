import cv2 as cv

image = cv.imread("f16.jpg")

canny = cv.Canny(image,100,200)

cv.imshow("orginal",image)
cv.imshow("canny",canny)

cv.waitKey(0)
cv.destroyAllWindows()
