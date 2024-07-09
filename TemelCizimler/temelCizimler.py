import cv2
import numpy

#Sahne Oluşturma
screen=numpy.zeros((512,512,3),dtype=numpy.uint8)+255#beyaz sahne için 255 ekledik zeros o lardan oluşan dizi oluşturur 3 rengi 512-512 boyutu
#print(screen)
#open cv görüntüler BGR olrak tutuluyor

#Çizgi Çizdirme
cv2.line(screen,(25,25),(100,25),(25,125,255),thickness=1)#(nereye çizileceği,başlangıç noktası x-y,bitiş noktası x-y,renkBGR,kalınlık)
cv2.line(screen,(25,100),(100,255),(0,0,255),3)

#Dikdörtgen Çizme
cv2.rectangle(screen,(75,75),(175,175),(255,0,0),2)#(nereye çizileceği,sol üst,sağ alt,renk,kalınlık)
cv2.rectangle(screen,(300,300),(400,400),(0,255,0),-1)#kalınlık -1 olunca içini boyuyor

#Çember Çizdirme
cv2.circle(screen,(256,256),50,(245,14,200),thickness=2)#(nereye çizileceği,merkez,yarıçap,renk,kalınlık)

#Elips Çizdirme
cv2.ellipse(screen,(250,400),(50,20),45,0,270,(0,0,0),-1)#(çizileceği yer,merkez noktası,yatay yarıçap-düşey yarıçap,yatayla eğim,başlangıç,bitiş,renk,kalınlık
cv2.ellipse(screen,(150,400),(50,20),0,0,360,(0,255,0),-1)

#Üçgen Çizme
x=(255,50)
y=(200,150)
z=(300,150)

cv2.line(screen,x,y,(0,0,255),2)
cv2.line(screen,y,z,(0,0,255),2)
cv2.line(screen,z,x,(0,0,255),2)

#Çokgen Çizme
points=numpy.array([[50,350],[100,350],[125,375],[75,400]],numpy.int32)#dörtgen çizer numpy int 32 sayısal değer
cv2.polylines(screen,[points],True,(125,125,125),2)#true kapalı false açık

#Yazı Yazma
cv2.putText(screen,"Goruntu Isleme",(50,500),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)#(çizileceği yer,yazı,sol alt nokta,yazılacağı tip,double değer-kalınlık,renk,çizgi tipi

cv2.imshow("Screen",screen)
cv2.waitKey(0)
cv2.destroyAllWindows()
