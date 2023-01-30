#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file



#<------------------------------------------- create an object of formatting Constant--------> 



c=import_file_obj.formatting_constant.constant



#<------------------------------------------------------------- Connection file --------------------------------------->

Conection=import_file_obj.Global_Class.Global





#<--------------------------------------------------------------- Student Register Form ------------------------------->


class Student_Register():

    def __init__(self):
        self.root=import_file_obj.tk.Tk()
        self.root.title("Admin form")


        self.phone_flat=True
        self.pass_flat=True
        self.email_flat=True
        self.nic_flat=True


        self.root.overrideredirect(True)
        self.root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
        self.root.focus_set() 

        self.canvas = import_file_obj.tk.Canvas(self.root, height=c.form_height, width=c.form_width,)
        self.canvas.pack()


        self.Fontlabel = import_file_obj.font.Font(family=c.family, size=13, )
        self.Fontlabel1 = import_file_obj.font.Font(family=c.family, font=8, )



        
        self.frame=import_file_obj.tk.Frame(self.root,bg=c.frame_bg)
        self.frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width_std_reg,relheight=c.frame_height)

        self.headframe=import_file_obj.tk.Frame(self.frame,bg='white')
        self.headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)




        self.leftframe=import_file_obj.tk.Frame(self.frame,bg=c.left_Frame_label_bg)
        self.leftframe.place(relx=0.0,rely=0.02,relwidth=c.register_leftframe_width,relheight=c.register_leftframe_height)
        
       
    #cross symbol
        self.file_name="D:\FYP_project_temp\images\\crossicon.png"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.on_click)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.98,rely=0.0)

        
    #back 
        self.file_name="D:\FYP_project_temp\images\\back.png"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.bind('<Button-1>', self.login_back)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.02,rely=0.03)

        self.file_name="D:\FYP_project_temp\images\\reg_logo.jpeg"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.03,rely=0.09)

        self.leftframelabel1=import_file_obj.tk.Label(self.leftframe,text="Make an account",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
        self.leftframelabel1['font']=self.Fontlabel
        self.leftframelabel1.place(relx=0.3,rely=0.34)

        self.leftframelabel2=import_file_obj.tk.Label(self.leftframe,text="to connect with us",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
        self.leftframelabel2['font']=self.Fontlabel
        self.leftframelabel2.place(relx=0.3,rely=0.4)


        


        self.mainframelabel=import_file_obj.tk.Label(self.frame,text='Create your account here',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.mainframelabel['font']=self.Fontlabel
        self.mainframelabel.place(relx=0.5,rely=0.1)


        self.string=import_file_obj.tk.StringVar()
        self.name_lbl=import_file_obj.tk.Label(self.frame,text="Name:",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.name_lbl.place(relx=0.5,rely=0.22)
        self.name_txt=import_file_obj.ttk.Entry(self.frame,textvariable=self.string,text="")
        self.name_txt.place(relx=0.68,rely=0.22,relwidth=c.register_textbox_width)

        self.fathername_lbl=import_file_obj.tk.Label(self.frame,text="Father Name:",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.fathername_lbl.place(relx=0.5,rely=0.30)
        self.fathername_txt=import_file_obj.ttk.Entry(self.frame,textvariable=self.string,text="")
        self.fathername_txt.place(relx=0.68,rely=0.30,relwidth=c.register_textbox_width)
        self.fathername_txt.bind("<Button-1>",self.call_father)


        self.email_validation=import_file_obj.tk.Label(self.frame,text="Invalid Email:",fg="red",bg=c.main_frame_label_bg)
        self.email_validation.place(relx=0.68,rely=0.35)

        self.email_lbl=import_file_obj.tk.Label(self.frame,text="Email Address:",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.email_lbl.place(relx=0.5,rely=0.38)
        self.email_txt=import_file_obj.ttk.Entry(self.frame,text="",)
        self.email_txt.place(relx=0.68,rely=0.38,relwidth=c.register_textbox_width)
        self.email_txt.bind("<Button-1>",self.call_email)


        self.password_lbl=import_file_obj.tk.Label(self.frame,text="Password:",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.password_lbl.place(relx=0.5,rely=0.46)
        self.password_txt=import_file_obj.ttk.Entry(self.frame,textvariable=self.string,text="",show='*')
        self.password_txt.place(relx=0.68,rely=0.46,relwidth=c.register_textbox_width)
        self.password_txt.bind("<Button-1>",self.call_pass)




        
        self.pass_validation=import_file_obj.tk.Label(self.frame,text="Password didn't match:",fg="red",bg=c.main_frame_label_bg)
        self.pass_validation.place(relx=0.68,rely=0.51)

        self.confirmpassword_lbl=import_file_obj.tk.Label(self.frame,text="Confirm Password:",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.confirmpassword_lbl.place(relx=0.5,rely=0.54)
        self.confirmpassword_txt=import_file_obj.ttk.Entry(self.frame,textvariable=self.string,text="",show='*')
        self.confirmpassword_txt.place(relx=0.68,rely=0.54,relwidth=c.register_textbox_width)
        self.confirmpassword_txt.bind("<Button-1>",self.call_confirm_pass)

        self.phone_validation=import_file_obj.tk.Label(self.frame,text="Invalid phone number:",fg="red",bg=c.main_frame_label_bg)
        self.phone_validation.place(relx=0.68,rely=0.58)

        self.phone_lbl = import_file_obj.tk.Label(self.frame, text="Phone Number:", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
        self.phone_lbl.place(relx=0.5,rely=0.61)
        self.phone_txt = import_file_obj.ttk.Entry(self.frame, textvariable=self.string, text="")
        self.phone_txt.place(relx=0.68,rely=0.61,relwidth=c.register_textbox_width)
        self.phone_txt.bind("<Button-1>",self.call_phone)

        self.program_lbl = import_file_obj.tk.Label(self.frame, text="Program:", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
        self.program_lbl.place(relx=0.5,rely=0.68)
        self.program_txt = import_file_obj.ttk.Entry(self.frame, textvariable=self.string, text="")
        self.program_txt.place(relx=0.68,rely=0.68,relwidth=c.register_textbox_width)
     
       



        self.nic_validation=import_file_obj.tk.Label(self.frame,text="Invalid Nic number:",fg="red",bg=c.main_frame_label_bg)
        self.nic_validation.place(relx=0.68,rely=0.73)


        self.nic_lbl = import_file_obj.tk.Label(self.frame, text="NIC:", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
        self.nic_lbl.place(relx=0.5,rely=0.76)
        self.nic_txt = import_file_obj.ttk.Entry(self.frame, textvariable=self.string, text="")
        self.nic_txt.place(relx=0.68,rely=0.76,relwidth=c.register_textbox_width)
        self.nic_txt.bind("<Button-1>",self.call_nic)

        self.city_lbl = import_file_obj.tk.Label(self.frame, text="City:", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
        self.city_lbl.place(relx=0.5,rely=0.84)
        self.city_txt = import_file_obj.ttk.Entry(self.frame, textvariable=self.string, text="")
        self.city_txt.place(relx=0.68,rely=0.84,relwidth=c.register_textbox_width)
        self.city_txt.bind("<Button-1>",self.call_city)
        

        self.address_lbl=import_file_obj.tk.Label(self.frame, text="Address:", fg=c.main_frame_label_fg,bg=c.main_frame_label_bg )
        self.address_lbl.place(relx=0.5,rely=0.90)
        self.address_txt = import_file_obj.ttk.Entry(self.frame, textvariable=self.string, text="")
        self.address_txt.place(relx=0.68,rely=0.90,relwidth=c.register_textbox_width)
        self.address_txt.bind("<Button-1>",self.call_address)


        self.photo_lbl=import_file_obj.tk.Label(self.frame,text="Add your photo:",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.photo_lbl.place(relx=0.5,rely=0.94)
        self.browse_photo=import_file_obj.tk.Button(self.frame,text="Take your photo",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg,command=self.std_photo)
        self.browse_photo['font']=self.Fontlabel1
        self.browse_photo.place(relx=0.68,rely=0.94,relwidth=c.register_textbox_width)
        


        self.hide()


        






        self.root.mainloop()


    def call_email(self,event=None):
        self.email_txt["textvariable"]=self.string
        self.email_pattern='(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False    
        
        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True


        if self.phone_txt.get() != ""  and not import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place(relx=0.68,rely=0.58)
            self.phone_flat=False
        if self.phone_txt.get() != ""  and  import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place_forget()
            self.phone_flat=True  





    def call_pass(self,event=None):
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False
        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True
        
        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True


        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False   

            


    def call_confirm_pass(self,event=None):
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False
        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True

        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True


        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False  

    def call_city(self,event=None):

        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False

        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True

        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True


        if self.phone_txt.get() != ""  and not import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place(relx=0.68,rely=0.58)
            self.phone_flat=False
        if self.phone_txt.get() != ""  and  import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place_forget()
            self.phone_flat=True    
    
                
            

        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False  

    def call_nic(self,event=None):
        self.NIC_no_patthern='\\d{11}'
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False

        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True

        if self.phone_txt.get() != ""  and not import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place(relx=0.68,rely=0.58)
            self.phone_flat=False

        if self.phone_txt.get() != ""  and  import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place_forget()   
            self.phone_flat=True   
    

        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False  


    def call_name(self,event=None):
        
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False
        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True


        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True


        if self.phone_txt.get() != ""  and not import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place(relx=0.68,rely=0.58)
            self.phone_flat=False
        if self.phone_txt.get() != ""  and  import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place_forget()
            self.phone_flat=True  

                
        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False  

    def call_phone(self,event=None):
        self.phone_no_pattern="\\d{4}[-.\s]?\\d{7}"
          
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False
        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True

            
        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True

        
        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False 


    def call_address(self,event=None):
                
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False
        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True


        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True


        if self.phone_txt.get() != ""  and not import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place(relx=0.68,rely=0.58)
            self.phone_flat=False
        if self.phone_txt.get() != ""  and  import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place_forget()
            self.phone_flat=True      

                
        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "":
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False   

    def call_father(self,event):
                
        if self.email_txt.get() !=  "" and not import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place(relx=0.68,rely=0.35)
            self.email_flat=False
        if self.email_txt.get() !=  "" and import_file_obj.re.search(self.email_pattern,self.email_txt.get()):
            self.email_validation.place_forget()
            self.email_flat=True


        if self.nic_txt.get() != "" and not import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place(relx=0.68,rely=0.73)
            self.nic_flat=False
        if self.nic_txt.get() != "" and  import_file_obj.re.search(self.NIC_no_patthern,self.nic_txt.get()):
            self.nic_validation.place_forget()
            self.nic_flat=True

        if self.phone_txt.get() != ""  and not import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place(relx=0.68,rely=0.58)
            self.phone_flat=False
        if self.phone_txt.get() != ""  and  import_file_obj.re.search(self.phone_no_pattern,self.phone_txt.get()):
            self.phone_validation.place_forget()
            self.phone_flat=True      

                
        if self.password_txt.get() != "" and self.confirmpassword_txt.get() != "" :
            if self.password_txt.get() == self.confirmpassword_txt.get():
                self.pass_validation.place_forget()
                self.pass_flat=True
            else:
                self.pass_validation.place(relx=0.68,rely=0.51)
                self.pass_flat=False                        



    def hide(self):

        # if invalid input is enter
        # ----------------------------


        self.email_validation.place_forget() 
        self.phone_validation.place_forget()
        self.pass_validation.place_forget()
        self.nic_validation.place_forget()   
    def error(self):
        import_file_obj.messagebox.showerror('Error','All fields are required')
#----------------------------------------------------------------------
    def error_Email(self):
        email_lbl_error=import_file_obj.tk.Label(self.frame,text="Email Address is not valid",fg=c.error_label_fg,bg=c.main_frame_label_bg)
        email_lbl_error.place(relx=0.5,rely=0.36)

    def std_register(self):
       
        #conn = pyodbc.connect('Driver={SQL Server};''Server=SHUMAILA\SHUM;''Database=FYP;''Trusted_Connection=yes;')
        #cursor=conn.cursor()

        
        # email_pattern='(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        # phone_no_pattern="\\d{4}[-.\s]?\\d{7}"
        # NIC_no_patthern='\\d{11}'

        if self.nic_flat == True and self.phone_flat ==True and self.email_flat==True and self.pass_flat == True:

            self.email_validation.place_forget()
            self.phone_validation.place_forget()
            self.phone_validation.place_forget()
            self.pass_validation.place_forget()

            std_name=self.name_txt.get()
            std_email=self.email_txt.get()
            std_fathername=self.fathername_txt.get()
            std_password=self.password_txt.get()
            std_confirmpassword=self.confirmpassword_txt.get()
            std_phoneno=self.phone_txt.get()
            std_nic=self.nic_txt.get()
            std_program=self.program_txt.get()
            std_address=self.address_txt.get()
            std_city=self.city_txt.get()


            from Controller import Student_Register_code
            Student_Register_code.Register(std_name,std_fathername,std_email,std_password,std_confirmpassword,std_phoneno,std_nic,std_city,std_address,std_program,self.root)
        
        else:
            import_file_obj.messagebox.showerror("please","Fixed the Invalid input")

        # if re.search(email_pattern,self.email_txt.get()):
        #     self.email_validation.place_forget()
        # if(re.search(phone_no_pattern,self.phone_txt.get())):
        #     self.phone_validation.place_forget()
        # if(re.search(NIC_no_patthern,self.nic_txt.get())):
        #     self.phone_validation.place_forget()        




        # if self.email_txt.get !="" and not re.search(email_pattern,self.email_txt.get()):
        #     self.email_validation.place(relx=0.68,rely=0.35)
        # if self.phone_txt.get() !="" and not re.search(phone_no_pattern,self.phone_txt.get()):
        #     self.phone_validation.place(relx=0.68,rely=0.58)  
        # if self.nic_txt.get() !="" and not re.search(NIC_no_patthern,self.nic_txt.get()):
        #     self.nic_validation.place(relx=0.68,rely=0.73)      


        
      
                    
    def on_click(self,event=None):
        self.root.destroy()

    def login_back(self,event=None):
        self.root.destroy()
        import login
        login.Login()    
        
#----------------------------------------------------------------------

    def std_photo(self):
        self.std_register()



#----------------------------------------------------------------------

   

