import cv2 as cv
import numpy as np

image = np.zeros((512,512),np.uint8)

cv.circle(image,(100,100),30,(100,100,12),3)

cv.imshow("Circle",image)
