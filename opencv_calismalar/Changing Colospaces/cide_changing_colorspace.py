import cv2 as cv
import numpy as np

video = cv.VideoCapture("cat.mp4")

while True:
               empty,frame = video.read()
               hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

               lower_white = np.array([0,0,0],dtype = np.uint8)
               upper_white = np.array([50,50,255],dtype = np.uint8)

               masked = cv.inRange(hsv,lower_white,upper_white)
               cv.imshow("Video",frame)
               cv.imshow("masked",masked)

               if cv.waitKey(27) & 0xFF==ord("q"):
                              break
video.release()
cv.destroyAllWindows()

cv.waitKey(0)
cv.destroyAllWindows()
