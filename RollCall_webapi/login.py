import sqlite3
from tkinter import *
from PIL import ImageTk,Image
import os
        
window=Tk()
window.title('LOGIN')
width = 350
height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

window.geometry("%dx%d+%d+%d" % (width, height, x, y))

window['bg']="Tomato"

def Login():

    global conn, cursor
    conn = sqlite3.connect("accountsdb.db")
    cursor = conn.cursor()     
    cursor.execute("SELECT * FROM `Kullanicilar` WHERE `KAdi` = 'admin' AND `Sifre` = 'admin'")


    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `Kullanicilar` WHERE `KAdi` = ? AND `Sifre` = ?", (USERNAME.get(), PASSWORD.get()))
        if USERNAME.get()=="":
            lbl_text.config(text="boş")
        if cursor.fetchone() is not None:
            HomeWindow()        
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Geçersiz kullanıcı adı veya şifre.", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
def loginquit():
    window.destroy()

def HomeWindow():
    def back():
        Home.destroy()
        window.deiconify()
    def datasetCreator():
        os.startfile('datasetCreator.py')
    def trainner():
        os.startfile('trainner.py')
    def detector():
        os.startfile('detector.py')
    window.withdraw()
    Home=Tk()
    Home.title('GUI')
    width = 300
    height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Home['bg']="Tomato"


    bt1=Button(Home, text="datasetCreator", width="16",
               fg="LightGray", font="Verdana 12 bold",
           bg="DodgerBlue"  ,
           command=datasetCreator).place(x=60, y=40)
    bt2=Button(Home, text="trainner", width="16",
               fg="LightGray", font="Verdana 12 bold",
           bg="DodgerBlue" ,
           command=trainner).place(x=60, y=80)
    bt3=Button(Home, text="detector", width="16",
               fg="LightGray", font="Verdana 12 bold",
           bg="DodgerBlue" ,
           command=detector).place(x=60, y=120)  
    bt4=Button(Home, text="Back", width="16",
               fg="white", font="Verdana 12 bold",
           bg="#c91d12" ,
           command=back).place(x=60, y=160)

USERNAME = StringVar()
PASSWORD = StringVar()
lbl_username = Label(window, bg="Tomato", text = "Username:",
                     width="10", fg="LightGray",
                     font="Verdana 12 bold").place(x=15,y=20)
username=Entry(window, textvariable=USERNAME, width="16",
               fg="DodgerBlue", font="Verdana 12 bold" ).place(x=125,y=20)
lbl_password = Label(window, bg="Tomato", text = "Password:",
                     width="10", fg="LightGray",
                     font="Verdana 12 bold").place(x=15,y=60)
password=Entry(window,textvariable=PASSWORD, show="*",
               width="16", fg="DodgerBlue",
               font="Verdana 12 bold").place(x=125,y=60)

bt1=Button(window, text="login", width="10",
           fg="LightGray", font="Verdana 12 bold",
           bg="DodgerBlue",
           command=Login).place(x=185, y=120)
bt2=Button(window, text="Quit", width="10", fg="LightGray",
           font="Verdana 12 bold",
           bg="DodgerBlue",
           command=loginquit).place(x=50, y=120)
lbl_text = Label(window,text="", font="Verdana 8 bold",)
lbl_text.grid(row=2, columnspan=2)

window.mainloop()
 #try:
   #        c.execute('''CREATE TABLE IF NOT EXISTS inputdersadi.get() (
       #          id PRIMARY KEY,
       #          name VARCRCHAR(100) UNIQUE NOT NULL,
        #         employees INTEGER DEFAULT 0)''')
       #  except sqlite3.OperationalError as e:
       #       print('sqlite error:', e.args[0])
              # table companies already exists 
