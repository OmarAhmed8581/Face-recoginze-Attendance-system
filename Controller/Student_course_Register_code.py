#<---------------------------------------------create an object of import file------------------->
import Import_file
import_file_obj=Import_file




#<-------------------------------------------------- Connection File --------------------------------------------------->


connection=import_file_obj.Global_Class.Global





def course_deleted(course,index,id,root):
    
    l=len(index)
    if l==0:
        import_file_obj.messagebox.showerror("error","Kindly select the course ID in Course Register")
    else :    
        a=""
        for j in index:
            a=course.get(j)
            split=a.split()
            course_id=split[0]
            course_name=split[1]
        

        connection.cursor.execute("select COURSE_ID from course where COURSE_NAME=?",course_name)
        Course_id=connection.cursor.fetchall()
        c_id=Course_id[0][0]
        
        connection.cursor.execute('delete from student_course_record where COURSE_ID_F=?',course_id)
        import_file_obj.messagebox.showinfo("Message","Course is Dropped")
        
        connection.cursor.execute("insert into student_Assigned_course(STUDENT_ID_F,COURSE_ID_F) values(?,?)",(id,c_id))
        connection.cursor.commit()



        path='D:\FYP_project_temp\course/'+course_id+" "+course_name+"_dataset"
        import_file_obj.os.chdir(path)
        i=str(id)
        for images_count in range(0,4): 
            image_path=i+" "+str(images_count)+'.jpg'
            import_file_obj.os.remove(image_path)
         
        root.destroy()
        import student_course_registeration
        student_course_registeration.Student_Course_Register(id)    




        
  
        

        

