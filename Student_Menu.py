
#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file





#<------------------------------------------- create an object of formatting Constant--------> 

c=import_file_obj.formatting_constant.constant



#<------------------------------------------- create an object of Connection File --------------------------------------------------->


Conection=import_file_obj.Global_Class.Global


#<---------------------------------------------------- Student Menu ----------------------------------------------------->

def Student_menu(id):


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




 
    


    

    root=import_file_obj.tk.Tk()
    root.title("Admin form")
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
    root.focus_set()  

    canvas = import_file_obj.tk.Canvas(root, height=c.form_height, width=c.form_width,bg="#757575")
    canvas.pack()
   
    Fontlabel = import_file_obj.font.Font(family=c.family, size=13, )
    Fontlabel1 = import_file_obj.font.Font(family=c.family, font=8, )
    Fontlabel2 = import_file_obj.font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )


    Conection.cursor.execute("select STD_ID , STD_NAME from  student_registeration_record where STD_ID=?",(id))
    result=Conection.cursor.fetchall()
    s_id=result[0][0]
    name=result[0][1]
  
  

   #main frame
    frame=import_file_obj.tk.Frame(root,bg=c.frame_bg)
    frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

    headframe=import_file_obj.tk.Frame(frame,bg=c.headframe_bg)
    headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)

    

#left frame
    leftframe=import_file_obj.tk.Frame(frame,bg=c.left_Frame_label_bg)
    leftframe.place(relx=0.0,rely=0.02,relwidth=c.leftframe_width,relheight=c.leftframe_height)




    def on_click(event=None):
        root.destroy()


#cross symbol
    file_name="D:\FYP_project_temp\images\\crossicon.png"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.bind('<Button-1>', on_click)
    imageshow.image=stdshow
    imageshow.place(relx=0.98,rely=0.0)



    def login_back(event=None):
        root.destroy()
        import login
       

    #back 
    # file_name="D:\FYP_project_temp\images\\back.png"
    # stdfilee=import_file_obj.Image.open(file_name)
    # stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    # imageshow=import_file_obj.tk.Label(image=stdshow)                                                                                                           
    # imageshow.bind('<Button-1>', login_back)
    # imageshow.image=stdshow
    # imageshow.place(relx=0.02,rely=0.03)

    back_label=import_file_obj.tk.Label(frame,text="\U000021B5 Login Out",bg=c.leftframe_bg,fg='white')
    back_label.config(font=("Gudea,sans-serif", 13))
    back_label.place(relx=0.02,rely=0.022)
    back_label.bind('<Button-1>',login_back)

    

 



    # headleftframe=tk.Frame(leftframe,bg='white')
    # headleftframe.place(relx=0.0,rely=0.0,relwidth=c.headleftframe_width,relheight=c.headleftframe_height)


    leftframelabel1=import_file_obj.tk.Label(leftframe,text="Welcome to the",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel1['font']=Fontlabel
    leftframelabel1.place(relx=0.3,rely=0.4)

    leftframelabel2=import_file_obj.tk.Label(leftframe,text="Student Attendance System",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel2['font']=Fontlabel
    leftframelabel2.place(relx=0.3,rely=0.5)

    leftframelabel3=import_file_obj.tk.Label(leftframe,text="Student Panel",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel3['font']=Fontlabel
    leftframelabel3.place(relx=0.3,rely=0.6)

    mainframelabel=import_file_obj.tk.Label(frame,text='Student Panel',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=Fontlabel2
    mainframelabel.place(relx=0.6,rely=0.1)


    #logo
    file_name="D:\FYP_project_temp\images\\studentlogo.jpeg"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)

    
    # label_id=tk.Label(frame,text=s_id,font='Cambria',)
    # label_id.place(relx=0.6,rely=0.2)

    Student_id_lbl=import_file_obj.tk.Label(frame,text="Student ID:",bg=c.frame_bg,fg=c.left_Frame_label_fg)
    Student_id_lbl['font']=Fontlabel
    Student_id_lbl.place(relx=0.55,rely=0.2)

    Student_id_text=import_file_obj.tk.Label(frame,text=s_id,bg=c.frame_bg,fg=c.left_Frame_label_fg)
    Student_id_text['font']=Fontlabel
    Student_id_text.place(relx=0.74,rely=0.2)

    Student_name_lbl=import_file_obj.tk.Label(frame,text="Student Name:",bg=c.frame_bg,fg=c.left_Frame_label_fg)
    Student_name_lbl['font']=Fontlabel
    Student_name_lbl.place(relx=0.55,rely=0.25)

    Student_name_text=import_file_obj.tk.Label(frame,text=name,bg=c.frame_bg,fg=c.left_Frame_label_fg)
    Student_name_text['font']=Fontlabel
    Student_name_text.place(relx=0.74,rely=0.25)

    # label_Name=tk.Label(frame,text=name,font='Cambria',)
    # label_Name.place(relx=0.9,rely=0.48)


    self_register_btn=import_file_obj.tk.Button(frame,text="Self Registeration",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self_reg_call)
    self_register_btn.place(relx=0.55,rely=0.39,relwidth=c.user_menu_button_width,relheight=c.user_button_height)


    attendance_report_btn=import_file_obj.tk.Button(frame,text="Attendance Report",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self_attendance_call)
    attendance_report_btn.place(relx=0.55,rely=0.54,relwidth=c.user_menu_button_width,relheight=c.user_button_height)
    




    root.mainloop()


  