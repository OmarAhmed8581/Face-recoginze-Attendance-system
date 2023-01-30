

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
import cv2
import cv2
import numpy as np
import imageio
import os
from PIL import Image,ImageTk
from Controller import Global_Class


HEIGHT=650
WIDTH=770




#<------------------------------------------------------------- Connection file --------------------------------------->

connection=Global_Class.Global





def take_photo():
    
    face_cascade=cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    sample_images_count=0
    while True:
        ret ,img = cam.read()
        gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces=face_cascade.detectMultiScale(gray_scale,1.3,5)

        for (x,y,w,h) in faces:

            crop=gray_scale[y:y+h,x:x+w]
            cv2.rectangle(gray_scale,(x,y),(x+w,y+h),(255,0,0),2)
            sample_images_count+=1
        

            cv2.imwrite('D:\student_images/'+str(sample_images_count)+".jpg",crop)

            cv2.imshow("face detect",gray_scale)
            cv2.waitKey(1)
        if(sample_images_count>=4):
            break   

    cam.release()
    cv2.destroyAllWindows()

    

    


def error():
    messagebox.showerror('Error','All fields are required')

def Register(std_name,std_fathername,std_email,std_password,std_confirmpassword,std_phoneno,std_nic,std_city,std_address,std_program,student_Register_root):
    std_password_hash=hashlib.md5(std_password.encode('utf-8'))
    std_confirm_password_hash=hashlib.md5(std_confirmpassword.encode('utf-8'))
    std_pass_hexa=std_password_hash.hexdigest()
    std_confirmpas_hexa=std_confirm_password_hash.hexdigest()

    flat=0

   
    # email_pattern='[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})'
    # phone_no_pattern="\\d{4}[-.\s]?\\d{7}"

    if(std_name!="" and std_fathername != "" and std_email !="" and std_password != "" and std_confirmpassword != "" and std_phoneno != "" and std_nic != "" and std_city != "" and std_address != "" and std_program != ""):

        connection.cursor.execute('select STD_EMAIL from student_registeration_record')
        result=connection.cursor.fetchall()
        length=len(result)

        for email in range(0,length):
            if result[email][0]==std_email:
                flat=1
                messagebox.showinfo('Email Already exists Error','Email is Already exist')
                

            

        if flat==0:
            connection.cursor.execute('insert into student_registeration_record(STD_ID,STD_NAME,STD_FATHER_NAME,STD_EMAIL,STD_PASSWORD,STD_CONFIRM_PASSWORD,STD_PHONE_NO,STD_NIC,STD_CITY,STD_ADDRESS,STD_PROGRAM)values(?,?,?,?,?,?,?,?,?,?,?)',('NULL',std_name,std_fathername,std_email,std_pass_hexa,std_confirmpas_hexa,std_phoneno,std_nic,std_city,std_address,std_program))


            query="select max(ID) from student_registeration_record"
            connection.cursor.execute(query)
            max_id=connection.cursor.fetchall()

            student_id="BS-3-19-" + str(max_id[0][0])
            student_max_id=int(max_id[0][0])


            connection.cursor.execute('update student_registeration_record set STD_ID=? where ID=?',(student_id,student_max_id))
            # connection.cursor.commit()

            take_photo()



            m_id=student_max_id
            query="select COURSE_ID from course"
            connection.cursor.execute(query)
            result=connection.cursor.fetchall()
            lenght=len(result)

                
            if(lenght>0):
                for id in range(0,lenght):
                    connection.cursor.execute("insert into student_Assigned_course(STUDENT_ID_F,COURSE_ID_f) values(?,?)",(student_id,result[id][0]))



                
                # insert into student Images table

                for index in range(1,5):

                    student_images_path="D:\student_images/"+str(index)+".jpg"

                    with open(student_images_path,'rb') as f:
                        data=f.read()
                        #  images_data=str(data)

                    connection.cursor.execute("insert into student_images(STD_ID,STD_PHOTO) values(?,?)",(student_id,data))    



                messagebox.showinfo('Registered','Successfully registered')

                connection.cursor.commit()
                student_Register_root.destroy()
                import login
            
    else:
        messagebox.showerror("Error","fill the required")
            


        
        
