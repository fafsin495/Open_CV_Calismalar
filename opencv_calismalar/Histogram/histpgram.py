import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread("f16.jpg")

b,g,r = cv.split(image)


cv.imshow("Images",image)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
