import cv2 as cv
import numpy as np

image1 = cv.imread("2.jpg")
image2 = cv.imread("cats.jpg")

image3 = image2[0:370,0:366]

# burada 0.6 ve 0.4 ün bulunduğu değişkenler katmanların saydamlıklarını ifade ediyor
# ve bu iki değerin toplamının 1 değerini geçmemesi gerekiyor
#print("ilk",image1.shape)
#print("ikinci",image2.shape)
#print(image3.shape)
combining = cv.addWeighted(image1,0.4,image3,0.6,0)

cv.imshow("Combined_Photo",combining)
cv.waitKey(0)
cv.destroyAllWindows()
