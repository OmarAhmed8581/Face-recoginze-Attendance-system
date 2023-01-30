
#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 

formatting_constant_object=import_file_obj.formatting_constant.constant



#<-------------------------------------------------- create and oject of  Connection File --------------------------------------------------->


connection_object=import_file_obj.Global_Class.Global



#<--------------------------------------------------Placeholder--------------------------------------------------->


class EntryWithPlaceholder(import_file_obj.tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()
  

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()



#<-----------------------------------------    Login Form -------------------------------------------------------->

def Login():


    def loginn(event=None):
    
        email_address=email_textbox.get()
        passwordd=password_textbox.get()

        user=combox.get()
        if user != "Login As":
            if email_address != "" and passwordd != "" and  passwordd !="Password" and email_address !="Email Address":
                from Controller import login_Validation
                login_Validation.Login(email_address,passwordd,user,root)
            else:
              # import_file_obj.messagebox.showwarning('warning','please fill required field')
                Required.place(relx=0.5,rely=0.6,relwidth=formatting_constant_object.frame_width,relheight=0.08)
                Required_lb.place(relx=0.02,rely=0.2)
 
        else:
            import_file_obj.messagebox.showwarning('warning','please Select Login as')



    def std_register_call(event=None):
        
        user=combox.get()
        if(user == "Student"):
            root.destroy
            import student_registeration
            p=student_registeration.Student_Register()
                    
    
        elif(user == "Faculty"):
            root.destroy
            import Teacher_Register
            Teacher_Register.Faculty_Register()
        else:
            import_file_obj.messagebox.showwarning('warning','please Select Login as')
            
      



    root=import_file_obj.tk.Tk()
    style=import_file_obj.ttk.Style()
    root.title("LOGIN FORM")
    root.overrideredirect(True)
    root.geometry('%dx%d+%d+%d' % (formatting_constant_object.form_width, formatting_constant_object.form_height,formatting_constant_object.form_x, formatting_constant_object.form_y))
    root.focus_set()  

    canvas =import_file_obj.tk.Canvas(root, height=formatting_constant_object.form_height, width=formatting_constant_object.form_width,)
    canvas.pack()   
    Fontlabel = import_file_obj.font.Font(family=formatting_constant_object.family, size=13, )
    Fontlabel1 = import_file_obj.font.Font(family=formatting_constant_object.family, font=8, )
    Fontlabel2 = import_file_obj.font.Font(family=formatting_constant_object.family, size=formatting_constant_object.label_font_heading_, weight=formatting_constant_object.label_style )
    fontbutton=   import_file_obj.font.Font(weight=formatting_constant_object.button_style)


#main frame
    frame=import_file_obj.tk.Frame(root,bg=formatting_constant_object.frame_bg)
    frame.place(relx=0.0,rely=0.0,relwidth=formatting_constant_object.frame_width,relheight=formatting_constant_object.frame_height)

    headframe=import_file_obj.tk.Frame(frame,bg=formatting_constant_object.headframe_bg)
    headframe.place(relx=0.0,rely=0.0,relwidth=formatting_constant_object.headframe_width,relheight=formatting_constant_object.headframe_height)


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
    
    leftframe=import_file_obj.tk.Frame(frame,bg=formatting_constant_object.left_Frame_label_bg)
    leftframe.place(relx=0.0,rely=0.02,relwidth=formatting_constant_object.leftframe_width,relheight=formatting_constant_object.leftframe_height)


#textbox email frame

    textbox_email_frame=import_file_obj.tk.Frame(frame,bg=formatting_constant_object.textbox_Frame_bg)
    textbox_email_frame.place(relx=0.5,rely=0.4,relwidth=formatting_constant_object.textbox_width,relheight=formatting_constant_object.textbox_height)
    

#textbox password frame

    textbox_password_frame=import_file_obj.tk.Frame(frame,bg=formatting_constant_object.textbox_Frame_bg)
    textbox_password_frame.place(relx=0.5,rely=0.5,relwidth=formatting_constant_object.textbox_width,relheight=formatting_constant_object.textbox_height)


    
    #logo
    file_name="D:\FYP_project_temp\images\\iconlogo.png"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.03,rely=0.08)

    leftframelabel1=import_file_obj.tk.Label(leftframe,text="Welcome to the",fg=formatting_constant_object.left_Frame_label_fg,bg=formatting_constant_object.left_Frame_label_bg)
    leftframelabel1['font']=Fontlabel
    leftframelabel1.place(relx=0.3,rely=0.37)

    leftframelabel2=import_file_obj.tk.Label(leftframe,text="Student Attendance System",fg=formatting_constant_object.left_Frame_label_fg,bg=formatting_constant_object.left_Frame_label_bg)
    leftframelabel2['font']=Fontlabel
    leftframelabel2.place(relx=0.3,rely=0.43)

    leftframelabel3=import_file_obj.tk.Label(leftframe,text="access portal",fg=formatting_constant_object.left_Frame_label_fg,bg=formatting_constant_object.left_Frame_label_bg)
    leftframelabel3['font']=Fontlabel
    leftframelabel3.place(relx=0.3,rely=0.5)

    
    mainframelabel=import_file_obj.tk.Label(frame,text='Login to your account',fg=formatting_constant_object.main_frame_label_fg,bg=formatting_constant_object.main_frame_label_bg)
    mainframelabel['font']=Fontlabel
    mainframelabel.place(relx=0.6,rely=0.2)



