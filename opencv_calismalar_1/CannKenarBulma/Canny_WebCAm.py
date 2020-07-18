import cv2 as cv

cam = cv.VideoCapture(0)

while(True):
               ret,frame = cam.read()
               frame = cv.flip(frame,1)#görüntüyü y ekseninde çeviriyoru

               canny = cv.Canny(frame,150,200)
               cv.imshow("Frame",frame)
               cv.imshow("Canny",canny)

               if cv.waitKey(27) & 0xFF == ord("q"):
                              break
cam.release()
cv.destroyAllWindows()
               
