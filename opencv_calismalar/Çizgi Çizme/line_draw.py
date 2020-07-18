import cv2 as cv
import numpy as np

#512X512 boyutunda RGB (3) renk alabilen bir matris oluşturuyoruz
#Siyah ekranımızı oluşturuyoruz
image = np.zeros((512,512,3),np.uint8)

#Basit doğrusal bir çizgi çizebilmek için line metodunu kullanıyoruz
#ilk parantezde çizgimizin başlaacağı noktayı
#bir sonraki parantezde bitireceğimz noktayı
#sonraki parantez ise hangi renkte çizgiyi çekeceğimizi giriyoruz
#5,parametresi ise çizgimizin kalınlığını ifade ediyor
cv.line(image,(0,0),(360,480),(100,0,0),5)

cv.imshow ("Line_Draw",image)
