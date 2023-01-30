import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import re
from PIL import Image,ImageTk
import tkinter.font as font
from tkinter import filedialog
import pyodbc
import os
import hashlib
import cryptography
from cryptography.fernet import Fernet
HEIGHT=650
WIDTH=770
from Controller import Global_Class
import formatting_constant 



c=formatting_constant.constant


#<------------------------------------------------------------- Connection file --------------------------------------->

Conection=Global_Class.Global





#<--------------------------------------------------------------- Student Register Form ------------------------------->


def Faculty_Register():

    def error():
        messagebox.showerror('Error','All fields are required')
#----------------------------------------------------------------------

    def faculty_register():
       
        faculty_name=name_txt.get()
        faculty_fathername=fathername_txt.get()
        faculty_email=email_txt.get()
        faculty_password=password_txt.get()
        faculty_confirmpassword=confirmpassword_txt.get()
        faculty_phone_no=phone_txt.get()
        faculty_NIC=NIC_txt.get()
        faculty_Desgination=designation_txt.get()
        faculty_Current_insititue= subject_txt.get()  
        faculty_address=address_txt.get()
        faculty_Quanlification=qualification_txt.get()
        

        faculty_password_hash=hashlib.md5(faculty_password.encode('utf-8'))
        faculty_confirmpassword_hash=hashlib.md5(faculty_confirmpassword.encode('utf-8'))
        faculty_pass_hexa=faculty_password_hash.hexdigest()
        faculty_confirmpas_hexa=faculty_confirmpassword_hash.hexdigest()
   

        email_pattern='[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})'
        phone_no_pattern="\\d{4}[-.\s]?\\d{7}"

    
        if faculty_name==""or faculty_fathername=="" or faculty_email=="" or faculty_password=="" or faculty_confirmpassword=="" or faculty_address=="" or faculty_Quanlification  =="" or faculty_NIC=="" or faculty_phone_no=="" or faculty_Desgination=="" or faculty_Current_insititue=="":
            error()
        

        elif not re.search(email_pattern,faculty_email):
            messagebox.showinfo('Email Address Error','Incorrect email address')
        
        elif faculty_password==faculty_confirmpassword:
            Conection.cursor.execute('insert into faculty_registeration_record(FACULTY_NAME,FACULTY_EMAIL,FACULTY_PASSWORD,FACULTY_CONFIRM_PASSWORD,FACULTY_PHONE_NO,FACULTY_NIC,FACULTY_DESIGNATION,FACULTY_CURRENT_INSITITUE,FACULTY_ADDRESS,FACULTY_QUALIFICATION)values(?,?,?,?,?,?,?,?,?,?)',(faculty_name,faculty_email,faculty_pass_hexa,faculty_confirmpas_hexa,faculty_phone_no,faculty_NIC, faculty_Desgination,faculty_Current_insititue, faculty_address,faculty_Quanlification))
            messagebox.showinfo('Registered','Successfully registered')
            Conection.cursor.commit()
            root.destroy()
            import login

        else:
            messagebox.showinfo('Password Error','Password is not matched')


#----------------------------------------------------------------------

 

    root=tk.Tk()
    root.title("Admin form")
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
    root.focus_set() 

    canvas = tk.Canvas(root, height=c.form_height, width=c.form_width,)
    canvas.pack()


    Fontlabel = font.Font(family=c.family, size=13, )
    Fontlabel1 = font.Font(family=c.family, font=8, )



    
    frame=tk.Frame(root,bg=c.frame_bg)
    frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width_std_reg,relheight=c.frame_height)

    headframe=tk.Frame(frame,bg='white')
    headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)




    leftframe=tk.Frame(frame,bg=c.left_Frame_label_bg)
    leftframe.place(relx=0.0,rely=0.02,relwidth=c.register_leftframe_width,relheight=c.register_leftframe_height)
    
    def on_click(event=None):
        root.destroy()
#cross symbol
    file_name="D:\FYP_project_temp\images\\crossicon.png"
    stdfilee=Image.open(file_name)
    stdshow=ImageTk.PhotoImage(stdfilee)
    imageshow=tk.Label(image=stdshow)
    imageshow.bind('<Button-1>', on_click)
    imageshow.image=stdshow
    imageshow.place(relx=0.98,rely=0.0)

    def login_back(event=None):
        import login
        login.Login()
