
#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 


c=import_file_obj.formatting_constant.constant


#<-------------------------------------------------------------Connection File ---------------------------------------->

Conection=import_file_obj.Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->


def admin_menu():


    def student_view_call():
        root.destroy()
        import student_view
        student_view.student_view()

    def maintain_course_call():
        root.destroy()
        import course_maintain
        p=course_maintain.Course_maintain(None)


    def faculty_call():
        root.destroy()
        import assigned_course_teacher
        assigned_course_teacher.teacher_course(None) 

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


    def menu_back(event=None):
        root.destroy()
        import login
        

    #back 
    file_name="D:\FYP_project_temp\images\\back.png"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.bind('<Button-1>', menu_back)
    imageshow.image=stdshow
    imageshow.place(relx=0.02,rely=0.03)

 



    # headleftframe=tk.Frame(leftframe,bg='white')
    # headleftframe.place(relx=0.0,rely=0.0,relwidth=c.headleftframe_width,relheight=c.headleftframe_height)


    leftframelabel1=import_file_obj.tk.Label(leftframe,text="Welcome to the",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel1['font']=Fontlabel
    leftframelabel1.place(relx=0.3,rely=0.4)

    leftframelabel2=import_file_obj.tk.Label(leftframe,text="Student Attendance System",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel2['font']=Fontlabel
    leftframelabel2.place(relx=0.3,rely=0.5)

    leftframelabel3=import_file_obj.tk.Label(leftframe,text="Admin Panel",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel3['font']=Fontlabel
    leftframelabel3.place(relx=0.3,rely=0.6)

    mainframelabel=import_file_obj.tk.Label(frame,text='Admin Panel',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=Fontlabel2
    mainframelabel.place(relx=0.6,rely=0.1)


    #logo
    file_name="D:\FYP_project_temp\images\\admin_logo.jpeg"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)


    button_Student_report=import_file_obj.tk.Button(frame,text="View Student",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=student_view_call)
    button_Student_report.place(relx=0.55,rely=0.4,relwidth=c.user_menu_button_width,relheight=c.user_button_height)


    button_teacher_report=import_file_obj.tk.Button(frame,text="Faculty Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=faculty_call)
    button_teacher_report.place(relx=0.55,rely=0.55,relwidth=c.user_menu_button_width,relheight=c.user_button_height)

    button_maintain_course=import_file_obj.tk.Button(frame,text="Maintain Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=maintain_course_call)
    button_maintain_course.place(relx=0.55,rely=0.7,relwidth=c.user_menu_button_width,relheight=c.user_button_height)

    root.mainloop()

