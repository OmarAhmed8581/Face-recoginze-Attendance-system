#<------------------------------------------------------- Import File ---------------------------------------------->

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import os
import os.path
import pyodbc
from PIL import Image,ImageTk
import tkinter.font as font
import hashlib
from cryptography.fernet import Fernet
from Controller import Global_Class
import formatting_constant 



c=formatting_constant.constant

#<-------------------------------------------------- Connection File --------------------------------------------------->


p1=Global_Class.Global

#<-----------------------------------------    Login Form -------------------------------------------------------->

def Login():


    
   


    root=tk.Tk()
    root.title("LOGIN FORM")

    
    root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))

  

    def Register():
        user=cb.get()
        if(user=='Faculty'):
            root.destroy()
            import Teacher_Register
            Teacher_Register.Faculty_Register()
        elif(user=='Student'):
            root.destroy()
            import student_registeration
            student_registeration.Student_Register()
            

    def loginn(event=None):
    
        email_address=Email_txt.get()
        passwordd=Password_txt.get()
        user=cb.get()
        from Controller import login_Validation
        login_Validation.Login(email_address,passwordd,user,root)



    canvas = tk.Canvas(root, height=c.form_height, width=c.form_width,bg="#6D3079")
    canvas.pack()

    #background image
    # load=Image.open('images/bgpics.jpg')
    # render=ImageTk.PhotoImage(load)
    
    # img=tk.Label(image=render)
    # img.image=render
    # img.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg= c.frame_bg)
    frame.place(relx=0.2, rely=0.3, relwidth=c.frame_width, relheight=c.frame_height)

    Fontlabel = font.Font(family=c.family, size=25, weight='bold')

    # headerlabel=tk.Label(root,text="ATTENDANCE SYSTEM BY FACE RECOGNITION",font=c.headerlabel_font, fg=c.headerlabel_fg)
    # headerlabel['font']=Fontlabel
    # headerlabel.place(relx=0.00,rely=0.00)


    # label=tk.Label(root,text="LOGIN FORM",font=c.headerlabel_font,fg=c.label_fg,)
    # label['font']=Fontlabel
    # label.place(relx=0.32,rely=0.20)


    ##logo image
    # loadd=Image.open('reg_logo.png')
    # renderr=ImageTk.PhotoImage(loadd)
    # imgg=tk.Label(image=renderr)
    # imgg.image=renderr
    # imgg.place(relx=0.40,rely=0.20)

    cblable=tk.Label(frame,text="Login As?",font=c.label_font,fg=c.label_fg)
    cblable.place(relx=0.20,rely=0.07)
    userlogin=["Faculty","Student","Admin"]
    cb=ttk.Combobox(root,values=userlogin,width=c.combox_width)
    cb.place(relx=0.44,rely=0.34,relwidth=c.textbox_width)


    # def func():
    #     l2.configure(text=cb.get())

    string=tk.StringVar()
    label1=tk.Label(frame,text="Email",font=c.label_font,fg=c.label_fg)
    label1.place(relx=0.20,rely=0.16)
    #Email_txt=ttk.Entry(root,textvariable=string,text="")
    Email_txt=ttk.Entry(root,textvariable=string)
    Email_txt.place(relx=0.44,rely=0.40,relwidth=c.textbox_width)



    label2=tk.Label(frame,text="Password",font=c.label_font,fg=c.label_fg)
    label2.place(relx=0.20,rely=0.25)
    #Password_txt=EntryWithPlaceholder(root,"Enter your password")
    Password_txt=ttk.Entry(root,textvariable=string,text="paswword",show='*')
    Password_txt.place(relx=0.44,rely=0.45,relwidth=c.textbox_width)



    myFont = font.Font(family=c.family, size=c.button_font, weight=c.button_style)

    button=tk.Button(frame,text="LOGIN",command=loginn,bg=c.button_bg,fg=c.button_fg)
    button['font']=myFont
    button.place(relx=0.22,rely=0.35,relwidth=c.button_width,relheight=c.button_height)

    button_register=tk.Button(frame,text="Register",bg=c.button_bg,fg=c.button_fg,command=Register)
    button_register['font']=myFont
    button_register.place(relx=0.50,rely=0.35,relwidth=c.button_width,relheight=c.button_height)


    root.mainloop()
Login()