#placeholder #4e546d

    
    
    style.configure( 'TCombobox', font=('Purisa', 10, 'bold'), background ='#EFFFE1',fieldbackground='red')
    cblable=import_file_obj.tk.Label(frame,text="Login As?",fg=formatting_constant_object.main_frame_label_fg,bg=formatting_constant_object.main_frame_label_bg)
    cblable['font']=Fontlabel1
    cblable.place(relx=0.52,rely=0.3)
    userlogin=["Faculty","Student","Admin"]
    combox=import_file_obj.ttk.Combobox(frame,values=userlogin,state='readonly')
    combox.current(0)
    combox.place(relx=0.65,rely=0.3,relwidth=formatting_constant_object.combox_width,relheight=formatting_constant_object.combox_height)
    combox.master.option_add( '*TCombobox*Listbox.background', '#EFFFE1')

    Required=import_file_obj.tk.Frame(frame,bg="#EBEBEB")
    Required.place(relx=0.5,rely=0.6,relwidth=formatting_constant_object.frame_width,relheight=0.085)

    Required_lb=import_file_obj.tk.Label(Required,text="*Please Fill Required Data",bg="#EBEBEB",fg="Red")
    Required_lb.config(font=("Times New Roman", 11))
    Required_lb.place(relx=0.02,rely=0.2)

    Required.place_forget()
    Required_lb.place_forget()

    
    
# email_label=tk.Label(frame,text="Email",fg='white',bg='violet')
# email_label['font']=Fontlabel1
# email_label.place(relx=0.6,rely=0.3)

    email_textbox=EntryWithPlaceholder(textbox_email_frame, "Email Address",)
    #email_textbox=tk.Entry(frame,bg=c.textbox_bg)
    email_textbox.place(relx=0.1,rely=0.0,relwidth=formatting_constant_object.login_textbox_width,relheight=formatting_constant_object.login_textbox_height)
    email_textbox.icursor(10)


    #email_logo
    file_name="D:\FYP_project_temp\images\\emaillogo.png"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.5,rely=0.42)


    def on_select(event=None):
        password_textbox['show']="*"

# password_label=tk.Label(frame,text="Password",fg='white',bg='violet')
# password_label['font']=Fontlabel1
# password_label.place(relx=0.6,rely=0.5)

    #bg='#5B5E6F'
    password_textbox=EntryWithPlaceholder(textbox_password_frame,"Password")
    password_textbox.place(relx=0.1,rely=0.0,relwidth=formatting_constant_object.login_textbox_width,relheight=formatting_constant_object.login_textbox_height)
    password_textbox.bind("<Button-1>",on_select)
    #email_logo
    file_name="D:\FYP_project_temp\images\\passlogo.png"
    stdfilee=import_file_obj.Image.open(file_name)
    stdshow=import_file_obj.ImageTk.PhotoImage(stdfilee)
    imageshow=import_file_obj.tk.Label(image=stdshow)
    imageshow.image=stdshow
    imageshow.place(relx=0.5,rely=0.51)


    login_button=import_file_obj.tk.Button(frame,text="LOGIN",bg=formatting_constant_object.frame_bg,fg=formatting_constant_object.button_fg,borderwidth=2,command=loginn)
    login_button['font']=fontbutton
    login_button.place(relx=0.5,rely=0.7,relwidth=formatting_constant_object.button_width,relheight=formatting_constant_object.button_height)

    forget_password_label=import_file_obj.tk.Label(frame,text="Don't have a account?",fg=formatting_constant_object.main_frame_label_fg,bg=formatting_constant_object.main_frame_label_bg,)
    forget_password_label['font']=Fontlabel1
    forget_password_label.place(relx=0.75,rely=0.7)
    forget_password_label.bind("<Button-1>",std_register_call)

    root.mainloop()

Login()






