import cv2
import numpy


def emptyFunc(x):
    pass#hiçbişey yapmıyo sadece fonk oluşturduk

cv2.namedWindow("Screen")
cv2.createTrackbar("F-Size","Screen",25,250,emptyFunc)#(isim,yerleşceği yer,değer,fonk parametresi)

fs=0.25
while True:
    img=numpy.zeros((512,512,3),dtype=numpy.uint8)+255
    cv2.putText(img,"OPEN-CV",(100,255),cv2.FONT_HERSHEY_SIMPLEX,fs,(0,0,255),cv2.LINE_4)#fs text büyüklüüğü
    cv2.imshow("Screen",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    fs=cv2.getTrackbarPos("F-Size","Screen")#get ile değer elde ediyoruz ismini yazıyoruz
    fs=fs/100#double değer istiyoruz


cv2.destroyAllWindows()