#back 
    file_name="D:\FYP_project_temp\images\\back.png"
    stdfilee=Image.open(file_name)
    stdshow=ImageTk.PhotoImage(stdfilee)
    imageshow=tk.Label(image=stdshow)
    imageshow.bind('<Button-1>', login_back)
    imageshow.image=stdshow
    imageshow.place(relx=0.02,rely=0.03)

#icon
    file_name="D:\FYP_project_temp\images\\reg_logo.jpeg"
    stdfilee=Image.open(file_name)
    stdshow=ImageTk.PhotoImage(stdfilee)
    imageshow=tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)




    leftframelabel1=tk.Label(leftframe,text="Make an account",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel1['font']=Fontlabel
    leftframelabel1.place(relx=0.3,rely=0.3)

    leftframelabel2=tk.Label(leftframe,text="to connect with us",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel2['font']=Fontlabel
    leftframelabel2.place(relx=0.3,rely=0.4)


    mainframelabel=tk.Label(frame,text='Create your account here',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=Fontlabel
    mainframelabel.place(relx=0.5,rely=0.1)


    string=tk.StringVar()
    name_lbl=tk.Label(frame,text="Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    name_lbl.place(relx=0.5,rely=0.2)
    name_txt=ttk.Entry(frame,textvariable=string,text="")
    name_txt.place(relx=0.68,rely=0.2,relwidth=c.register_textbox_width)

    fathername_lbl=tk.Label(frame,text="Father Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    fathername_lbl.place(relx=0.5,rely=0.27)
    fathername_txt=ttk.Entry(frame,textvariable=string,text="")
    fathername_txt.place(relx=0.68,rely=0.27,relwidth=c.register_textbox_width)

    email_lbl=tk.Label(frame,text="Email Address",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    email_lbl.place(relx=0.5,rely=0.33)
    email_txt=ttk.Entry(frame,textvariable=string,text="",)
    email_txt.place(relx=0.68,rely=0.33,relwidth=c.register_textbox_width)


    password_lbl=tk.Label(frame,text="Password",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    password_lbl.place(relx=0.5,rely=0.39)
    password_txt=ttk.Entry(frame,textvariable=string,text="",show='*')
    password_txt.place(relx=0.68,rely=0.39,relwidth=c.register_textbox_width)

    confirmpassword_lbl=tk.Label(frame,text="Confirm Password",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    confirmpassword_lbl.place(relx=0.5,rely=0.46)
    confirmpassword_txt=ttk.Entry(frame,textvariable=string,text="",show='*')
    confirmpassword_txt.place(relx=0.68,rely=0.46,relwidth=c.register_textbox_width)


    phone_lbl = tk.Label(frame, text="Phone Number", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    phone_lbl.place(relx=0.5,rely=0.52)
    phone_txt = ttk.Entry(frame, textvariable=string, text="")
    phone_txt.place(relx=0.68,rely=0.52,relwidth=c.register_textbox_width)


    NIC_lbl = tk.Label(frame, text="NIC", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    NIC_lbl.place(relx=0.5,rely=0.58)
    NIC_txt = ttk.Entry(frame, textvariable=string, text="")
    NIC_txt.place(relx=0.68,rely=0.58,relwidth=c.register_textbox_width)

    designation_lbl = tk.Label(frame, text="Designation", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    designation_lbl.place(relx=0.5,rely=0.64)
    designation_txt = ttk.Entry(frame, textvariable=string, text="")
    designation_txt.place(relx=0.68,rely=0.64,relwidth=c.register_textbox_width)

    subject_lbl = tk.Label(frame, text="Current Insititue", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    subject_lbl.place(relx=0.5,rely=0.70)
    subject_txt = ttk.Entry(frame, textvariable=string, text="")
    subject_txt.place(relx=0.68,rely=0.70,relwidth=c.register_textbox_width)

    address_lbl=tk.Label(frame, text="Address", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    address_lbl.place(relx=0.5,rely=0.76)
    address_txt = ttk.Entry(frame, textvariable=string, text="")
    address_txt.place(relx=0.68,rely=0.76,relwidth=c.register_textbox_width)

    qualification_lbl=tk.Label(frame, text="Qualification", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    qualification_lbl.place(relx=0.5,rely=0.82)
    qualification_txt = ttk.Entry(frame, textvariable=string, text="")
    qualification_txt.place(relx=0.68,rely=0.82,relwidth=c.register_textbox_width)

    


    
    signup_btn=tk.Button(frame,text="Sign up",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg,command=faculty_register)
    signup_btn['font']=Fontlabel1
    signup_btn.place(relx=0.68,rely=0.88,relwidth=c.register_textbox_width)




    root.mainloop()

Faculty_Register()



