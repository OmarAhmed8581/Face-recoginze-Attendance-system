#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 


c=import_file_obj.formatting_constant.constant
Conection=import_file_obj.Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->
def Student_data(id):


    Conection.cursor.execute("SELECT  STD_ID,STD_NAME,STD_FATHER_NAME,STD_EMAIL,STD_PHONE_NO,STD_NIC,STD_CITY,STD_ADDRESS,STD_PROGRAM from  student_registeration_record where  STD_ID=?",(id))
    result=Conection.cursor.fetchall()
    s_id=result[0][0]
    name=result[0][1]
   
    father_name=result[0][2]
    email=result[0][3]
    phone=result[0][4]
    nic=result[0][5]
    city=result[0][6]
    address=result[0][7]
    program=result[0][8]

    
    
    



    

    # def find():
        
    #     std=std_id_txt.get()
    #     Conection.cursor.execute('select std_id,std_name,std_photo from  student_registeration_record where std_id=?',(std))
    #     m=Conection.cursor.fetchall()
#following this code
    #     temp=0.17
    #     for x in m:
    #         temp=temp+0.40
    #         id=x[0]
    #         name=x[1]
    #         photo=x[2]

    #         x1=str(id)
    #         path='student_image/'+x1+'.png'
    #         with open(path,'wb') as m:
    #             m.write(photo)
                
    #         stdfilee=Image.open(path)
    #         stdshow=ImageTk.PhotoImage(stdfilee)
    #         imageshow=tk.Label(image=stdshow)
    #         imageshow.image=stdshow
    #         imageshow.place(relx=0.37,rely=temp) 

    #     select_idlbl1=tk.Label(root,text=id,font=20,bg="#FBEAFE",fg='black')
    #     select_idlbl1.place(relx=0.60,rely=temp) 
    #     select_namelbl1=tk.Label(root,text=name,font=20,bg="#FBEAFE",fg='black')
    #     select_namelbl1.place(relx=0.78,rely=temp) 
      
#------------------------------side options------------------------------------------#
    def call():
        root.destroy()
        import student_view
        student_view.student_view()

    def Course_call():
        root.destroy()
        import course_maintain
        course_maintain.Course_maintain(None)

    def faculty_call():
        root.destroy()
        import assigned_course_teacher
        assigned_course_teacher.teacher_course(None)
#------------------------------side options------------------------------------------#
    

  

   
    root=import_file_obj.tk.Tk()
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
    root.focus_set()  

    canvas = import_file_obj.tk.Canvas(root, height=c.form_height, width=c.form_width,)
    canvas.pack()
   
    # Fontlabel = font.Font(family=c.family, size=13, )
    # Fontlabel1 = font.Font(family=c.family, font=8, )
    # Fontlabel2 = font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )
    # fontbutton=font.Font(weight=c.button_style)


    heading_font = import_file_obj.font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style_heading )
    rightframe_font = import_file_obj.font.Font(family=c.family, size=c.label_font_main_frame, )
    leftframe_font= import_file_obj.font.Font(family=c.family, size=c.label_font_main_frame, )
    other_font = import_file_obj.font.Font(family=c.family, size=c.label_font_other, )
    button_font=import_file_obj.font.Font(weight=c.button_style)

    
  

    #main frame
    frame=import_file_obj.tk.Frame(root,bg=c.frame_bg)
    frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

    headframe=import_file_obj.tk.Frame(frame,bg=c.headframe_bg)
    headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)


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
    

