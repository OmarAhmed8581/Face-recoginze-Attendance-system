
#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 



c=import_file_obj.formatting_constant.constant


#<-------------------------------------------------------------Connection File ---------------------------------------->

Conection=import_file_obj.Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->


def faculty_menu(id):

    def student_record():
        root.destroy()
        import teacher_attendance_report
        p=teacher_attendance_report.attendance_report(id)

    def take_attendance():
        root.destroy()
        import take_Attendance
        p=take_Attendance.Take_Attendance(id)    


    root=import_file_obj.tk.Tk()
    root.title("LOGIN FORM")
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
    root.focus_set()  

    canvas = import_file_obj.tk.Canvas(root, height=c.form_height, width=c.form_width,)
    canvas.pack()
   
    Fontlabel = import_file_obj.font.Font(family=c.family, size=13, )
    Fontlabel1 = import_file_obj.font.Font(family=c.family, font=8, )
    Fontlabel2 = import_file_obj.font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )
    fontbutton=import_file_obj.font.Font(weight=c.button_style)

    
  

    #main frame
    frame=import_file_obj.tk.Frame(root,bg=c.frame_bg)
    frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

    headframe=import_file_obj.tk.Frame(frame,bg=c.headframe_bg)
    headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)


    def on_click(event=None):
        root.destroy()


 #left frame
    
    leftframe=import_file_obj.tk.Frame(frame,bg=c.left_Frame_label_bg)
    leftframe.place(relx=0.0,rely=0.02,relwidth=c.leftframe_width,relheight=c.leftframe_height)

    def login_back(event=None):
        root.destroy()
        import login
         

    #back 
    back_label=import_file_obj.tk.Label(frame,text="\U000021B5 Login Out",bg=c.leftframe_bg,fg='white')
    back_label.config(font=("Gudea,sans-serif", 13))
    back_label.place(relx=0.02,rely=0.022)
    back_label.bind('<Button-1>',login_back)


    #logo
    file_name="D:\FYP_project_temp\images\\teacher_logo.jpeg"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)



   

    leftframelabel1=import_file_obj.tk.Label(leftframe,text="Welcome to the",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel1['font']=Fontlabel
    leftframelabel1.place(relx=0.3,rely=0.37)

    leftframelabel2=import_file_obj.tk.Label(leftframe,text="Student Attendance System",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel2['font']=Fontlabel
    leftframelabel2.place(relx=0.3,rely=0.43)

    leftframelabel3=import_file_obj.tk.Label(leftframe,text="Faculty Panel",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
    leftframelabel3['font']=Fontlabel
    leftframelabel3.place(relx=0.3,rely=0.5)

    mainframelabel=import_file_obj.tk.Label(frame,text='Faculty Panel',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=Fontlabel2
    mainframelabel.place(relx=0.6,rely=0.1)


    take_attendance_btn=import_file_obj.tk.Button(frame,text="Take Attendance",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=take_attendance)
    take_attendance_btn.place(relx=0.55,rely=0.3,relwidth=c.user_menu_button_width,relheight=c.user_button_height)

    student_attendance_report_btn=import_file_obj.tk.Button(frame,text="Student Attendance Report",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=student_record)
    student_attendance_report_btn.place(relx=0.55,rely=0.5,relwidth=c.user_menu_button_width,relheight=c.user_button_height)
    root.mainloop()

