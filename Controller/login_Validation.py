#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<-------------------------------------------create an object of Connection File --------------------------------------------------->


connection_obj=import_file_obj.Global_Class.Global









def Login(email_address,passwordd,user,root):
    std_password_hash=import_file_obj.hashlib.md5(passwordd.encode('utf-8'))
    std_pass_hexa=std_password_hash.hexdigest()

    # salt=os.urandom(32)
    # key=hashlib.pbkdf2_hmac('sha256',passwordd.encode('utf-8'),salt,100000)
    # storage=salt + key

    varselect=[]
    varselect.append(email_address)
    varselect.append(passwordd)
    
    
    if email_address=="" or passwordd=="" or user=="":
        import_file_obj.messagebox.showinfo("Message","Please enter the required Information")
    else:
        if user=='Student':
            connection_obj.cursor.execute('select STD_ID,STD_EMAIL,STD_PASSWORD from student_registeration_record where STD_EMAIL=? AND  STD_PASSWORD=?',(email_address,std_pass_hexa))
            result=connection_obj.cursor.fetchall()
            if len(result) != 0:
                id=result[0][0]
                email=result[0][1]
                Password=result[0][2]
               
                import success_login
                success_login.msgbox("You're successfully login!",id,root)
                # root.destroy()

               
                
            else:
                import_file_obj.messagebox.showinfo("Message","Invalid username or password")      
        
        elif user=='Faculty':

            connection_obj.cursor.execute('select FACULTY_ID,FACULTY_EMAIL,FACULTY_PASSWORD from faculty_registeration_record where FACULTY_EMAIL=? AND FACULTY_PASSWORD=?',(email_address,std_pass_hexa))
            result=connection_obj.cursor.fetchall()
            if result is not None:

                #messagebox.showinfo("Message","Successfully login")
                root.destroy()
                import Teacher_menu
                Teacher_menu.faculty_menu(result[0][0])
            else:
                import_file_obj.messagebox.showinfo("Message","Invalid username or password")
        elif user=='Admin':
            if email_address=='Admin' and passwordd=='Admin':
                root.destroy()
                import Admin_Menu
                Admin_Menu.admin_menu()
            else:
                import_file_obj.messagebox.showinfo("Message","Invalid username or password")

                
    