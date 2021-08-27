import cv2
import numpy as np
from PIL import Image as Img
import pickle
import sqlite3


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer\\trainningData.yml")
cascadePath="Classifiers/face.xml"
faceCascade=cv2.CascadeClassifier(cascadePath);
path='dataSet'

def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    query="SELECT * FROM Kisiler WHERE Id="+str(id)
    cursor=conn.execute(query)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile
        
cam=cv2.VideoCapture(0);
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if conf<70:           
            if profile!=None:
                cv2.putText(img,str(profile[1]),(x,y+h+30), font, 1,(255,255,255))
                cv2.putText(img,str(profile[2]),(x,y+h+60), font, 1,(255,255,255))
                cv2.putText(img,str(profile[3]),(x,y+h+90), font, 1,(255,255,255))
                cv2.putText(img,str(profile[4]),(x,y+h+120), font, 1,(255,255,255))
                cv2.putText(img,str(profile[5]),(x,y+h+150), font, 1,(255,255,255))
        else:
             cv2.putText(img,str('unknown'),(x,y+h+30), font, 1,(255,255,255))
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
