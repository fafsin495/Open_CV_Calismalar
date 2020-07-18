import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

def bosh(x):
               pass
cv.namedWindow("BODY TrackBar")
cv.resizeWindow("BODY TrackBar",500,250)

cv.createTrackbar("Lower-H","BODY TrackBar",0,180,bosh)
cv.createTrackbar("Lower-S","BODY TrackBar",0,255,bosh)
cv.createTrackbar("Lower-V","BODY TrackBar",0,255,bosh)

cv.createTrackbar("Upper-H","BODY TrackBar",0,180,bosh)
cv.createTrackbar("Upper-S","BODY TrackBar",0,255,bosh)
cv.createTrackbar("Upper-V","BODY TrackBar",0,255,bosh)

cv.setTrackbarPos("Upper-H","BODY TrackBar",180)
cv.setTrackbarPos("Upper-S","BODY TrackBar",255)
cv.setTrackbarPos("Upper-V","BODY TrackBar",255)

while True:
               ret,frame =cam.read()
               frame = cv.flip(frame,1)
               hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

               lowh = cv.getTrackbarPos("Lower-H","BODY TrackBar")
               lows = cv.getTrackbarPos("Lower-S","BODY TrackBar")
               lowv = cv.getTrackbarPos("Lower-V","BODY TrackBar")

               uph = cv.getTrackbarPos("Upper-H","BODY TrackBar")
               ups = cv.getTrackbarPos("Upper-S","BODY TrackBar")
               upv = cv.getTrackbarPos("Upper-V","BODY TrackBar")

               lower_color = np.array([lowh,lows,lowv])
               upper_color = np.array([uph,ups,upv])

               masked = cv.inRange(hsv,lower_color,upper_color)

               cv.imshow("Original",frame)
               cv.imshow("Masked",masked)

               if cv.waitKey(27) & 0xFF==ord("q"):
                              break
cam.release()
cv.destroyAllWindows()
