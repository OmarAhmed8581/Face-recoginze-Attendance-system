#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 







c=import_file_obj.formatting_constant.constant


#<-------------------------------------------------------------Connection File ---------------------------------------->


Conection=import_file_obj.Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->

class Course_maintain():
    

    def __init__(self,event):
    

        # print(event)
        
        self.root = import_file_obj.tk.Tk()
        self.root.overrideredirect(True)           

        self.root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
        
        self.root.focus_set()  

        self.canvas = import_file_obj.tk.Canvas(self.root, height=c.form_height, width=c.form_width,)
        self.canvas.pack()
       


        self.Fontlabel = import_file_obj.font.Font(family=c.family, size=13, )
        self.Fontlabel1 = import_file_obj.font.Font(family=c.family, font=8, )
        self.Fontlabel2 = import_file_obj.font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )
        self.fontbutton=import_file_obj.font.Font(weight=c.button_style)


    #main frame
        self.frame=import_file_obj.tk.Frame(self.root,bg=c.frame_bg)
        self.frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

        self.headframe=import_file_obj.tk.Frame(self.frame,bg=c.headframe_bg)
        self.headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)

        self.file_name="D:\FYP_project_temp\images\\crossicon.png"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.on_click)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.98,rely=0.0)


        self.file_name="D:\FYP_project_temp\images\\back.png"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.menu_back)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.02,rely=0.03)

            
        self.leftframe=import_file_obj.tk.Frame(self.frame,bg=c.left_Frame_label_bg)
        self.leftframe.place(relx=0.0,rely=0.02,relwidth=c.register_leftframe_width,relheight=c.leftframe_height)



        #logo
        self.file_name="D:\FYP_project_temp\images\\admin_logo.jpeg"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.03,rely=0.09)



        self.mainframelabel=import_file_obj.tk.Label(self.frame,text='Course Maintain Options',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.mainframelabel['font']=self.Fontlabel2
        self.mainframelabel.place(relx=0.5,rely=0.1)


        self.button_Student_report=import_file_obj.tk.Button(self.leftframe,text="View Student",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.student_view_call)
        self.button_Student_report.place(relx=0.1,rely=0.4,relwidth=c.user_button_width,relheight=c.user_button_height)


        self.button_teacher_report=import_file_obj.tk.Button(self.leftframe,text="Faculty Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.faculty_call)
        self.button_teacher_report.place(relx=0.1,rely=0.55,relwidth=c.user_button_width,relheight=c.user_button_height)

        self.button_maintain_course=import_file_obj.tk.Button(self.leftframe,text="Maintain Course",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.maintain_course_call)
        self.button_maintain_course.place(relx=0.1,rely=0.7,relwidth=c.user_button_width,relheight=c.user_button_height)

        self.add_course=import_file_obj.tk.Button(self.frame,text='Add',bg=c.button_bg,fg=c.button_fg,command=self.add)
        self.add_course.place(relx=0.45,rely=0.2,relwidth=c.maintain_course_button_width,relheight=c.maintain_course_button_height)

        self.delete_course=import_file_obj.tk.Button(self.frame,text='Delete',bg=c.button_bg,fg=c.button_fg,command=self.delete)
        self.delete_course.place(relx=0.59,rely=0.2,relwidth=c.maintain_course_button_width,relheight=c.maintain_course_button_height)

        self.update_course=import_file_obj.tk.Button(self.frame,text='Update',bg=c.button_bg,fg=c.button_fg,command=self.update)
        self.update_course.place(relx=0.73,rely=0.2,relwidth=c.maintain_course_button_width,relheight=c.maintain_course_button_height)

        self.view_course=import_file_obj.tk.Button(self.frame,text='View',bg=c.button_bg,fg=c.button_fg,command=self.view)
        self.view_course.place(relx=0.87,rely=0.2,relwidth=c.maintain_course_button_width,relheight=c.maintain_course_button_height)



        #<----------------------------------- add course frame ------------------------------>

        self.add_course_frame = import_file_obj.tk.LabelFrame( self.frame, text="Add Course", padx=8, pady=8,bg=c.frame_bg,fg=c.course_frame_fg)
        self.add_course_frame.pack(padx=10, pady=15)
        self.add_course_frame.place(relx=0.5,rely=0.4)
    
        self.course_name_lbl = import_file_obj.tk.Label(self.add_course_frame, text="Enter Course Name: ",bg=c.frame_bg,fg=c.course_frame_fg)
        self.course_name_lbl.grid(row=0, column=0, sticky=import_file_obj.tk.E)
        self.course_name_txt = import_file_obj.tk.Entry(self.add_course_frame, bd=1, bg="white", highlightbackground="#bebebe", highlightthickness=1)
        self.course_name_txt.grid(row=0, column=1, ipady=1)
        
        self.addbutton=import_file_obj.tk.Button(self.add_course_frame,text="Add",bg=c.button_bg,fg=c.button_fg,command=self.Add_course)
        #addbutton.place(relx=0.68,rely=0.6,relwidth=4,relheight=2)
        self.addbutton.grid(row=1,column=1,ipadx=c.maintain_course_button_ipadx)
        self.add_course_frame.grid_rowconfigure(0, minsize=28)
        self.add_course_frame.grid_rowconfigure(1, minsize=28)


        #<----------------------------------------------------------------------------------->





        #<-------------------------------------- delete course frame------------------------>


        self.delete_course_frame = import_file_obj.tk.LabelFrame(self.frame, text="Delete Course", padx=8, pady=8,bg=c.frame_bg,fg=c.course_frame_fg)
        self.delete_course_frame.pack(padx=10, pady=10)
        self.delete_course_frame.place(relx=0.5,rely=0.4)
    
        self.select_course_lbl = import_file_obj.tk.Label(self.delete_course_frame, text="Select Course: ",bg=c.frame_bg,fg=c.course_frame_fg)
        self.select_course_lbl.grid(row=0, column=0, sticky=import_file_obj.tk.E)
        self.Delete_course_name_cb = import_file_obj.ttk.Combobox(self.delete_course_frame,values=self.selectcourse())
        course_data=self.selectcourse()
        self.Delete_course_name_cb['value']=course_data
        self.Delete_course_name_cb.grid(row=0, column=1, ipady=1)
        self.Delete_course_name_cb.bind("<<ComboboxSelected>>",self.show_course_id)

        self.Delete_select_course_id_lbl = import_file_obj.tk.Label(self.delete_course_frame, text="Select Course ID: ",bg=c.frame_bg,fg=c.course_frame_fg)
        self.Delete_select_course_id_lbl.grid(row=1, column=0, sticky=import_file_obj.tk.E)

        self.Delete_select_course_id_cb = import_file_obj.ttk.Combobox(self.delete_course_frame)
        # course_data=self.selectcourse()
        # self.Delete_select_course_id_lbl['value']=self.show_id
        self.Delete_select_course_id_cb.grid(row=1, column=1, ipady=1)







        self.delete_button=import_file_obj.tk.Button(self.delete_course_frame,text="Delete",bg=c.button_bg,fg=c.button_fg,command=self.Delete_course)
        self.delete_button.grid(row=2,column=1,ipadx=c.maintain_course_button_ipadx)

        self.delete_course_frame.grid_rowconfigure(0, minsize=28)
        self.delete_course_frame.grid_rowconfigure(1, minsize=28)


        #<--------------------------------------------------------------------------------------->


        #<----------------------------- update frame------------------------------------------->

    

        self.update_course_frame = import_file_obj.tk.LabelFrame(self.frame, text="Update Course", padx=8, pady=8,bg=c.frame_bg,fg=c.course_frame_fg)
        self.update_course_frame.pack(padx=10, pady=10)
        self.update_course_frame.place(relx=0.5,rely=0.4)
    
        self.select_course_lbl = import_file_obj.tk.Label(self.update_course_frame, text="Select Course: ",bg=c.frame_bg,fg=c.course_frame_fg)
        self.select_course_lbl.grid(row=0, column=0, sticky=import_file_obj.tk.E)

        # def textbox_value(self,e):

        #     self.combo_Value=self.course_name_cb.get()
        #     check_txtbox_value=self.update_course_txt.get('1.0','1.end')
        #     if not check_txtbox_value:
        #         self.update_course_txt.insert(INSERT, self.combo_Value)
        #     else:
        #         self.update_course_txt.delete('1.0','1.end')               
        #         self.update_course_txt.insert('END', self.combo_Value)


        
        self.course_name_cb = import_file_obj.ttk.Combobox(self.update_course_frame,values=self.selectcourse())
        course_data=self.selectcourse()
        self.course_name_cb['value']=course_data
        self.course_name_cb.grid(row=0, column=1, ipady=1)
        self.course_name_cb.bind("<<ComboboxSelected>>",self.call_update)

       
        self.update_course_lbl = import_file_obj.tk.Label(self.update_course_frame, text="Update course here: ",bg=c.frame_bg,fg=c.course_frame_fg)
        self.update_course_lbl.grid(row=1, column=0, sticky=import_file_obj.tk.E)

        

        self.update_course_name_txt = import_file_obj.tk.Entry(self.update_course_frame,bd=1,bg="white",highlightbackground="#bebebe",highlightthickness=1,)
        self.update_course_name_txt.place(relx=0.45,rely=0.4,relwidth=c.update_course_textbox_width)
        # self.update_course_name_txt.insert('end','a')
       
        
        self.update_button=import_file_obj.tk.Button(self.update_course_frame,text="Update",bg=c.button_bg,fg=c.button_fg,command=self.update_couse)
        self.update_button.grid(row=2,column=1,ipadx=c.maintain_course_button_ipadx)

        self.update_course_frame.grid_rowconfigure(0, minsize=28)
        self.update_course_frame.grid_rowconfigure(1, minsize=28)
        
        
    
    # /ef textArea(event=None):

    
    #     self.value_of_combo = self.course_name_cb.get()
    #     # print(self.value_of_combo)
    #     # Get the content of the Text widget
    #     r=self.update_course_txt.get('1.0','1.end')
    #     # If it is empty then insert the selected value directly
    #     if not r:
    #         self.update_course_txt.insert(INSERT, self.value_of_combo) 
    #         # If not empty then delete existing text and insert the selected value
    #     else: 
    #         self.update_course_txt.delete('1.0','1.end')               
    #         self.update_course_txt.insert(END, self.value_of_combo)



    # def combo(self):  
    #     self.course_name_cb = ttk.Combobox(self.update_course_frame,values=self.selectcourse(),state='readonly')
    #     course_data=self.selectcourse()
    #     self.course_name_cb['value']=course_data
    #     self.course_name_cb.bind('<<ComboboxSelected>>',self.textArea)
    #     self.course_name_cb.current(0)
    #     self.course_name_cb.grid(column=0, row=0)        

    #     self.update_course_txt = tk.Label(self.update_course_frame, text="Update course here: ",bg=c.frame_bg,fg=c.course_frame_fg)
    #     self.update_course_txt.grid(row=1, column=0, sticky=tk.E)
    #     self.update_course_name_txt = tk.Entry(self.update_course_frame,bd=1,bg="white",highlightbackground="#bebebe",highlightthickness=1,)
    #     self.update_course_name_txt.place(relx=0.45,rely=0.4,relwidth=c.update_course_textbox_width)


        
 
        



        #<----------------------- view course frame------------------------------------------>

        self.view_course_frame = import_file_obj.tk.LabelFrame(self.frame, text="View Course", padx=8, pady=8,bg=c.frame_bg,fg=c.course_frame_fg)
        self.view_course_frame.pack(padx=10, pady=10)
        self.view_course_frame.place(relx=0.5,rely=0.4)
    
        self.view_course_frame.grid_rowconfigure(0, minsize=40)
        self.view_course_frame.grid_rowconfigure(1, minsize=40)

        

        self.tv=import_file_obj.ttk.Treeview(self.frame,columns=(1,2),show="headings",xscroll=0.3)
        self.tv.column(1,width=100)
        self.tv.column(2,width=150)


        self.tv.heading(1,text="Course ID")
        self.tv.heading(2,text="Course Name")

        self.tv.tag_configure(1, background="red")
        self.tv.place(relx=0.5,rely=0.3)

        Conection.cursor.execute("select OFFER_COURSE_ID from course_offer")
        result=Conection.cursor.fetchall()
        length=len(result)
        for i in range(0,length):
            Conection.cursor.execute("select COURSE_NAME from course c join course_offer co on c.COURSE_ID=co.COURSE_ID_F where co.OFFER_COURSE_ID=?",(result[i][0]))
            course_name=Conection.cursor.fetchall()

            if(len(course_name)!=0):

                l=[(result[i][0],course_name[0][0])]
                for index in l:

                    self.tv.insert('','end',values=index)



        self.hide()


        if event == "Delete":
            self.delete()
        elif event == "ADD":
            self.add()
        elif event == "UPDATE":
            self.update()        





        self.root.mainloop()

#-------------------------------------------------Functionality of add,delete,update,select are here-----------------------
    def show_course_id (self,event=None):
        self.show_id=[]
        
        Conection.cursor.execute("select COURSE_ID from course where COURSE_NAME=?",(self.Delete_course_name_cb.get()))
        course_name_result=Conection.cursor.fetchall()


        Conection.cursor.execute("select OFFER_COURSE_ID from course_offer where COURSE_ID_F=?",(course_name_result[0][0]))
        result=Conection.cursor.fetchall()

        for i in range(len(result)):
            self.show_id.append(result[i][0])
        self.Delete_select_course_id_cb['value']=self.show_id
        self.Delete_select_course_id_cb.current(0)





    def selectcourse(self):
        data=[]
        Conection.cursor.execute('select COURSE_NAME from course')
        result=Conection.cursor.fetchall()
        for row in result:
            data.append(row[0])
        return data    

    # def textbox_value(self,event=None):
    #         # self.select_course=course_name_cb.get()run kro
    #         name=self.course_name_cb.get()
    #         self.update_course_name_txt['text']=name

    # def textbox_value(event=None):
    #     value=tk.StringVar(self.update_course_frame,value=self.course_name_cb.get())
    #     update_course_name_txt['textvariable']=value

    

   
    
    def hide(self):
        self.add_course_frame.place_forget() 
        self.delete_course_frame.place_forget() 
        self.update_course_frame.place_forget()
        self.view_course_frame.place_forget()  
        self.tv.place_forget()

    def add(self):
        self.add_course_frame.place(relx=0.5,rely=0.4)
        self.delete_course_frame.place_forget()
        self.update_course_frame.place_forget()
        self.view_course_frame.place_forget()
        self.tv.place_forget()

    def delete(self):
        self.add_course_frame.place_forget()
        self.update_course_frame.place_forget()   
        self.view_course_frame.place_forget()
        self.delete_course_frame.place(relx=0.5,rely=0.4)
        self.tv.place_forget() 

    def update(self):
        self.add_course_frame.place_forget()
        self.delete_course_frame.place_forget()
        self.view_course_frame.place_forget()
        self.update_course_frame.place(relx=0.5,rely=0.4)
        self.tv.place_forget()
        
    def view(self):
        self.add_course_frame.place_forget()
        self.delete_course_frame.place_forget()
        self.update_course_frame.place_forget()
        self.view_course_frame.place(relx=0.5,rely=0.4)
        self.tv.place(relx=0.5,rely=0.4)




#------------------------side buttons---------------------------------------
    def on_click(self,event=None):
        self.root.destroy()

    def menu_back(self,event=None):
        self.root.destroy()
        import Admin_Menu
        Admin_Menu.admin_menu()

    def student_view_call(self):
        self.root.destroy()
        import student_view
        student_view.student_view()

    def maintain_course_call(self):
        self.root.destroy()
        import course_maintain

    def faculty_call(self):
        self.root.destroy()
        import assigned_course_teacher
        assigned_course_teacher.teacher_course(None) 

#------------------------------------------------------------------------------------

    def Add_course(self):
        name=self.course_name_txt.get()

        if name != "":
        
            courses_f=import_file_obj.os.chdir('D:\FYP_project_temp\course')

            #course_folder=os.mkdir(name)  #for creating course folder
            # name_dataset=name+"_dataset"
        
            #course_folder=os.mkdir(name)
            # os.mkdir(name_dataset) 
            Conection.cursor.execute("select * from course where COURSE_NAME=?",(name))
            result=Conection.cursor.fetchall()

            if(len(result) == 0):
                
                Conection.cursor.execute('insert into course(COURSE_NAME)values(?)',(name))

                Conection.cursor.execute('select COURSE_ID from course where COURSE_NAME=?',(name))

                result_id=Conection.cursor.fetchall()

                Conection.cursor.execute('insert into course_offer(COURSE_ID_F)values(?)',(result_id[0][0]))
                
                Conection.cursor.execute('select max(OFFER_COURSE_ID) from course_offer')
                result_course_offer_id=Conection.cursor.fetchall()
                
                dataset_course_name=str(result_course_offer_id[0][0])+" "+name+"_dataset"
                import_file_obj.os.mkdir(dataset_course_name)

                # new course id
                Conection.cursor.execute('select max(COURSE_ID) from course')
                max_course_id=Conection.cursor.fetchall()
                max_id=max_course_id[0][0]

                # number of student id get
                Conection.cursor.execute('select STD_ID from student_registeration_record')
                number_of_student_id=Conection.cursor.fetchall()
                length=len(number_of_student_id)

                
                import_file_obj.messagebox.showinfo("Message","Course is added")    


                if(length!=0):  # check if there is one or more student
                    for index in range(0,length):
                        Conection.cursor.execute('insert into student_Assigned_course(STUDENT_ID_F,COURSE_ID_F)values(?,?)',str(number_of_student_id[index][0]),max_id)
            else:
                Conection.cursor.execute('select COURSE_ID from course where COURSE_NAME=?',(name))
                result_id=Conection.cursor.fetchall()


                Conection.cursor.execute('insert into course_offer(COURSE_ID_F)values(?)',(result_id[0][0]))

                Conection.cursor.execute('select max(OFFER_COURSE_ID) from course_offer where COURSE_ID_F=?',(result_id[0][0]))
                max_id=Conection.cursor.fetchall()

                dataset_course_name=str(max_id[0][0])+" "+name+"_dataset"
                import_file_obj.os.mkdir(dataset_course_name)

                
                import_file_obj.messagebox.showinfo("Message","Course is added")    




            Conection.conn.commit()
            self.root.destroy()
            Course_maintain("ADD")
        else:
            import_file_obj.messagebox.showerror("Error","please insert Course Name")
            





    
    def Delete_course(self):
        name=self.Delete_course_name_cb.get()
        id=self.Delete_select_course_id_cb.get()

        if name != "" and id != "":


            Conection.cursor.execute("Select COURSE_ID from course where COURSE_NAME=?",(name))
            course_id=Conection.cursor.fetchall()

            Conection.cursor.execute("Select count(*) from course_offer where COURSE_ID_F=?",(course_id[0][0]))
            count=Conection.cursor.fetchall()

            Conection.cursor.execute('select STUDENT_ID_F from student_course_record where COURSE_ID_F=?',(id))
            student_count=Conection.cursor.fetchall()

            #            0 ,1
            #        0=(1233,)
            if len(student_count) == 0:
                if count[0][0] > 1:



                    Conection.cursor.execute("Delete from course_offer where OFFER_COURSE_ID=?",(id))
                    course_folder_name=id+" "+name+"_dataset"

                    path='D:\FYP_project_temp\course'
                    import_file_obj.os.chdir(path)
                    import_file_obj.os.rmdir(course_folder_name)
                    Conection.cursor.commit()
                    import_file_obj.messagebox.showinfo("Message","Course is Deleted")
                    self.root.destroy()
                    Course_maintain("Delete")
                    
                else:

                    Conection.cursor.execute("Delete from course where COURSE_NAME=?",(name))

                    Conection.cursor.execute("Delete from course_offer where OFFER_COURSE_ID=?",(id))
                    course_folder_name=id+" "+name+"_dataset"

                    path='D:\FYP_project_temp\course'
                    import_file_obj.os.chdir(path)
                    import_file_obj.os.rmdir(course_folder_name)
                    Conection.cursor.commit()
                    import_file_obj.messagebox.showinfo("Message","Course is Deleted")
                    self.root.destroy()
                    Course_maintain("Delete")
            else:

                if count[0][0] > 1:

                    path='D:\FYP_project_temp\course'  

                    Conection.cursor.execute('Delete from  student_course_record where COURSE_ID_F=?',(id))

                    Conection.cursor.execute("Delete from course_offer where OFFER_COURSE_ID=?",(id))
                    course_images_name='D:\FYP_project_temp\course/'+id+" "+name+"_dataset"
                

                    # remove images for course folder
                    import_file_obj.os.chdir(course_images_name)
                    for student_index in range(0,len(student_count)):
                        for index in range(0,4):
                            student_path=str(student_count[student_index][0])+" "+str(index)+'.jpg'
                            import_file_obj.os.remove(student_path)

                    # remove course folder    
                    import_file_obj.os.chdir(path)    
                    course_folder_name=id+" "+name+"_dataset"
                    import_file_obj.os.rmdir(course_folder_name)
                    Conection.cursor.commit()
                    import_file_obj.messagebox.showinfo("Message","Course is Deleted")
                    self.root.destroy()
                    Course_maintain("Delete")
                    
                else:

                    path='D:\FYP_project_temp\course'
                    # path1="D:\FYP_project_temp\course\"

                    Conection.cursor.execute("Delete from course where COURSE_NAME=?",(name))

                    Conection.cursor.execute('Delete from  student_course_record where COURSE_ID_F=?',(id))

                    Conection.cursor.execute("Delete from course_offer where OFFER_COURSE_ID=?",(id))
                    course_images_name='D:\FYP_project_temp\course/'+id+" "+name+"_dataset"
                
                    import_file_obj.os.chdir(course_images_name)
                    for student_index in range(0,len(student_count)):
                        for index in range(0,4):
                            student_path=str(student_count[student_index][0])+" "+str(index)+'.jpg'
                            import_file_obj.os.remove(student_path)
                    import_file_obj.os.chdir(path)   
                    course_folder_name=id+" "+name+"_dataset"
                    import_file_obj.os.rmdir(course_folder_name)
                    Conection.cursor.commit()
                    import_file_obj.messagebox.showinfo("Message","Course is Deleted")
                    
                    self.root.destroy()
                    Course_maintain("Delete")
        else:
            import_file_obj.messagebox.showerror("Error","please select course Name and course Id")
                


            



        
        # query='delete from course where COURSE_NAME= ?'
        # Conection.cursor.execute(query,(name))
        # os.rmdir(name) #for deleting oourse folder
        # Conection.conn.commit()
        # messagebox.showinfo("Message","Course is Deleted")

    def call_update(self,event=None):
        v = import_file_obj.tk.StringVar(self.root, value=self.course_name_cb.get())
        self.update_course_name_txt['textvariable']=v

    def update_couse(self):
        if self.update_course_name_txt.get() != "" and self.course_name_cb.get() != "":
            Conection.cursor.execute('update course set COURSE_NAME=? where COURSE_NAME=?',(self.update_course_name_txt.get(),self.course_name_cb.get()))
            Conection.conn.commit()
            import_file_obj.messagebox.showinfo('Info','Course name is updated!')
            self.root.destroy()
            Course_maintain("UPDATE")
        else:
            import_file_obj.messagebox.showerror("Error","please select course Name")
              





    
    
        