#left frame
    
    leftframe=import_file_obj.tk.Frame(frame,bg=c.left_Frame_label_bg)
    leftframe.place(relx=0.0,rely=0.02,relwidth=0.40,relheight=c.leftframe_height)

    def menu_back(event=None):
        root.destroy()
        import Admin_Menu
        Admin_Menu.admin_menu()   

    #back 
    file_name="D:\FYP_project_temp\images\\back.png"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.bind('<Button-1>', menu_back)
    imageshow.image=stdshow
    imageshow.place(relx=0.02,rely=0.03)

    #logo
    file_name="D:\FYP_project_temp\images\\studentlogo.jpeg"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)


    button_Student_report=import_file_obj.tk.Button(leftframe,text="View Student",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=call)
    button_Student_report['font']=button_font
    button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


    button_teacher_report=import_file_obj.tk.Button(leftframe,text="Faculty Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=faculty_call)
    button_teacher_report['font']=button_font
    button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

    button_maintain_course=import_file_obj.tk.Button(leftframe,text="Maintain Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=Course_call)
    button_maintain_course['font']=button_font
    button_maintain_course.place(relx=0.1,rely=0.7,relwidth=c.user_button_width,relheight=c.user_button_height)




    mainframelabel=import_file_obj.tk.Label(frame,text='Student Details',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=heading_font
    mainframelabel.place(relx=0.46,rely=0.1)



    id_lbl=import_file_obj.tk.Label(frame,text="Id",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    id_lbl.place(relx=0.45,rely=0.30)
    std_id=import_file_obj.tk.Label(frame,text=s_id,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_id.place(relx=0.6,rely=0.30)


    name_lbl=import_file_obj.tk.Label(frame,text="Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    name_lbl.place(relx=0.45,rely=0.35)
    std_name=import_file_obj.tk.Label(frame,text=name,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_name.place(relx=0.6,rely=0.35)

    fathername_lbl=import_file_obj.tk.Label(frame,text="Father Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    fathername_lbl.place(relx=0.45,rely=0.4)
    std_father_name=import_file_obj.tk.Label(frame,text=father_name,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_father_name.place(relx=0.6,rely=0.4)

    email_lbl=import_file_obj.tk.Label(frame,text="Email Address",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    email_lbl.place(relx=0.45,rely=0.45)
    std_email=import_file_obj.tk.Label(frame,text=email,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_email.place(relx=0.6,rely=0.45)


    phone_lbl = import_file_obj.tk.Label(frame, text="Phone Number", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    phone_lbl.place(relx=0.45,rely=0.5)
    std_phone=import_file_obj.tk.Label(frame,text=phone,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_phone.place(relx=0.6,rely=0.5)
    

    program_lbl = import_file_obj.tk.Label(frame, text="Program", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    program_lbl.place(relx=0.45,rely=0.55)
    std_program=import_file_obj.tk.Label(frame,text=program,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_program.place(relx=0.6,rely=0.55)
   

    nic_lbl = import_file_obj.tk.Label(frame, text="NIC", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    nic_lbl.place(relx=0.45,rely=0.6)
    std_nic=import_file_obj.tk.Label(frame,text=nic,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_nic.place(relx=0.6,rely=0.6)
   

    city_lbl = import_file_obj.tk.Label(frame, text="City", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    city_lbl.place(relx=0.45,rely=0.65)
    std_city=import_file_obj.tk.Label(frame,text=city,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_city.place(relx=0.6,rely=0.65)
  

    address_lbl=import_file_obj.tk.Label(frame, text="Address", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
    address_lbl.place(relx=0.45,rely=0.7)
    std_address=import_file_obj.tk.Label(frame,text=address,bg=c.main_frame_label_bg,fg=c.main_frame_label_fg)
    std_address.place(relx=0.6,rely=0.7)

#photo
    # x1=str(id)
    # path='student_image/'+x1+'.png'
    # with open(path,'wb') as m:
    #      m.write(photo)
                
    # stdfilee1=Image.open(path)
    # stdshow1=ImageTk.PhotoImage(stdfilee1)
    # imageshow1=tk.Label(image=stdshow1)
    # imageshow1.image=stdshow1
    # imageshow1.place(relx=0.81,rely=0.2) 


    





    



    # add_course_btn=tk.Button(frame,text="FIND",bg=c.frame_bg,fg=c.button_fg,borderwidth=2,)
    # add_course_btn['font']=fontbutton       
    # add_course_btn.place(relx=0.50,rely=0.6,relwidth=0.20,relheight=0.06)
   



    root.mainloop()

