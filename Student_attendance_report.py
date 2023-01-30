#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 


c=import_file_obj.formatting_constant.constant

#<-------------------------------------------------------------Connection File ---------------------------------------->

Conection=import_file_obj.Global_Class.Global


#<-----------------------------------------------------------------------------------------


class attendance_report():
    def __init__(self,id):
        self.id=id
        self.root=import_file_obj.tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
        self.root.focus_set()  

        self.canvas = import_file_obj.tk.Canvas(self.root, height=c.form_height, width=c.form_width,bg="#757575")
        self.canvas.pack()
    
        self.Fontlabel = import_file_obj.font.Font(family=c.family, size=13, )
        self.Fontlabel1 = import_file_obj.font.Font(family=c.family, font=8, )
        self.Fontlabel2 = import_file_obj.font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )


        


    #main frame
        self.frame=import_file_obj.tk.Frame(self.root,bg=c.frame_bg)
        self.frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

        self.headframe=import_file_obj.tk.Frame(self.frame,bg=c.headframe_bg)
        self.headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)

        

    #left frame
        self.leftframe=import_file_obj.tk.Frame(self.frame,bg=c.left_Frame_label_bg)
        self.leftframe.place(relx=0.0,rely=0.02,relwidth=c.register_leftframe_width,relheight=c.leftframe_height)

        self.file_name="D:\FYP_project_temp\images\\crossicon.png"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.on_click)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.98,rely=0.0)


        # self.file_name="D:\FYP_project_temp\images\\back.png"
        # self.stdfilee=import_file_obj.Image.open(self.file_name)
        # self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        # self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        # self.imageshow.bind('<Button-1>', self.menu_back)
        # self.imageshow.image=self.stdshow
        # self.imageshow.place(relx=0.02,rely=0.03)

        back_label=import_file_obj.tk.Label(self.frame,text="\U000021B5 Back",bg=c.leftframe_bg,fg='white')
        back_label.config(font=("Gudea,sans-serif", 13))
        back_label.place(relx=0.02,rely=0.022)
        back_label.bind('<Button-1>',self.menu_back)


        #logo
        self.file_name="D:\FYP_project_temp\images\\admin_logo.jpeg"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.03,rely=0.08)


        self.button_Student_report=import_file_obj.tk.Button(self.leftframe,text="Self Registeration",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.self_reg_call)
        self.button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


        self.button_teacher_report=import_file_obj.tk.Button(self.leftframe,text="Attendance Report",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.self_attendance_call)
        self.button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

        self.mainframelabel=import_file_obj.tk.Label(self.frame,text='Student attendance report',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.mainframelabel['font']=self.Fontlabel2
        self.mainframelabel.place(relx=0.5,rely=0.2)











        Conection.cursor.commit()





        Conection.cursor.execute('Select count(*) from student_course_record where STUDENT_ID_F=?',(self.id))
        count=Conection.cursor.fetchall()

        self.tv=import_file_obj.ttk.Treeview(self.frame,columns=(1,2,3,4),show="headings",height=count[0][0],xscroll=0.3)
        self.tv.column(1,width=100)
        self.tv.column(2,width=150)
        self.tv.column(3,width=50)
        self.tv.column(4,width=50)

        self.tv.heading(1,text="Course ID")
        self.tv.heading(2,text="Course Name")
        self.tv.heading(3,text="total")
        self.tv.heading(4,text="present")

        self.tv.tag_configure(1, background="red")
     
        self.tv.place(relx=0.4,rely=0.3)


        
        Conection.cursor.execute("select course_id_f from student_course_record where STUDENT_ID_F=?",(self.id))
        result=Conection.cursor.fetchall()
        length=len(result)
        for i in range(0,length):
            Conection.cursor.execute("select COURSE_NAME from course c join course_offer co on c.COURSE_ID=co.COURSE_ID_F where co.OFFER_COURSE_ID=?",(result[i][0]))
            course_name=Conection.cursor.fetchall()

            Conection.cursor.execute("select count(COURSE_ID_F) from student_attendance where COURSE_ID_F=? and STUDENT_ID_F=?",(result[i][0],self.id))
            Total=Conection.cursor.fetchall()


            Conection.cursor.execute("Select * from student_attendance where COURSE_ID_F=? and STUDENT_ID_F=? and STATUS='PRESENT'",(result[i][0],self.id))
            present=Conection.cursor.fetchall()

            count_present=len(present)
            

            l=[(result[i][0],course_name[0][0],Total[0][0],count_present)]

            for index in l:

                self.tv.insert('','end',values=index)
            # self.tv.insert('','end',values=result[i][0])
            # self.tv.insert('2',tk.END,values=course_name[0][0])




        


        self.root.mainloop()

    def menu_back(self,event=None):
        self.root.destroy()
        import Student_Menu
        Student_Menu.Student_menu(self.id)

    def on_click(self,event=None):
        self.root.destroy()

    def self_attendance_call(self):
        self.root.destroy()
        import Student_attendance_report
        p=Student_attendance_report.attendance_report(self.id)

    def self_reg_call(self):
        self.root.destroy()
        import student_course_registeration
        student_course_registeration.Student_Course_Register(self.id)    

           

