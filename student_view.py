
#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 




c=import_file_obj.formatting_constant.constant



#<------------------------------------------- create an object of Connection File ---------------------------------------->



Conection=import_file_obj.Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->
def student_view():
 
#------------------------------side options------------------------------------------#
    
    def call():
        root.destroy()
        import student_view
        student_view.student_view()

    def Course_call():
        root.destroy()
        import course_maintain
        p=course_maintain.Course_maintain(None)

    def faculty_call():
        root.destroy()
        import assigned_course_teacher
        assigned_course_teacher.teacher_course(None)
#------------------------------side options------------------------------------------#
    

  

   
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


#cross symbol
    file_name="D:\FYP_project_temp\images\crossicon.png"
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
    file_name="D:\FYP_project_temp\images\\admin_logo.jpeg"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)

    
    def Data(event=None):
        id=int(std_data_listbox.curselection()[0])
        value=std_data_listbox.get(id)
        new=value.split()
        root.destroy()
        #print(new[0])
        import student_data
        student_data.Student_data(new[0])




    button_Student_report=import_file_obj.tk.Button(leftframe,text="View Student",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=call)
    button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


    button_teacher_report=import_file_obj.tk.Button(leftframe,text="Faculty Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=faculty_call)
    button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

    button_maintain_course=import_file_obj.tk.Button(leftframe,text="Maintain Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=Course_call)
    button_maintain_course.place(relx=0.1,rely=0.7,relwidth=c.user_button_width,relheight=c.user_button_height)




    mainframelabel=import_file_obj.tk.Label(frame,text='View Student Data',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    mainframelabel['font']=Fontlabel2
    mainframelabel.place(relx=0.56,rely=0.1)

    id_lbl=import_file_obj.tk.Label(frame,text="Student Id",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    id_lbl['font']=Fontlabel
    id_lbl.place(relx=0.50,rely=0.2)

    name_lbl=import_file_obj.tk.Label(frame,text="Student Name",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
    name_lbl['font']=Fontlabel
    name_lbl.place(relx=0.73,rely=0.2)

    std_data_listbox=import_file_obj.tk.Listbox(frame,bg='#35394a',fg='white',bd=0)
    std_data_listbox.place(relx=0.5,rely=0.25,relwidth=0.45,relheight=0.5)
    std_data_listbox.bind('<Button-1>',Data)


#-----------------------id and name query---------------------------------------#
    query="select STD_ID,STD_NAME from student_registeration_record"
    Conection.cursor.execute(query)
    result=Conection.cursor.fetchall()
    l=len(result)


#--------------------------------------------------------------------------------#

    scrollbar = import_file_obj.tk.Scrollbar(std_data_listbox)
    scrollbar.pack(side='right', fill='y')
    for line in range(0,l):
        std_data_listbox.insert(import_file_obj.tk.END, str(result[line][0])+"                                                 "+str(result[line][1]))
    # for i in range(100):
    #     std_data_listbox.insert('end', i)
# attach listbox to scrollbar




    std_data_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=std_data_listbox.yview)





    # add_course_btn=tk.Button(frame,text="FIND",bg=c.frame_bg,fg=c.button_fg,borderwidth=2,command=Data)
    # add_course_btn['font']=fontbutton       

    # add_course_btn.place(relx=0.6,rely=0.8,relwidth=0.25,relheight=0.06)
   



    root.mainloop()

# student_view()