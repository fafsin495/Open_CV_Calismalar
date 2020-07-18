import cv2 as cv
import numpy as np

#Resmimizi imread ile okuyoruz
image = cv.imread("cat.png")
#resim üzerinden seçtiğimiz bölgeyi değişkene atayıp
roi = image[256:356,80:160]
#resim üzerinde belirlediğimiz bir alana bu değişkeni atıyoruz
image[0:100,300:380] = roi

cv.imshow("ROI",image)

cv.waitKey(0)
cv.destroyAllWindows()
