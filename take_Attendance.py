
#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<------------------------------------------- create an object of formatting Constant--------> 


c=import_file_obj.formatting_constant.constant


#<-------------------------------------------------------------Connection File ---------------------------------------->

Conection=import_file_obj.Global_Class.Global




#<------------------------------------------------------------- Admin Menu form --------------------------------------->

global count
count =0

class Take_Attendance():

   

    def __init__(self,id):

       

        self.root=import_file_obj.tk.Tk()

        self.time = import_file_obj.tk.StringVar()
        self.time.set("00:00:00")
               
        self.id=id
        self.root.overrideredirect(True)
        self.root.geometry('%dx%d+%d+%d' % (c.form_width, c.form_height, c.form_x, c.form_y))
        self.root.focus_set()  

        self.canvas = import_file_obj.tk.Canvas(self.root, height=c.form_height, width=c.form_width,)
        self.canvas.pack()
        

        self.Fontlabel = import_file_obj.font.Font(family=c.family, size=13, )
        self.Fontlabel1 = import_file_obj.font.Font(family=c.family, size=13, )
        self.Fontlabel2 = import_file_obj.font.Font(family=c.family, size=c.label_font_heading_, weight=c.label_style )
        self.fontbutton=import_file_obj.font.Font(weight=c.button_style)
    #main frame
        self.frame=import_file_obj.tk.Frame(self.root,bg=c.frame_bg)
        self.frame.place(relx=0.0,rely=0.0,relwidth=c.frame_width,relheight=c.frame_height)

        self.headframe=import_file_obj.tk.Frame(self.frame,bg=c.headframe_bg)
        self.headframe.place(relx=0.0,rely=0.0,relwidth=c.headframe_width,relheight=c.headframe_height)
         
        


         
        self.leftframe=import_file_obj.tk.Frame(self.frame,bg=c.left_Frame_label_bg)
        self.leftframe.place(relx=0.0,rely=0.02,relwidth=c.leftframe_width,relheight=c.leftframe_height)



        #back 
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
        self.file_name="D:\FYP_project_temp\images\\teacher_logo.jpeg"
        self.stdfilee=import_file_obj.Image.open(self.file_name)
        self.stdshow=import_file_obj.ImageTk.PhotoImage(self.stdfilee)
        self.imageshow=import_file_obj.tk.Label(image=self.stdshow)
        self.imageshow.image=self.stdshow
        self.imageshow.place(relx=0.03,rely=0.08)



    

        self.leftframelabel1=import_file_obj.tk.Label(self.leftframe,text="Welcome to the",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
        self.leftframelabel1['font']=self.Fontlabel
        self.leftframelabel1.place(relx=0.3,rely=0.37)

        self.leftframelabel2=import_file_obj.tk.Label(self.leftframe,text="Student Attendance System",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
        self.leftframelabel2['font']=self.Fontlabel
        self.leftframelabel2.place(relx=0.3,rely=0.43)

        self.leftframelabel3=import_file_obj.tk.Label(self.leftframe,text="Faculty Panel",fg=c.left_Frame_label_fg,bg=c.left_Frame_label_bg)
        self.leftframelabel3['font']=self.Fontlabel
        self.leftframelabel3.place(relx=0.3,rely=0.5)

        self.mainframelabel=import_file_obj.tk.Label(self.frame,text='Faculty Panel',fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.mainframelabel['font']=self.Fontlabel2
        self.mainframelabel.place(relx=0.6,rely=0.1)


        self.cblable=import_file_obj.tk.Label(self.frame,text="Select your course from the list below",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.cblable['font']=self.Fontlabel1
        self.cblable.place(relx=0.51,rely=0.2)
        self.combox=import_file_obj.ttk.Combobox(self.frame,command=self.selectcourse())
        self.combox.place(relx=0.51,rely=0.26,relwidth=c.combox_width,relheight=c.combox_height)
        self.combox['value']=self.data
        self.combox.bind("<<ComboboxSelected>>",self.show_id)


        self.timmer_lb = import_file_obj.tk.Label(self.frame,text="Time ",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.timmer_lb['font']=self.Fontlabel1
        self.timmer_lb.place(relx=0.73,rely=0.6)


        self.timmer = import_file_obj.tk.Label(self.frame,textvariable=self.time,fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.timmer['font']=self.Fontlabel1
        self.timmer.place(relx=0.81,rely=0.6)





        self.course_id_lbl=import_file_obj.tk.Label(self.frame,text="Select your course ID from the list below",fg=c.main_frame_label_fg,bg=c.main_frame_label_bg)
        self.course_id_lbl['font']=self.Fontlabel1
        self.course_id_lbl.place(relx=0.51,rely=0.35)
        self.course_cb_id=import_file_obj.ttk.Combobox(self.frame,)
        # self.course_cb_id['value']=self.show_data
        self.course_cb_id.place(relx=0.51,rely=0.4,relwidth=c.combox_width,relheight=c.combox_height)


        
        

        self.take_attendance_btn=import_file_obj.tk.Button(self.frame,text="Take Attendance",bg=c.leftframe_bg,fg=c.left_Frame_label_fg,font=c.family,borderwidth=2,command=self.call_take_attendance)
        self.take_attendance_btn.place(relx=0.55,rely=0.48,relwidth=c.user_menu_button_width,relheight=c.user_button_height)
         
        



        self.root.mainloop()

    def Absent_call(self):

        
       

        Conection.cursor.execute("Select STUDENT_ID_F from student_course_record where COURSE_ID_F=?",(self.course_cb_id.get()))
        student_id=Conection.cursor.fetchall()

        length=len(student_id)
        data=self.get_date()
        time=self.get_CurrentTime()

        for index in range(0,length):
            Conection.cursor.execute("select * from student_attendance where TEACHER_ID_F=? and STUDENT_ID_F=? and COURSE_ID_F=?",(self.id,student_id[index][0],self.course_cb_id.get()))
            count=Conection.cursor.fetchall()
            if(len(count) == 0):
                Conection.cursor.execute("insert into student_attendance(TEACHER_ID_F,STUDENT_ID_F,COURSE_ID_F,DATE,TIME,STATUS) values(?,?,?,?,?,?)",(self.id,student_id[index][0],self.course_cb_id.get(),data,time,'ABSENT'))

        Conection.cursor.commit()
        self.drop_warning_msg()

    def call_take_attendance(self):
        Conection.cursor.execute("Select count(*) from student_course_record where COURSE_ID_F=?",(self.course_cb_id.get()))
        count=Conection.cursor.fetchall()
        if count[0][0]!=0:
            self.take_attendance()
        else:
            import_file_obj.messagebox.showerror("error","None of this student enroll is this course") 







    def drop_warning_msg(self):

        

        Conection.cursor.execute("Select STUDENT_ID_F from student_course_record where COURSE_ID_F=?",(self.course_cb_id.get()))
        student_id=Conection.cursor.fetchall()

        # 
        # messagebox.showinfo(student_email)

        for i in range(0,len(student_id)):
        
            Conection.cursor.execute("Select count(*) from student_attendance where COURSE_ID_F=? and STATUS='ABSENT' and STUDENT_ID_F=? ",(self.course_cb_id.get(),student_id[i][0]))
            Absent=Conection.cursor.fetchall()

            if(Absent[0][0] == 4):

                Conection.cursor.execute("Select STD_EMAIL from student_registeration_record where STUDENT_ID_F=?",(student_id[i][0]))
                student_email=Conection.cursor.fetchall()
                # import smtp
                warning_msg="Your course will be drop after 2 absents!"  #message you want to send
                mail=import_file_obj.smtplib.SMTP('smtp.gmail.com',587) 
                mail.ehlo()  
                mail.starttls()  
                mail.login('shumailaashiq10@gmail.com','FYP_2020')
                mail.sendmail('shumailaashiq10@gmail.com',student_email[0][0],warning_msg)
                mail.close()
                # smtp.WARNING(student_email)
                # messagebox.showerror("warning","warning msg")

            elif(Absent[0][0] == 6):
                # import smtp
                drop_msg="Your course has been dropped!"  #message you want to send
                mail=import_file_obj.smtplib.SMTP('smtp.gmail.com',587)  
                mail.ehlo()  
                mail.starttls() 
                mail.login('shumailaashiq10@gmail.com','FYP_2020')
                mail.sendmail('shumailaashiq10@gmail.com',student_email[0][0],drop_msg)
                mail.close()


                #  Delete from student course record
                Conection.cursor.execute("delete COURSE_ID_F from student_course_record where STUDENT_ID_F=? AND COURSE_ID_F=?",(student_id[i][0],self.course_cb_id.get()))


                # Delete from teacher attendance

                


                Conection.cursor.commit()


               


                
               
                
                

                path='D:\FYP_project_temp\course/'+self.course_cb_id.get()+" "+self.combox.get()+'_dataset'
                import_file_obj.os.chdir(path)
                i=str(self.id)
                for images_count in range(0,4): 
                    image_path=i+" "+str(images_count)+'.jpg'
                    import_file_obj.os.remove(image_path)

                
                        # smtp.DROPPED(student_email)
                        # messagebox.showerror("warning","Drop msg")

    def on_click(self,event=None):
        self.root.destroy()
    

    def menu_back(self,event=None):
        self.root.destroy()
        import Teacher_menu
        Teacher_menu.faculty_menu(self.id)

    # def start(self):
    #     global count
    #     count=0
    #     self.start_timer()

    # def start_timer(self):
    #     global count
    #     self.timer()

    # def timer(self):
    #     global count
    #     if(count==0):
    #         self.d = str(self.time.get())
    #         h,m,s = map(int,self.d.split(":"))
            
    #         h = int(h)
    #         m=int(m)
    #         s= int(s)
    #         if(s<59):
    #             s+=1
    #         elif(s==59):
    #             s=0
    #             if(m<59):
    #                 m+=1
    #             elif(m==59):
    #                 h+=1
    #         if(h<10):
    #             h = str(0)+str(h)
    #         else:
    #             h= str(h)
    #         if(m<10):
    #             m = str(0)+str(m)
    #         else:
    #             m = str(m)
    #         if(s<10):
    #             s=str(0)+str(s)
    #         else:
    #             s=str(s)
    #         self.d=h+":"+m+":"+s
            
            
    #         self.t.set(self.d)
    #         if(count==0):
    #             self.root.after(930,self.start_timer)
                

    def show_id(self,event=None):
        self.show_data=[]
        self.id_show=[] 
        selectt_course=self.combox.get()


        Conection.cursor.execute('select COURSE_ID from course where COURSE_NAME=?',(selectt_course))
        RESULT_COURSE=Conection.cursor.fetchall()

        Conection.cursor.execute('select OFFER_COURSE_ID from course_offer where COURSE_ID_F=?',(RESULT_COURSE[0][0]))
        Result_Course_id=Conection.cursor.fetchall()

        length=len(Result_Course_id)

        for index in range(0,length):
            self.show_data.append(Result_Course_id[index][0])

        for j in range(0,len(self.show_data)):

            Conection.cursor.execute('select COURSE_ID_F from faculty_course_assigned where FACULTY_ID =? and COURSE_ID_F=?',(self.id,self.show_data[j]))
            Course_ID=Conection.cursor.fetchall()

            if(len(Course_ID)!=0):
                self.id_show.append(Course_ID[0][0])
        # for x in range(0,len(show_data)):
        #     Conection.cursor.execute("select ")

        self.course_cb_id['values']=self.id_show
        self.course_cb_id.current(0)


    def selectcourse(self):
        self.data=[]
        self.course_id=[]
        Conection.cursor.execute("select COURSE_ID_F from faculty_course_assigned where FACULTY_ID=?",(self.id))
        result_id=Conection.cursor.fetchall()
        length=len(result_id)

        for index in range(0,length):
           self.course_id.append(result_id[index][0])


        for course in range(0,len(self.course_id)):
            Conection.cursor.execute("select COURSE_ID_F from course_offer where OFFER_COURSE_ID=?",(self.course_id[course]))
            result_name=Conection.cursor.fetchall()   


            if len(result_name) != 0:
                Conection.cursor.execute("select COURSE_NAME from course where COURSE_ID = ?",(result_name[0][0]))
                result=Conection.cursor.fetchall()
                self.data.append(result[0][0])
        self.data=list(dict.fromkeys(self.data))    

            
        

        
    def get_date(self):
        today=import_file_obj.date.today()
        date = today.strftime("%B %d, %Y") 
        return date

    def get_CurrentTime(self):
      #  now = datetime.now()
        currentDT = import_file_obj.datetime.datetime.now()
        time=currentDT.strftime("%I:%M:%S %p")
        return time


    def tranner(self):

        select_course=self.combox.get()
        select_course_id=self.course_cb_id.get()
      
        
        Conection.cursor.execute("select COURSE_ID from course where COURSE_NAME=?",(select_course))
        course_id=Conection.cursor.fetchall()
        c_id=course_id[0][0]




            
        
        dataset_path="D:\FYP_project_temp\course/"+select_course_id+" "+select_course+"_dataset"   # where the images is store

        train_images = import_file_obj.cvutils.imlist(dataset_path)   # list the dataset images
        #   cvutils it is a namespace /packages and imlist is a method




        train_dic = {}     # this dic contain id of each images e.g 'Dataset\\1.jpg': 1 
       

        dataset_images_train = []  
        dataset_images_name = []

        train_index=0

        # --------------------------->





        for train_image in train_images:
           
            # Read the image
            img = import_file_obj.cv2.imread(train_image)



            # Convert  each images to grayscale 
            gray_image = import_file_obj.cv2.cvtColor(img, import_file_obj.cv2.COLOR_BGR2GRAY)

            radius = 1   # 3 by 3 matrix 


            # Number of points to be considered as neighbourers             
            
            neighbour = 8                        # 8 point consider

            # Uniform LBP is used
            lbp = import_file_obj.local_binary_pattern(gray_image,neighbour, radius, method='uniform')
                
            # import_file_obj.cv2.imshow("LBP frame",lbp)

            # Hi=∑x,yI{fl(x,y)=i},i=0,…,n−1,  (histogrm=sum(lbprryresult==i)) where i is the loop histogram Formular

            # histogram formular 256 different pixel label

            # Calculate the histogram

            train_images_histogram = import_file_obj.itemfreq(lbp.ravel())
            # hist = zeros(1,256)

            Calculating_histogram=[]
            for i in range(1,11):
                Calculating_histogram.append(sum(lbp[:]==(i-1))) 

            # print(sum(hist[0]))
            # print(sum(hist[1]))
            # print(sum(hist[2]))
            # print(sum(hist[3]))
            # print(sum(hist[4]))
            # print(sum(hist[5]))
            # print(sum(hist[6]))
            # print(sum(hist[7]))
            # print(sum(hist[8]))
            # print(sum(hist[9]))

            histogram_values=[]
            for i in range(0,10):
                histogram_values.append(sum(Calculating_histogram[i]))
        




    #itemfreq calculate histogram of lbp
            # print(train_images_histogram[:,1])
                
            # Normalize the histogram
            # histogram_value = train_images_histogram[:, 1]/sum(train_images_histogram[:, 1])
            # h[:]/sum(h[:]) 
            Normalize_value_train_images=histogram_values[:]/sum(histogram_values[:])

            # print("hist value")
            # print(histogram_value)

            # print("Noam")
            # print(Normalize_value)
            # print(sum(Normalize_value[0]))
    #--------------------------rough work of normlize value----------------------------------------------
            # 3,4,6
            # 3,4,6/13       3/13,4/13,6/13

    #-----------------------------------------------------------------------------------        
            # Append image path in dataset_name
            dataset_images_name.append(train_images[train_index])
            train_index +=1




            # Append Normalize histogram to dataset_train
            dataset_images_train.append(Normalize_value_train_images)


       
      
        #<-----------------------------------------------------------------------------------------
        #Reconginze of test imge
        test_path="D:\FYP_project_temp\course/test"   # where the images is store

        test_images = import_file_obj.cvutils.imlist(test_path)   # list the test images

        for test_image in test_images:


            # Read the image
            images = import_file_obj.cv2.imread(test_image)
            
            # Convert to grayscale of test images
            GrayScaleImages = import_file_obj.cv2.cvtColor(images, import_file_obj.cv2.COLOR_BGR2GRAY)

#now applying lbp on test image
            radius = 1
            # Number of points to be considered as neighbourers 
            neighbour = 8 * radius


            # Uniform LBP is used
            lbp = import_file_obj.local_binary_pattern(GrayScaleImages, neighbour, radius, method='uniform')


            # Calculate the histogram
            # test_images_histogram = import_file_obj.itemfreq(lbp.ravel())


            Calculating_histogram=[]
            for i in range(1,11):
                Calculating_histogram.append(sum(lbp[:]==(i-1))) 

            # print(sum(hist[0]))
            # print(sum(hist[1]))
            # print(sum(hist[2]))
            # print(sum(hist[3]))
            # print(sum(hist[4]))
            # print(sum(hist[5]))
            # print(sum(hist[6]))
            # print(sum(hist[7]))
            # print(sum(hist[8]))
            # print(sum(hist[9]))

            histogram_values=[]
            for i in range(0,10):
                histogram_values.append(sum(Calculating_histogram[i]))
        

            # sum=65,025

            # Normalize the histogram
            # hist = test_images_histogram[:, 1]/sum(test_images_histogram[:, 1])

             # h[:]/sum(h[:]) index0 =1985/65025=0.03052672
            Normalize_value_test_image=histogram_values[:]/sum(histogram_values[:])

          
            # d(H1,H2)=∑I(H1(I)−H2(I))2H1(I)
            
            results = []
            number=[]
            #Comparision of two histograms b/w train and test image
            for index in range(0,len(dataset_images_train)):
                Comparision_Histogram = import_file_obj.cv2.compareHist(import_file_obj.np.array(dataset_images_train[index] , import_file_obj.np.float32) , import_file_obj.np.array(Normalize_value_test_image , import_file_obj.np.float32) , import_file_obj.cv2.HISTCMP_CHISQR)
                results.append((dataset_images_name[index], round(Comparision_Histogram, 3)))

            # results = sorted(results, key=lambda Comparision_Histogram:Comparision_Histogram[0])    


            # compare value is store in number

            for compare in range(0,len(results)):
                number.append(results[compare][1])


            number=sorted(number)    
            images_sorted_value=""


            for i in range(0,len(results)):
                if(results[i][1] == number[0]):
                    images_sorted_value=results[i][0]
            print(images_sorted_value)
            print(results) 

            if number[0]<0.02:       # stop unknown person
                DATE=self.get_date()
                TIME=self.get_CurrentTime()


                # get id from images path

                remove_double_dash=images_sorted_value.split("\\")
                STD_ID=remove_double_dash[3].split()
                


                # get course id from images path

                # print(id[0])
                # if the student attendance is not taken
                Conection.cursor.execute("select STATUS from student_attendance where STUDENT_ID_F=? and COURSE_ID_F=? and DATE=?",(STD_ID[0],self.course_cb_id.get(),DATE))
                results=Conection.cursor.fetchall()
                length=len(results)
                if(length==0):
                    Conection.cursor.execute("insert into student_attendance(TEACHER_ID_F,STUDENT_ID_F,COURSE_ID_F,DATE,TIME,STATUS) values(?,?,?,?,?,?)",(self.id,STD_ID[0],self.course_cb_id.get(),DATE,TIME,"PRESENT"))
                # else:
                #     if(results[0][0] != "PRESENT"):
                #         Conection.cursor.execute("update student_attendance set STATUS='PRESENT' where STATUS=? and STUDENT_ID_F=?",("ABSENT",STD_ID[0]))





                Conection.cursor.commit()







    


    
    #Detection is done here.

    def take_attendance(self):

        image_width=182
        image_height=182


        if self.combox.get() != "" and self.course_cb_id.get() != "":

            face_cascade=import_file_obj.cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
            cam=import_file_obj.cv2.VideoCapture(0)
            sample_images_count=0
            id=1
            while True:
                ret ,img = cam.read()
                gray_scale=import_file_obj.cv2.cvtColor(img,import_file_obj.cv2.COLOR_BGR2GRAY)

                faces=face_cascade.detectMultiScale(gray_scale,1.3,5)

                for (x,y,w,h) in faces:

                    crop=gray_scale[y:y+h,x:x+w]
                    import_file_obj.cv2.rectangle(gray_scale,(x,y),(x+w,y+h),(255,0,0),2)
                    resizing_image=import_file_obj.cv2.resize(crop,(image_width,image_height))
                    import_file_obj.cv2.imwrite('D:\FYP_project_temp\course/test/'+str(id)+".jpg",crop)
                    self.tranner()
                    sample_images_count += 1
                    import_file_obj.cv2.imshow("face detect",gray_scale)
                    import_file_obj.cv2.waitKey(1)
                if(sample_images_count>=4):
                    self.Absent_call()
                    break   

            cam.release()
            import_file_obj.cv2.destroyAllWindows()  
        else:
            import_file_obj.messagebox.showerror ("Error","Kindly select course Name and course id")     

 #left frame
   

