# <--------------------------- create an object of import file--------------------------->
import Import_file
import_file_object=Import_file


# #<------------------------------------------- create an object of formatting Constant--------> 

# formatting_constant_object=import_file_object.formatting_constant.constant


#<------------------------------------------- create an object of formatting Constant--------> 

c=import_file_object.formatting_constant.constant


    
def msgbox(name,id,login_root):


    msg_root=import_file_object.tk.Tk()
       
    msg_root.overrideredirect(True)
    msg_root.geometry('%dx%d+%d+%d' % (320,220,500,260))
    msg_root.config(bg="white")
    msg_root.focus_set() 

     

        # self.headframe=tk.Frame(self.root,bg="#377fc3")
        # self.headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height+0.02)

    # file_name="D:\success_404675.png"
    # stdfilee=Image.open(file_name)
    # stdshow=ImageTk.PhotoImage(stdfilee)
    # imageshow=tk.Label(image=stdshow)
    # imageshow.image=stdshow
    # imageshow.place(relx=0.32,rely=0.0)

    headframe=import_file_object.tk.Frame(msg_root,bg="#8CD4F5")
    headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height+0.02)


    fontt=import_file_object.font.Font(weight='bold')
    Success_label=import_file_object.tk.Label(msg_root,text="Congrats!",fg="#575757",bg="white",)
    Success_label['font']=fontt
    Success_label.config(font=("Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", 26))
    Success_label.place(relx=0.23,rely=0.2)

      
    text_label=import_file_object.tk.Label(msg_root,text=name,fg="#797979",bg="white")
    text_label.config(font=("Gudea,sans-serif", 13))
    text_label.place(relx=0.23,rely=0.43)


        # self.footerframe=tk.Frame(self.root,bg="#377fc3")
        # self.footerframe.place(relx=0.0,rely=0.96,relwidth=c.headframe_width,relheight=c.headframe_height+0.04)
    
    def call_student_menu(event=None):
        msg_root.destroy()
        login_root.destroy()
        import Student_Menu
        Student_Menu.Student_menu(id)
        
    Ok_button=import_file_object.tk.Button(msg_root,text="OK",bg="#8CD4F5",fg="white",borderwidth=1,relief="raised",command=call_student_menu)
    Ok_button.place(relx=0.33,rely=0.65,relwidth=0.32,relheight=0.14)
    Ok_button.config(font=("'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", 17))

    msg_root.mainloop()