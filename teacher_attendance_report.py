
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
        self.style=import_file_obj.ttk.Style()
        self.student=[]
        self.c_data=[]
       
        self.root.overrideredirect(True)
        self.root.geometry('%dx%d+%d+%d' % (c.form_width+300, c.form_height, c.form_x, c.form_y))
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

        self.back_label=import_file_obj.tk.Label(self.frame,text="\U000021B5 Login Out",bg=c.leftframe_bg,fg='white')
        self.back_label.config(font=("Gudea,sans-serif", 13))
        self.back_label.place(relx=0.02,rely=0.022)
        self.back_label.bind('<Button-1>',self.menu_back)


        #logo
        self.file_name="D:\FYP_project_temp\images\\admin_logo.jpeg"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.03,rely=0.08)


        self.button_Student_report=import_file_obj.tk.Button(self.leftframe,text="Take Attendance",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.self_take_attendance)
        self.button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


        self.button_teacher_report=import_file_obj.tk.Button(self.leftframe,text="Attendance Report",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.self_attendance_call)
        self.button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

        self.mainframelabel=import_file_obj.tk.Label(self.frame,text='Student attendance report',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.mainframelabel['font']=self.Fontlabel2
        self.mainframelabel.place(relx=0.5,rely=0.1)

        self.course_name_lbl=import_file_obj.tk.Label(self.frame,text="Select Course Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.course_name_lbl['font']=self.Fontlabel1
        self.course_name_lbl.place(relx=0.37,rely=0.2)


        
        self.style.configure( 'TCombobox', font=('Purisa', 10, 'bold'), background ='#EFFFE1',fieldbackground='red')
        self.course_cb=import_file_obj.ttk.Combobox(self.frame,values=self.select_course())
        self.course_cb['value']=self.c_data
        self.course_cb.place(relx=0.37,rely=0.24,relwidth=c.combox_width-0.14,relheight=c.combox_height)
        self.course_cb.bind("<<ComboboxSelected>>",self.show_id)
        self.course_cb.master.option_add( '*TCombobox*Listbox.background', '#EFFFE1')


        self.course_name_id=import_file_obj.tk.Label(self.frame,text="Select Course id",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.course_name_id['font']=self.Fontlabel1
        self.course_name_id.place(relx=0.57,rely=0.2)


        self.course_cb_id=import_file_obj.ttk.Combobox(self.frame)
        self.course_cb_id.place(relx=0.57,rely=0.24,relwidth=c.combox_width-0.17,relheight=c.combox_height)
        self.course_cb_id.bind("<<ComboboxSelected>>",self.select_attendance_record)
        self.course_cb_id.master.option_add( '*TCombobox*Listbox.background', '#EFFFE1')

        self.date_lb=import_file_obj.tk.Label(self.frame,text="Select Date",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.date_lb['font']=self.Fontlabel1
        self.date_lb.place(relx=0.74,rely=0.2)

        self.date_cb=import_file_obj.ttk.Combobox(self.frame)
        self.date_cb.place(relx=0.74,rely=0.24,relwidth=c.combox_width-0.23,relheight=c.combox_height)
        # self.date_cb.bind("<<ComboboxSelected>>",self.date_report)
        self.date_cb.master.option_add( '*TCombobox*Listbox.background', '#F4F4F4')
        self.date_cb.bind("<<ComboboxSelected>>",self.call_year)

        self.month_cb=import_file_obj.ttk.Combobox(self.frame)
        self.month_cb.place(relx=0.81,rely=0.24,relwidth=c.combox_width-0.2,relheight=c.combox_height)
        # self.date_cb.bind("<<ComboboxSelected>>",self.date_report)
        self.month_cb.master.option_add( '*TCombobox*Listbox.background', '#F4F4F4')
        self.month_cb.bind("<<ComboboxSelected>>",self.call_year)


        self.year_cb=import_file_obj.ttk.Combobox(self.frame)
        self.year_cb.place(relx=0.91,rely=0.24,relwidth=c.combox_width-0.23,relheight=c.combox_height)
        # self.date_cb.bind("<<ComboboxSelected>>",self.date_report)
        self.year_cb.master.option_add( '*TCombobox*Listbox.background', '#F4F4F4')
        self.year_cb.bind("<<ComboboxSelected>>",self.call_year)

        
        













        

        self.tv=import_file_obj.ttk.Treeview(self.frame,columns=(1,2,3,4),show="headings",height=15,xscroll=0.3)
        self.tv.column(1,width=100)
        self.tv.column(2,width=100)
        self.tv.column(3,width=100)
        self.tv.column(3,width=100)
       

        self.tv.heading(1,text="student ID")
        self.tv.heading(2,text="Student Name")
        self.tv.heading(3,text="total of present")
        self.tv.heading(4,text="total of Absent")

     
     
        self.tv.place(relx=0.4,rely=0.35)



        
        self.tv1=import_file_obj.ttk.Treeview(self.frame,columns=(1,2,3),show="headings",height=15,xscroll=0.3)
        self.tv1.column(1,width=100)
        self.tv1.column(2,width=100)
        self.tv1.column(3,width=100)
    
       

        self.tv1.heading(1,text="student ID")
        self.tv1.heading(2,text="Student Name")
        self.tv1.heading(3,text="Status")
      

     
     
        self.tv1.place(relx=0.5,rely=0.35)

        self.hide()


        
        self.root.mainloop()
    
    def student_record(self):
        self.root.destroy()
        import teacher_attendance_report
        p=teacher_attendance_report.attendance_report(id)

    def take_attendance(self):
        self.root.destroy()
        import take_Attendance
        p=take_Attendance.Take_Attendance(id)    
    


    def hide(self):

        self.tv.place_forget()
        self.tv1.place_forget()

    def call_year(self,event=None):
        self.date_report_year()    
    def call_month(self,event=None):
        self.date_report_year()   
    def call_Days(self,event=None):
        self.date_report_year()       
            

        
    def date_report_year(self):
        if(self.date_cb.get() != "Date:" and self.year_cb.get() != "Year:" and self.month_cb.get() != "Month:"):
            self.tv1.place(relx=0.5,rely=0.35)
            self.tv.place_forget()

            if(len(self.student) != 0):

                for row in self.tv1.get_children():
                    self.tv1.delete(row)



            
            self.student=[]

            date=self.month_cb.get()+" "+self.date_cb.get()+", "+self.year_cb.get()

            Conection.cursor.execute("Select * from student_attendance where DATE=?",(date))
            count=Conection.cursor.fetchall()

            # January 02, 2020

            if(len(count) == 0):
                import_file_obj.messagebox.showinfo("info","Attendance is not taken")
            else:

                Conection.cursor.execute("Select STUDENT_ID_F from student_attendance where COURSE_ID_F=?",(self.course_cb_id.get()))
                student_id=Conection.cursor.fetchall()


                
                for j in range(0,len(student_id)):
                    self.student.append(student_id[j][0])
                self.student=list(dict.fromkeys(self.student))    

                for i in range(0,len(self.student)):


                    Conection.cursor.execute("Select STD_NAME from student_registeration_record where STD_ID=?",(self.student[i]))
                    student_name=Conection.cursor.fetchall()

                    Conection.cursor.execute("Select STATUS from student_attendance where COURSE_ID_F=? and STUDENT_ID_F=? and DATE=?",(self.course_cb_id.get(),self.student[i],date))
                    status=Conection.cursor.fetchall()
                    
                    if len(status) != 0:

                        l=[( self.student[i],student_name[0][0],status[0][0])]
                        for j in l:
                            self.tv1.insert('','end',values=j)
        









    
    def select_attendance_record(self,event=None):
        if(self.course_cb_id.get() != "Select course id......"):

            if(len(self.student) != 0):

                for row in self.tv.get_children():
                    self.tv.delete(row)

            
            self.student=[]
            self.tv.place(relx=0.4,rely=0.35)
            self.tv1.place_forget()
            

            

            Conection.cursor.execute("Select STUDENT_ID_F from student_attendance where COURSE_ID_F=?",(self.course_cb_id.get()))
            student_id=Conection.cursor.fetchall()


            for j in range(0,len(student_id)):
                self.student.append(student_id[j][0])
            self.student=list(dict.fromkeys(self.student))    




            


            

            for i in range(0,len(self.student)):


                Conection.cursor.execute("Select STD_NAME from student_registeration_record where STD_ID=?",(self.student[i]))
                student_name=Conection.cursor.fetchall()


                Conection.cursor.execute("Select count(*) from student_attendance where COURSE_ID_F=? and STATUS='PRESENT' and STUDENT_ID_F=?",(self.course_cb_id.get(),self.student[i]))
                Present=Conection.cursor.fetchall()

                Conection.cursor.execute("Select count(*) from student_attendance where COURSE_ID_F=? and STATUS='ABSENT' and STUDENT_ID_F=? ",(self.course_cb_id.get(),self.student[i]))
                Absent=Conection.cursor.fetchall()


                l=[(self.student[i],student_name[0][0],Present[0][0],Absent[0][0])]

                for index in l:
                    self.tv.insert('','end',values=index)
            show_date=[]        

            Conection.cursor.execute("select DATE from student_attendance where COURSE_ID_F=?",(self.course_cb_id.get()))
            date_result=Conection.cursor.fetchall()
            show_date.append('select date....') 

            for i in range(0,len(date_result)):
                show_date.append(date_result[i][0])

            show_date=list(dict.fromkeys(show_date))  
            

            self.date=["Day:","01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
            self.month=["Month:","January","February","March","April","May","June","july","August","September","October","November","December"]
            self.year=["Year:",2016,2017,2018,2019,2020,2021,2022,2023,2024]
            self.date_cb['value']=self.date
            self.date_cb.current(0) 
            self.month_cb['value']=self.month
            self.month_cb.current(0)

            self.year_cb['value']=self.year
            self.year_cb.current(0)


        else:
            import_file_obj.messagebox.showwarning("warning","please Select a Course Id")




    def select_course(self):

        self.c_data=[]

        Conection.cursor.execute('select COURSE_ID_F from faculty_course_assigned where FACULTY_ID=?',(self.id))
        course_offer_id=Conection.cursor.fetchall()

        for i in range(0,len(course_offer_id)):
            Conection.cursor.execute('select COURSE_ID_F from course_offer where OFFER_COURSE_ID=?',(course_offer_id[i][0]))
            course_id=Conection.cursor.fetchall()

            Conection.cursor.execute('select COURSE_NAME from course where COURSE_ID=?',(course_id[0][0]))
            course_name=Conection.cursor.fetchall()

            self.c_data.append(course_name[0][0])

        self.c_data=list(dict.fromkeys(self.c_data))    



    def menu_back(self,event=None):
        self.root.destroy()
        import Teacher_menu
        Teacher_menu.faculty_menu(self.id)
          
    def show_id(self,event):

        show_data=[]  
        selectt_course=self.course_cb.get()


        Conection.cursor.execute('select COURSE_ID from course where COURSE_NAME=?',(selectt_course))
        RESULT_COURSE=Conection.cursor.fetchall()

        Conection.cursor.execute('select OFFER_COURSE_ID from course_offer where COURSE_ID_F=?',(RESULT_COURSE[0][0]))
        Result_Course_id=Conection.cursor.fetchall()

        length=len(Result_Course_id)
        show_data.append('Select course id......')

        for index in range(0,length):
            Conection.cursor.execute('select * from faculty_course_assigned where COURSE_ID_F=?',(Result_Course_id[index][0]))
            no_of_course=Conection.cursor.fetchall()
            if(len(no_of_course) != 0):
                show_data.append(Result_Course_id[index][0])

        self.course_cb_id['values']=show_data

        self.course_cb_id.current(0)    

    def on_click(self,event=None):
        self.root.destroy()

    def self_attendance_call(self):
        self.root.destroy()
        import take_Attendance
        take_Attendance.Take_Attendance(self.id)   

    def self_take_attendance(self):
        self.root.destroy() 
       
        import take_Attendance
        take_Attendance.Take_Attendance(self.id) 
         



