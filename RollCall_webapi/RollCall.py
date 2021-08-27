from tkinter import *
import datetime
from tkinter import Menu
import sqlite3
import cv2
import numpy as np
from PIL import Image as Img
import pickle
import os
import time

def close():
    exit()

window=Tk()
window.title('GUI') 
width = 550
height = 450
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window['bg']="#59C2CF"


#---Course Start Function-----
def CourseStart(): 
    global tabloadi
    tabloadi=inputdersadi.get()+inputsinifadi.get()+inputderstarihi.get()
    global GirisSaati
    GirisSaati=time.strftime("%X")
    print(tabloadi)
    conn = sqlite3.connect("accountsdb.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE {tab}
         (Id INT PRIMARY KEY     NOT NULL,
          Zaman  TEXT NOT NULL,
          AdSoyad   TEXT    NOT NULL,
          No            INT     NOT NULL,
          Bolum        TEXT NOT NULL,
          Yas         INT,
          Cinsiyet Text);'''.format(tab=tabloadi))
        print ("Table created successfully")
        cursor.close()
        conn.commit()   
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
                        cv2.putText(img,str(profile[4]),(x,y+h+120),font, 1,(255,255,255))
                        cv2.putText(img,str(profile[5]),(x,y+h+150),font, 1,(255,255,255))

                        con=sqlite3.connect("accountsdb.db")
                        cursor=con.cursor()
                        cursor.execute("SELECT * FROM "+tabloadi+" WHERE Id="+str(profile[0]))
                        isRecordExist=0
                        for row in cursor:
                            isRecordExist=1
                        if(isRecordExist==1):
                             print('Derste böyle bir kişi var.')
                        else:
                            params = (profile[0], GirisSaati,  profile[1], profile[2], profile[3],profile[4],profile[5])
                            cursor.execute("INSERT INTO "+tabloadi+" VALUES (?,?, ?, ?, ?, ?, ?)", params)
                        con.commit()
                        con.close()
                  
                else:
                    cv2.putText(img,str('unknown'),(x,y+h+30), font, 1,(255,255,255))
            cv2.imshow("Dersi bitirmek icin 'E' tuslayiniz.",img);
            if(cv2.waitKey(1)==ord('e') or cv2.waitKey(1)==ord('E')):
                    break
                    cam.release()
                    cv2.destroyAllWindows()
        cam.release()
        cv2.destroyAllWindows()
    except sqlite3.OperationalError as e:
        print('Error: Daha önce böyle bir ders kaydı oluşturulmuş veya noktalama hatası yapılmıştır.')
#-----------------------------
#-----COURSE START FORM ------
def CourseStartForm():
    def back():
        coursewindow.destroy()
        window.deiconify()
    window.withdraw()
    coursewindow=Tk()
    coursewindow.title('GUI')
    width = 550
    height = 450
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    coursewindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    coursewindow['bg']="#59C2CF"
    menu = Menu(coursewindow)
    menu.add_cascade(label='Geri', command=back)
    coursewindow.config(menu=menu)

    dateLabel = Label(coursewindow,bg="#59C2CF", text="Öğrenci", width=10)
    dateLabel.grid(row=0, column=0)
    BMILabel = Label(coursewindow,bg="#59C2CF", text="Saat", width=10)
    BMILabel.grid(row=0, column=1)
    stateLabel = Label(coursewindow,bg="#59C2CF", text="Ad Soyad", width=10)
    stateLabel.grid(row=0, column=2)
    stateLabel = Label(coursewindow,bg="#59C2CF", text="No", width=10)
    stateLabel.grid(row=0, column=3)
    stateLabel = Label(coursewindow,bg="#59C2CF", text="Bolum", width=10)
    stateLabel.grid(row=0, column=4)
    stateLabel = Label(coursewindow,bg="#59C2CF", text="Yas", width=10)
    stateLabel.grid(row=0, column=5)
    stateLabel = Label(coursewindow,bg="#59C2CF", text="Cinsiyet", width=10)
    stateLabel.grid(row=0, column=6)
    con=sqlite3.connect("accountsdb.db")
    cursor=con.cursor()
    def readfromdatabase():
        cursor.execute("SELECT * FROM "+tabloadi)
        return cursor.fetchall()
    data = readfromdatabase()
    for index, dat in enumerate(data):
        Label(coursewindow,bg="#59C2CF", text=dat[0]).grid(row=index+1, column=0)
        Label(coursewindow,bg="#59C2CF", text=dat[1]).grid(row=index+1, column=1)
        Label(coursewindow,bg="#59C2CF", text=dat[2]).grid(row=index+1, column=2)
        Label(coursewindow,bg="#59C2CF", text=dat[3]).grid(row=index+1, column=3)
        Label(coursewindow,bg="#59C2CF", text=dat[4]).grid(row=index+1, column=4)
        Label(coursewindow,bg="#59C2CF", text=dat[5]).grid(row=index+1, column=5)
        Label(coursewindow,bg="#59C2CF", text=dat[6]).grid(row=index+1, column=6)
    con.commit()
    con.close()

#------------------------
#-----MAIN FORM ---------
menu = Menu(window)
ders_islemleri = Menu(menu)
close_menu = Menu(menu)
menu.add_cascade(label='Ders İşlemleri', menu=ders_islemleri)
ders_islemleri.add_separator()
ders_islemleri.add_command(label='Ders Yoklama Çizelgeleri', command=CourseStartForm)
ders_islemleri.add_separator()

menu.add_cascade(label='Çıkış', command=close)


window.config(menu=menu)
inputdersadi = StringVar()
inputsinifadi=StringVar()
inputderstarihi = StringVar()
inputderstarihi.set(datetime.date.today().strftime("%d%B%Y"))

lbl_DersTarihi = Label(window, bg="#59C2CF", text = "Ders Tarihi :",
                         width="20", fg="#154360", font="Verdana 10 bold").place(x=15,y=20)
lbl_DersTarihi=Label(window ,width="20", textvariable = inputderstarihi,  
                   fg="#12CBC4",
                   font="Verdana 10 bold" ).place(x=195,y=20)
lbl_DersAdi = Label(window, bg="#59C2CF", text = "Ders Kodu :", width="20",
                   fg="#154360",
                   font="Verdana 10 bold").place(x=14,y=60)
txt_inputDersAdi=Entry(window, textvariable=inputdersadi, width="20", 
                   fg="#148F77",
                   font="Verdana 10 bold").place(x=195,y=60)
lbl_dersornek=Label(window, width="10", text="Ör:EMY244",bg="#59C2CF",
                   fg="#148F77",
                   font="Verdana 10").place(x=385,y=60)
lbl_SınıfAdi = Label(window, bg="#59C2CF", text = "Sınıf Adı :", width="20",
                   fg="#154360",
                   font="Verdana 10 bold").place(x=8,y=100)
txt_inputSınıfAdi=Entry(window, textvariable=inputsinifadi, width="20", 
                   fg="#148F77",
                   font="Verdana 10 bold").place(x=195,y=100)
lbl_sınıfornek=Label(window, width="7", text="Ör:NOB",bg="#59C2CF",
                   fg="#148F77",
                   font="Verdana 10").place(x=385,y=100)
iconstart=PhotoImage(file="compose-icon.png")
bt1=Button(window, command=CourseStart, border=0,text="Dersi Başlat",
           image=iconstart, highlightcolor="#4cae4c", width="120",
           fg="White",
           compound=LEFT, font="Verdana 10",
           bg="#FE7279",
           ).place(x=250, y=150)
window.mainloop()
#------------------------
