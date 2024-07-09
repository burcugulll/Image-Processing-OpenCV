
import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot

#1-Piksel okuma

img = cv2.imread("kertenkele.jpg")
dim = img.shape
print(dim) #satır sutun kanal
pxl = img[250,250,1] #1 yesildeki deger
img[250,250,1] = 250 #degistirme

b = img[:,:,0] #tum satir tum sutun 0.kanal
g = img[:,:,1]
r = img[:,:,2]

print(b)

cv2.imshow("Kertenkele", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

#2-Histogram
img = cv2.imread("cameraman.jpg")

img2 = cv2.imread("kertenkele.jpg")
b, g, r = cv2.split(img2)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

cv2.imshow("Cameraman", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#3-İlgi alanı
img = cv2.imread("brain.jpg")
img = cv2.resize(img,(480,480))
print(img.shape)

cv2.rectangle(img,(130,90),(210,200),(0,255,0),3)

cv2.imshow("Brain", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#4-Aritmetik işlemler

t = cv2.imread("tom2.jpeg")
j = cv2.imread("jerry2.jpeg")
tomandjerry = cv2.add(t, j)
tomandjerryWeighted = cv2.addWeighted(t, 0.7, j, 0.3, 0)
print("Tom shape: ", t.shape)
print("Jerry shape: ", j.shape)

cv2.imshow("Tom", t)
cv2.imshow("Jerry", j)
cv2.imshow("Tom and Jerry", tomandjerry)
cv2.imshow("Tom and Jerry Weighted", tomandjerryWeighted)

img = cv2.imread("cameraman.jpg")
imgAdded = cv2.add(img, 50)
imgMinus = cv2.add(img, -100)

cv2.imshow("Orjinal", img)
cv2.imshow("Added", imgAdded)
cv2.imshow("Minus", imgMinus)

cv2.waitKey(0)
cv2.destroyAllWindows()

#5-Mantıksal Operatörler
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

imgAnd = cv2.bitwise_and(img2, img1)
imgOr = cv2.bitwise_or(img2, img1)
imgNot = cv2.bitwise_not(img2)

cv2.imshow("img 1", img1)
cv2.imshow("img 2", img2)
cv2.imshow("imgAnd", imgAnd)
cv2.imshow("imgOr", imgOr)
cv2.imshow("img2Not", imgNot)

cv2.waitKey(0)
cv2.destroyAllWindows()

#6-Görüntü Döndürme
img = cv2.imread("cameraman.jpg", cv2.IMREAD_GRAYSCALE)
r, c = img.shape

rotationRules = cv2.getRotationMatrix2D((c/2, r/2), 90, 1)
rotatedImg = cv2.warpAffine(img, rotationRules, (c, r))

cv2.imshow("Cameraman", img)
cv2.imshow("Rotated Cameraman", rotatedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
