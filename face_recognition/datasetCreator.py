import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,AdSoyad,No,Bolum,Yas,Cinsiyet):
    conn=sqlite3.connect("FaceBase.db")
    query="SELECT * FROM Kisiler WHERE Id="+str(Id)
    cursor=conn.execute(query)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        query="UPDATE Kisiler SET AdSoyad='"+str(AdSoyad)+"' , No='"+str(No)+"', Bolum='"+str(Bolum)+"' ,  Yas='"+str(Yas)+"', Cinsiyet='"+str(Cinsiyet)+"'  WHERE Id="+str(Id)
    else:
        query="INSERT INTO Kisiler (Id,AdSoyad,No,Bolum,Yas,Cinsiyet) Values('"+str(Id)+"','"+str(AdSoyad)+"','"+str(No)+"','"+str(Bolum)+"', '"+str(Yas)+"', '"+str(Cinsiyet)+"' )"
                                                                    
    conn.execute(query)
    conn.commit()
    conn.close()

    
id=input('kullanici id giriniz:')
adsoyad=input('Ad Soyad giriniz:')
no=input('No giriniz:')
bolum=input('Bolum giriniz:')
yas=input('Yaş giriniz:')
cinsiyet=input('Cinsiyet giriniz E/K):')
insertOrUpdate(id,adsoyad,no,bolum,yas,cinsiyet)
sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>20) or (cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
