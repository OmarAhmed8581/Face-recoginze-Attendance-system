#<--------------------------------------------------------- Import file ---------------------------------------------->

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
from Controller import Global_Class
import formatting_constant 







c=formatting_constant.constant

#<-------------------------------------------------------------Connection File ---------------------------------------->

Conection=Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->


class teacher_course():

    def __init__(self,event):
        
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
        self.root.focus_set()  

        self.canvas = tk.Canvas(self.root, height=c.form_height, width=c.form_width,bg="#757575")
        self.canvas.pack()
    
        self.Fontlabel = font.Font(family=c.family, size=13, )
        self.Fontlabel1 = font.Font(family=c.family, font=8, )
        self.Fontlabel2 = font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )


        


    #main frame
        self.frame=tk.Frame(self.root,bg=c.frame_bg)
        self.frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

        self.headframe=tk.Frame(self.frame,bg=c.headframe_bg)
        self.headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)

        

    #left frame
        self.leftframe=tk.Frame(self.frame,bg=c.left_Frame_label_bg)
        self.leftframe.place(relx=0.0,rely=0.02,relwidth=c.register_leftframe_width,relheight=c.leftframe_height)


    #cross symbol
        self.file_name="D:\FYP_project_temp\images\\crossicon.png"
        self.stdfilee=Image.open(self.file_name)
        self.stdshow=ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.on_click)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.98,rely=0.0)

    



        # headleftframe=tk.Frame(leftframe,bg='white')
        # headleftframe.place(relx=0.0,rely=0.0,relwidth=c.headleftframe_width,relheight=c.headleftframe_height)
      
            
        #back 
        self.file_name="D:\FYP_project_temp\images\\back.png"
        self.stdfilee=Image.open(self.file_name)
        self.stdshow=ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.menu_back)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.02,rely=0.03)


        #logo
        self.file_name="D:\FYP_project_temp\images\\admin_logo.jpeg"
        self.stdfilee=Image.open(self.file_name)
        self.stdshow=ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=tk.Label(image=self.stdshow)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.03,rely=0.08)   
    #----------------------------------------------------------------------------------------------------

        self.button_Student_report=tk.Button(self.leftframe,text="View Student",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.call)
        self.button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


        self.button_teacher_report=tk.Button(self.leftframe,text="Faculty Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.faculty_call)
        self.button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

        self.button_maintain_course=tk.Button(self.leftframe,text="Maintain Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.Course_call)
        self.button_maintain_course.place(relx=0.1,rely=0.7,relwidth=c.user_button_width,relheight=c.user_button_height)


        
        self.mainframelabel=tk.Label(self.frame,text='Assign course to faculty',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.mainframelabel['font']=self.Fontlabel2
        self.mainframelabel.place(relx=0.5,rely=0.1)

        self.add_course=tk.Button(self.frame,text='Assign Course',bg=c.button_bg,fg=c.button_fg,command=self.add)
        self.add_course.place(relx=0.4,rely=0.2,relwidth=0.17,relheight=c.maintain_course_button_height)

        self.delete_course=tk.Button(self.frame,text='UnAssign Course',bg=c.button_bg,fg=c.button_fg,command=self.delete)
        self.delete_course.place(relx=0.59,rely=0.2,relwidth=0.17,relheight=c.maintain_course_button_height)


        self.view_course=tk.Button(self.frame,text='View ',bg=c.button_bg,fg=c.button_fg,command=self.view)
        self.view_course.place(relx=0.8,rely=0.2,relwidth=0.17,relheight=c.maintain_course_button_height)

    
    #--------------------------------------------Add---------------------------------------------------

        self.assign_course_frame = tk.LabelFrame(self.frame, text="Assign Course", padx=8, pady=8,bg=c.frame_bg,fg=c.course_frame_fg)
        self.assign_course_frame.pack(padx=10, pady=15)
        self.assign_course_frame.place(relx=0.5,rely=0.4)

        self.course_name_lbl=tk.Label(self.assign_course_frame,text="Select Course Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.course_name_lbl['font']=self.Fontlabel1
        self.course_name_lbl.grid(row=0, column=0, sticky=tk.E)
        self.course_cb=ttk.Combobox(self.assign_course_frame,values=self.select_course())
        self.course_cb['value']=self.c_data
        self.course_cb.grid(row=0, column=1, ipady=1)
        self.course_cb.bind("<<ComboboxSelected>>",self.show_id)

        self.course_id_lbl=tk.Label(self.assign_course_frame,text="Select Course ID",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.course_id_lbl['font']=self.Fontlabel1
        self.course_id_lbl.grid(row=1, column=0, sticky=tk.E)
        self.course_cb_id=ttk.Combobox(self.assign_course_frame)
        self.course_cb_id.grid(row=1, column=1, ipady=1)
        
        self.faculty_name_lbl=tk.Label(self.assign_course_frame,text="Select Faculty Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.faculty_name_lbl['font']=self.Fontlabel1
        self.faculty_name_lbl.grid(row=2, column=0, sticky=tk.E)
        self.faculty_cb=ttk.Combobox(self.assign_course_frame,values=self.teacher_data())
        self.faculty_cb['value']=self.f_data
        self.faculty_cb.grid(row=2, column=1, ipady=1)

        
        self.assign_btn=tk.Button(self.assign_course_frame,text="ASSIGN",bg=c.frame_bg,fg='White',borderwidth=3,command=self.register_course)
        self.assign_btn.grid(row=3,column=1,ipadx=c.maintain_course_button_ipadx)


    #--------------------------------------------Unassign---------------------------------------------------

        self.f_id=[]
        Conection.cursor.execute('select FACULTY_ID from faculty_course_assigned')
        self.result=Conection.cursor.fetchall()
        for row in range(0,len(self.result)):
            self.f_id.append(self.result[row][0])
            
        self.f_id=list(dict.fromkeys(self.f_id))
        
        self.f_name=[]
        for i in range(0,len(self.f_id)):
            Conection.cursor.execute('select FACULTY_NAME from faculty_registeration_record where FACULTY_ID=?',(self.f_id[i]))
            self.result_name=Conection.cursor.fetchall()
            self.f_record=str(self.f_id[i])+"  " + self.result_name[0][0]
            self.f_name.append(self.f_record)
            
        # f_name=list(dict.fromkeys(f_name))


        
        self.Unassign_course_frame = tk.LabelFrame(self.frame, text="Unassign Course", padx=8, pady=8,bg=c.frame_bg,fg=c.course_frame_fg)
        self.Unassign_course_frame.pack(padx=10, pady=15)
        self.Unassign_course_frame.place(relx=0.5,rely=0.4)

        # course_name_lbl=tk.Label(Unassign_course_frame,text="Select Course Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        # course_name_lbl['font']=Fontlabel1
        # course_name_lbl.grid(row=0, column=0, sticky=tk.E)
        # course_cb=ttk.Combobox(Unassign_course_frame,values=select_course())
        # course_cb['value']=c_data
        # course_cb.grid(row=0, column=1, ipady=1)
        # course_cb.bind("<<ComboboxSelected>>",show_id)

        self.faculty_name_lbl1=tk.Label(self.Unassign_course_frame,text="Select Faculty Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.faculty_name_lbl1['font']=self.Fontlabel1
        self.faculty_name_lbl1.grid(row=0, column=0, sticky=tk.E)
        self.faculty_cb1=ttk.Combobox(self.Unassign_course_frame)
        self.faculty_cb1['value']=self.f_name
        self.faculty_cb1.bind("<<ComboboxSelected>>",self.call_id)
        self.faculty_cb1.grid(row=0, column=1, ipady=1)




        
        # Conection.cursor.execute('select COURSE_ID_F from faculty_course_assigned where FACULTY_ID=?',(faculty_cb.get()))
        # course_id=Conection.cursor.fetchall()

        self.course_id_lbl1=tk.Label(self.Unassign_course_frame,text="Select Course ID",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.course_id_lbl1['font']=self.Fontlabel1
        self.course_id_lbl1.grid(row=1, column=0,sticky=tk.E)
        self.course_cb_id1=ttk.Combobox(self.Unassign_course_frame,)
        self.course_cb_id1.grid(row=1, column=1, ipady=1)
        


        
        self.Unassign_btn=tk.Button(self.Unassign_course_frame,text="UNASSIGN",bg=c.frame_bg,fg='White',borderwidth=3,command=self.unassign_course)
        self.Unassign_btn.grid(row=3,column=1,ipadx=c.maintain_course_button_ipadx)


    #---------------------------------------------View------------------------------------------------------------------

    
        self.tv=ttk.Treeview(self.frame,columns=(1,2,3),show="headings",xscroll=0.2)
        self.tv.column(1,width=75)
        self.tv.column(2,width=90)
        self.tv.column(2,width=90)


        self.tv.heading(1,text="Course Id")
        self.tv.heading(2,text="Course Name")
        self.tv.heading(3,text="Teacher Name")


        teacher_id=[]
        Conection.cursor.execute("select FACULTY_ID from faculty_course_assigned")
        result=Conection.cursor.fetchall()

        for i in range(0,len(result)):
            teacher_id.append(result[i][0])
        teacher_id=list(dict.fromkeys(teacher_id))

        for j in range(0,len(teacher_id)):
            Conection.cursor.execute("Select FACULTY_NAME from faculty_registeration_record where FACULTY_ID=?",(teacher_id[j]))
            teacher_name=Conection.cursor.fetchall()

            Conection.cursor.execute("Select COURSE_ID_F from faculty_course_assigned where FACULTY_ID=?",(teacher_id[j]))
            course_offer_id=Conection.cursor.fetchall()

            for k in range(0,len(course_offer_id)):
                Conection.cursor.execute("Select COURSE_ID_F from course_offer where OFFER_COURSE_ID=?",(course_offer_id[k][0]))
                course_id=Conection.cursor.fetchall()



                if(len(course_id)!=0):
                    Conection.cursor.execute("Select COURSE_NAME from course where COURSE_ID=?",(course_id[0][0]))
                    course_name=Conection.cursor.fetchall()

                    if(len(course_name)!=0):

                        l=[(course_offer_id[k][0],course_name[0][0],teacher_name[0][0])]

                        for index in l:

                            self.tv.insert('','end',values=index)





        self.hide()

        if event=="Assigned":
            self.add()
        elif event== "Unassigned":
            self.delete()    



        self.root.mainloop()
    
    def on_click(self,event=None):
        self.root.destroy()
    def menu_back(self,event=None):
        self.root.destroy()
        import Admin_Menu
        Admin_Menu.admin_menu()  
    
    def call_id(self,event=None):
        
        self.course_id=[]
        self.get_f_id=self.faculty_cb1.get()
        self.get=self.get_f_id.split()

        Conection.cursor.execute('select COURSE_ID_F from faculty_course_assigned where FACULTY_ID=?',self.get[0])
        self.result=Conection.cursor.fetchall()
        for row in range(0,len(self.result)):
            self.course_id.append(self.result[row][0])
            
        self.course_id=list(dict.fromkeys(self.course_id))

        self.course_cb_id1['value']=self.course_id
        self.course_cb_id1.current(0)
    

    
#------------------------------side options------------------------------------------#
    def call(self):
        self.root.destroy()
        import student_view
        student_view.student_view()

    def Course_call(self):
        self.root.destroy()
        import course_maintain
        p= course_maintain.Course_maintain(None)

    def faculty_call(self):
        self.root.destroy()
        import assigned_course_teacher
        assigned_course_teacher.teacher_course(None)
#------------------------------side options------------------------------------------#


    def hide(self):
        self.assign_course_frame.place_forget() 
        self.Unassign_course_frame.place_forget() 
        
        # self.view_course_frame.place_forget()  
        self.tv.place_forget()
    def add(self):
        self.assign_course_frame.place(relx=0.5,rely=0.4)
        self.Unassign_course_frame.place_forget()
        # update_course_frame.place_forget()
        # view_course_frame.place_forget()
        self.tv.place_forget()

    def delete(self):
        self.Unassign_course_frame.place(relx=0.5,rely=0.4)
        self.assign_course_frame.place_forget()
        # update_course_frame.place_forget()   
        # view_course_frame.place_forget()
        
        self.tv.place_forget() 
        

    def view(self):
        self.assign_course_frame.place_forget()
        self.Unassign_course_frame.place_forget()
        # self.update_course_frame.place_forget()
        # self.view_course_frame.place(relx=0.5,rely=0.4)
        self.tv.place(relx=0.38,rely=0.4)

   
    def teacher_data(self):
        self.f_data=[]
        Conection.cursor.execute('select FACULTY_NAME from faculty_registeration_record')
        result=Conection.cursor.fetchall()
        for row in result:
            self.f_data.append(row[0])
         
    def show_id(self,event):
        self.show_data=[]   
        selectt_course=self.course_cb.get()
        


        Conection.cursor.execute('select COURSE_ID from course where COURSE_NAME=?',(selectt_course))
        RESULT_COURSE=Conection.cursor.fetchall()

        Conection.cursor.execute('select OFFER_COURSE_ID from course_offer where COURSE_ID_F=?',(RESULT_COURSE[0][0]))
        Result_Course_id=Conection.cursor.fetchall()

        length=len(Result_Course_id)

        for index in range(0,length):
            Conection.cursor.execute('select * from faculty_course_assigned where COURSE_ID_F=?',(Result_Course_id[index][0]))
            no_of_course=Conection.cursor.fetchall()
            if(len(no_of_course) == 0):
                self.show_data.append(Result_Course_id[index][0])

        self.course_cb_id['values']=self.show_data
        self.course_cb_id.current(0)
      
        
   
    def select_course(self):
        self.c_data=[]
        count=0

        Conection.cursor.execute('select COURSE_NAME from course')
        result=Conection.cursor.fetchall()

        for row in range(0,len(result)):
            count=0
            Conection.cursor.execute('select COURSE_ID from course where COURSE_NAME=?',(result[row][0]))
            course_id=Conection.cursor.fetchall()

            Conection.cursor.execute('Select OFFER_COURSE_ID from course_offer where COURSE_ID_F=?',(course_id[0][0]))
            offer_course_id=Conection.cursor.fetchall()
             

            for j in range(0,len(offer_course_id)): 
                Conection.cursor.execute('Select * from faculty_course_assigned where COURSE_ID_F=?',(offer_course_id[j][0]))
                id=Conection.cursor.fetchall()

                if len(id) != 0:
                    count +=1

            if count != len(offer_course_id):
                
                self.c_data.append(result[row][0])



    def register_course(self):
        selectt_course=self.course_cb_id.get()
        select_faculty=self.faculty_cb.get()

        Conection.cursor.execute("select FACULTY_ID from faculty_registeration_record where FACULTY_NAME=?",select_faculty)
        faculty_id=Conection.cursor.fetchall()
        f_id=faculty_id[0][0]

        Conection.cursor.execute('insert into faculty_course_assigned(FACULTY_ID,COURSE_ID_F)values(?,?)',(f_id,selectt_course))
        messagebox.showinfo('Assigned','course is assigned!')
        Conection.conn.commit()
        self.root.destroy()
        teacher_course("Assigned")


        








#wait


#--------------------------------------unassign-----------------------------------------

    f_id=[]
    Conection.cursor.execute('select FACULTY_ID from faculty_course_assigned')
    result=Conection.cursor.fetchall()
    for row in range(0,len(result)):
        f_id.append(result[row][0])
        
    f_id=list(dict.fromkeys(f_id)) 

    def unassign_course(self):
        self.get_id=self.faculty_cb1.get()
        self.faculty_id=self.get_id.split()

        # get_name=course_cb_id1.get()
        # faculty_nama
        Conection.cursor.execute('delete from faculty_course_assigned where FACULTY_ID=? AND COURSE_ID_F=?',(self.faculty_id[0],self.course_cb_id1.get()))
        Conection.conn.commit()
        messagebox.showinfo('Unassigned Course','Course is Unassigned successfully!')
        self.root.destroy()
        teacher_course("Unassigned")

    # Conection.cursor.execute('select FACULTY_NAME from faculty_registeration_record where FACULTY_ID=?',(f_id))
    # faculty_name=Conection.cursor.fetchall()

    






















teacher_course(None)