import cv2 as cv
import numpy as np

image = np.zeros((512,512,3),np.uint8)

cv.rectangle(image,(210,210),(100,100),(100,200,10),3)

cv.imshow("Rectangle",image)

