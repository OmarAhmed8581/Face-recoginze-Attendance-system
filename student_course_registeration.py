#<------------------------------------------------------ Import file ------------------------------------------------->
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import * 
# from tkinker import StringVar
#from tk import *
import tkinter.font as font
import pyodbc
from PIL import Image,ImageTk
from Controller import Global_Class
from Controller import Student_course_Register_code
import formatting_constant
import os 



c=formatting_constant.constant


#<-------------------------------------------------- Connection File --------------------------------------------------->


connection=Global_Class.Global




#<--------------------------------------------- Student Course Register Form ------------------------------------------->

def Student_Course_Register(id):

    def self_attendance_call():
        root.destroy()
        import Student_attendance_report
        p=Student_attendance_report.attendance_report(id)


#------------------------------side options------------------------------------------#
    def self_reg_call():
        root.destroy()
        import student_course_registeration
        student_course_registeration.Student_Course_Register(id)
#------------------------------side options------------------------------------------#
    #----------------------------------------------------------------------
    data=[]
    def selectcourse():
       
        connection.cursor.execute("select COURSE_NAME from student_Assigned_course inner join course ON COURSE_ID_F = COURSE_ID where STUDENT_ID_F=?",(id))
        result=connection.cursor.fetchall()
        for row in result:
            data.append(row[0])
            

    def select_offer(event):
        course_offer_listbox.delete(0,tk.END)
        course_name=combox.get()
        connection.cursor.execute("select co.OFFER_COURSE_ID ,c.COURSE_NAME from course_offer co join course c on co.COURSE_ID_F=c.COURSE_ID where c.COURSE_NAME=?",(course_name))
        course_offer_result=connection.cursor.fetchall()
        length=len(course_offer_result)

        for index in range(0,length):
            name=str(course_offer_result[index][0])+"   "+str(course_offer_result[index][1])
            course_offer_listbox.insert(index,name)

            





    # ----------------------------------------------------------------------
    def add_course():
        try:
            if(combox.get() == ""):
                messagebox.showwarning("warning","please Select a course")
            else:

                select_course=int(course_offer_listbox.curselection()[0])

                value=course_offer_listbox.get(select_course)
                new=value.split()
            
                
                connection.cursor.execute("select COURSE_ID from course where COURSE_NAME=?",(new[1]))
                course_id=connection.cursor.fetchall()
                c_id=course_id[0][0]

                connection.cursor.execute("select count(*) as 'number' from student_course_record where COURSE_ID_F=? ",(c_id))
                id_count=connection.cursor.fetchall()
                number=id_count[0][0]

                if(number==15):
                    messagebox.showerror("Message","Id is full")

                else :
                    connection.cursor.execute('insert into student_course_record(COURSE_ID_F,STUDENT_ID_F)values(?,?)',(new[0],id))
                    messagebox.showinfo("Message","Course is Registered")
                    name=str(new[0])+"   "+str(new[1])
                    course_listbox.insert(1,name)
                    
                    connection.cursor.execute("delete from student_Assigned_course  where COURSE_ID_F=?",(c_id))
                    

                    connection.cursor.execute("select STD_PHOTO from student_images where STD_ID=?",(id))
                    result=connection.cursor.fetchall()
                    length=len(result)
                    stduent_images=str(new[0])+" "+str(new[1])

                    for index in range(0,length):
                        path_dataset_images="D:\FYP_project_temp\course/"+stduent_images+"_dataset/"+id+" "+str(index)+".jpg"
                        with open(path_dataset_images,'wb') as f:
                            f.write(result[index][0])




                    connection.conn.commit()


                    
                    root.destroy()

                    import student_course_registeration
                    student_course_registeration.Student_Course_Register(id)
            
        except:
            messagebox.showwarning("warning","please select a course ID in course Offer")







    #----------------------------------------------------------------------
    def drop_course():
      
        index=course_listbox.curselection()
        Student_course_Register_code.course_deleted(course_listbox,index,id,root)
        
        # root.destroy()
       
    


    #----------------------------------------------------------------------


    
    # def self_reg_call():
        # root.destroy()
        # import student_course_registeration
        # student_course_registeration.Student_Course_Register(id)
    #----------------------------------------------------------------------

    root=tk.Tk()
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (c.form_width_course_register, c.form_height, c.form_x, c.form_y))
    root.focus_set()  

    canvas = tk.Canvas(root, height=c.form_height, width=c.form_width,bg="#757575")
    canvas.pack()
   
    Fontlabel = font.Font(family=c.family, size=13, )
    Fontlabel1 = font.Font(family=c.family, font=8, )
    Fontlabel2 = font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )


    


   #main frame
    frame=tk.Frame(root,bg=c.frame_bg)
    frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

    headframe=tk.Frame(frame,bg=c.headframe_bg)
    headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)

    

