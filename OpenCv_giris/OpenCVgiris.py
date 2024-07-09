from cv2 import cv2
import time
#resim okuma
#img=cv2.imread("kertenkele.jpg")#gorüntü okuma
#img=cv2.imread("kertenkele.jpg",cv2.IMREAD_GRAYSCALE)#görüntüyü gri olarak okur
img=cv2.imread("cameraman.jpg")
cv2.imwrite("kameraman gri seviye.jpg",img)
#print(img)
cv2.namedWindow("Hayvan",cv2.WINDOW_NORMAL)#pencereyi büyültüp küçültebilme
cv2.imshow("Hayvan",img)#ekrana basma- pencere ismi
cv2.waitKey(0)#1000 yazarsak=1sn ekranda gözüküp gidiyor 0 yazarsak ekranda sabit
cv2.destroyAllWindows()#kullanılan pencereleri kapatır

"""
#video okuma
#web camden okuma
#movie=cv2.VideoCapture(0)#canlı görüntü okumak için tek kamera varsa 0 harici 1 tane daha varsa 1
movie=cv2.VideoCapture(0,cv2.CAP_DSHOW)#video okunduğunda hata değil parametre veriyorsa q ya basıldığında kapanınca uyarı verdiği için
while True:
   state,frame=movie.read()
   frame=cv2.flip(frame,1)#yansıtma
   cv2.imshow("Camera",frame)
   #cv2.waitKey(30)#yazılan sayı yazarsa yavaşlar 0 olduğunda ilk görüntüyü alır ve sadece onu gösterir
   if cv2.waitKey(30) & 0xFF ==ord("q"):#q ya basıldığında düzgün kapanır o*ff karşılığı q
       break
movie.release()#serbest bırakma başka kullanımlara açılması için
movie.destroyAllWindows()

"""
#kaydedilmiş video okuma
movie=cv2.VideoCapture("malesia.mp4")
while True:
    state,frame=movie.read()
    frame=cv2.resize(frame,(480,480))#görüntüyü küçülttük
    if state==0:#video sonuna gelindiyse
        break
    cv2.imshow("Malezya",frame)
    if cv2.waitKey(30) & 0xFF ==ord("q"):
        break
movie.release()
cv2.destroyAllWindows()
"""
video_name="malesia.mp4"
cap=cv2.VideoCapture(video_name)
print("Genişlik:",cap.get(3))
print("Yükseklik:",cap.get(4))

if cap.isOpened()==False:
    print("Hata")
while True:#sonsuz döngüye soktuk videoya dönüşmesi için
    ret,frame=cap.read()
    if ret==True:
        time.sleep(0.01)#yavaşlatma
        cv2.imshow("Video",frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cap.release() #videyo bıraktık
cv2.destroyAllWindows()# tüm pencereleri kapattık
"""

