import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
# from tkinker import StringVar
#from tk import *
import tkinter.font as font
import pyodbc
from PIL import Image,ImageTk
import numpy as np
import cv2 
from Controller import Global_Class



#<-------------------------------------------------- Connection File --------------------------------------------------->




Conection=Global_Class.Global





def get_images_database(id,course):
    face_cascade = cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('D:\haarcascade_eye.xml')  


    Conection.cursor.execute("select std_id,std_photo from  student_registeration_record where std_id=?",(id))
    result=Conection.cursor.fetchall()
    id=result[0][0]
    photo=result[0][1]




    Student_id=str(id)
    student_course=course
    path='D:/course/'+student_course+'/'+Student_id+'.jpg'
    with open(path,'wb') as m:
        m.write(photo)
   
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    width = 100
    height =128


    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


        cv2.imwrite(path, roi_color)
        # to convert in a gray scale
        image=Image.open(path)
        gray_scale=image.convert(mode='L')

        gray_scale.save(path)


        stdfilee=Image.open(path)
        im2 = stdfilee.resize((width, height), Image.NEAREST)
        file_name=path
        im2.save(file_name)
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.destroyAllWindows()



def set_images_database():
    face_cascade = cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('D:\haarcascade_eye.xml')

    













         




