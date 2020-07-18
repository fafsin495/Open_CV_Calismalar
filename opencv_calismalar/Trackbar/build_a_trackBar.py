import cv2 as cv
import numpy as np

def nothing (x):
               pass
#Siyah bir ekran ve pencere oluşturma
image = np.zeros((300,512,3),np.uint8)
cv.namedWindow("Pencere")

# Renk değişimleri için çubuklar (trackbar)

cv.createTrackbar("R","Pencere",0,255,nothing)
cv.createTrackbar("G","Pencere",0,255,nothing)
cv.createTrackbar("B","Pencere",0,255,nothing)
cv.createTrackbar("Ac-Kapa","Pencere",0,255,nothing)

while (1):
           cv.imshow("Picture",image)
           button = cv.waitKey(1) & 0xFF
# Esc tuşuna basılınca kapatılması için Asci koduyla
#if bloğunda döngüyü  durdurma komutunu yazıyoruz
                          
           if button == 27 :
               cv.destroyAllWindows()
               break
           r = cv.getTrackbarPos("R","Pencere")
           g = cv.getTrackbarPos("G","Pencere")
           b = cv.getTrackbarPos("B","Pencere")
           on_of = cv.getTrackbarPos("Aç-Kapat","Pencere")
           if  on_of == 0:
                          image[:] = 0
           else :
                          image[:]=[b,g,r]