#left frame
    leftframe=tk.Frame(frame,bg=c.left_Frame_label_bg)
    leftframe.place(relx=0.0,rely=0.02,relwidth=c.register_leftframe_width,relheight=c.leftframe_height)




    def on_click(event=None):
        root.destroy()


#cross symbol
    file_name="D:\FYP_project_temp\images\crossicon.png"
    stdfilee=Image.open(file_name)
    stdshow=ImageTk.PhotoImage(stdfilee)
    imageshow=tk.Label(image=stdshow)
    imageshow.bind('<Button-1>', on_click)
    imageshow.image=stdshow
    imageshow.place(relx=0.98,rely=0.0)
    
    button_Student_report=tk.Button(leftframe,text="Self Registeration",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self_reg_call)
    button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


    button_teacher_report=tk.Button(leftframe,text="Attendance Report",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self_attendance_call)
    button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

    

    mainframelabel=tk.Label(frame,text='Self Registeration Course',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=Fontlabel2
    mainframelabel.place(relx=0.5,rely=0.1)

    
    def menu_back(event=None):
        root.destroy()
        import Student_Menu
        Student_Menu.Student_menu(id) 

    #back 
    # file_name="D:\FYP_project_temp\images\\back.png"
    # stdfilee=Image.open(file_name)
    # stdshow=ImageTk.PhotoImage(stdfilee)
    # imageshow=tk.Label(image=stdshow)
    # imageshow.bind('<Button-1>', menu_back)
    # imageshow.image=stdshow
    # imageshow.place(relx=0.02,rely=0.03)

    back_label=tk.Label(frame,text="\U000021B5 Back",bg=c.leftframe_bg,fg='white')
    back_label.config(font=("Gudea,sans-serif", 13))
    back_label.place(relx=0.02,rely=0.022)
    back_label.bind('<Button-1>', menu_back)



   #logo
    file_name="D:\FYP_project_temp\images\studentlogo.jpeg"
    stdfilee=Image.open(file_name)
    stdshow=ImageTk.PhotoImage(stdfilee)
    imageshow=tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)

    cblable=tk.Label(frame,text="Select course",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    cblable['font']=Fontlabel1
    cblable.place(relx=0.43,rely=0.2)
    combox=ttk.Combobox(frame,values=selectcourse(),width=17)
    combox.place(relx=0.55,rely=0.2,relwidth=c.combox_width,relheight=c.combox_height)
  #  cb=ttk.Combobox(root,values=selectcourse(),width=17)
    combox['value']=data
    combox.bind("<<ComboboxSelected>>",select_offer)
 

    login_button=tk.Button(frame,text="Add   \U000021D2",bg=c.frame_bg,fg='white',borderwidth=3,command=add_course)
    login_button.place(relx=0.61,rely=0.46,relwidth=c.maintain_course_button_width,relheight=c.maintain_course_button_height)


    course_listbox=tk.Listbox(root,)
    course_listbox.pack(side=LEFT, fill=BOTH)
    course_listbox.place(relx=0.73,rely=0.4,relwidth=c.course_listbox_width,relheight=c.course_listbox_height)
    
    course_register_lb=tk.Label(frame,text="Course Register",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    course_register_lb['font']=Fontlabel1
    course_register_lb.place(relx=0.73,rely=0.34)


    course_offer_lb=tk.Label(frame,text="Course Offer",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    course_offer_lb['font']=Fontlabel1
    course_offer_lb.place(relx=0.35,rely=0.34)

    course_offer_listbox=tk.Listbox(root,)
    course_offer_listbox.pack(side=LEFT, fill=BOTH)
    course_offer_listbox.place(relx=0.35,rely=0.4,relwidth=c.course_listbox_width,relheight=c.course_listbox_height)
    


    a=lambda course_listbox=course_listbox: course_listbox.delete(ANCHOR)


    connection.cursor.execute("select COURSE_ID_F from student_course_record where STUDENT_ID_F=?",(id))
    c_id=connection.cursor.fetchall()

    length=len(c_id)
    for index in range(0,length):
        select_id=c_id[index][0]
        
        connection.cursor.execute("select COURSE_ID_F from course_offer where OFFER_COURSE_ID=?",(select_id))
        course_id=connection.cursor.fetchall()

        connection.cursor.execute("select COURSE_NAME from course where COURSE_ID=?",(course_id[0]))
        course_name=connection.cursor.fetchall()
        name=str(select_id) + "   "+str(course_name[0][0])
        course_listbox.insert(index,name)


    


    # l=len(c_id) 
    # for i in range(0,l):
    #     course_listbox.insert(END,c_id[i][0])


    drop_button=tk.Button(frame,text="\U000021D0   drop",bg=c.frame_bg,fg='white',borderwidth=3,command=drop_course)
    drop_button.place(relx=0.61,rely=0.54,relwidth=c.maintain_course_button_width,relheight=c.maintain_course_button_height)






    root.mainloop()



