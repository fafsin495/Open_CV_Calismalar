import cv2 as cv
import numpy as np

image = cv.imread("f16.jpg",0)

kernel = np.ones((5,5),np.uint8)

#Erosion metodu
# ön plandaki nesnenin sınırlarını aşındırır
#Küçük beyaz gürültüleri kaldırmak
#bağlı iki nesneyi çıkarmak vb şeyler için kullanılabilir
erosion = cv.erode(image,kernel,iterations=1)

# DİLATON
#erazyonun tam tersidir
#ön plandaki nesenenin boyutu artar
dilation = cv.dilate(image,kernel,iterations=1)

#Opening
#Açılma erozyonun ardından dilatasyonun başka adıdır
#Gürültü gidermede yararlıdır.

oppen = cv.morphologyEx(image,cv.MORPH_OPEN,kernel)
#CLOSİNG
#Ön plandaki nesnelerin içindeki küçük deliklerin veya nesnelerin üzrrindeki küçük siyah noktaların kapatılmasında faydalıdır

closing = cv.morphologyEx(image,cv.MORPH_CLOSE,kernel)

#Morphological Gradient
#dilation ve erasion un arasındaki farktır
gradient = cv.morphologyEx(image,cv.MORPH_GRADIENT,kernel)

#Tophat Metodu
tophat = cv.morphologyEx(image,cv.MORPH_TOPHAT,kernel)

#BlACK HAT
blackhat =cv.morphologyEx(image,cv.MORPH_BLACKHAT,kernel)

cv.imshow("TOPHAT Method",tophat)
cv.imshow("Erosion_metodu",erosion)
cv.imshow("DILATION_metodu",dilation)
cv.imshow("OPENING_metodu",oppen)
cv.imshow("CLOSING_metodu",closing)
cv.imshow("gradient_metodu",gradient)
cv.imshow("BLACKHAT MTODU",blackhat)

cv.waitKey(0)
cv.destroyAllWindows()
