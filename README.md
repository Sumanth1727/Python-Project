
                                                           Project Shiksha
                                                           
                                                           
                             
 Prerequisites for project: mysql sever and working python compiler installed on the computer
project description:
 it is login system where teacher students and admins login to their respective portals and do their operations
    
  it iconsists of 3 portals and 4 tables

  tables used in this project are student table,studentmarks table,admins table,teacher table

  cotents of teacher table are:

    teacherid (int)  auto_increment primary key,
    pass (varchar) not null,
    department (varchar) not null,
   salary (int) not null,
   experience(int) not null,
   teachername (varchar) not null,

cotents of student table are:
   studentid (int)  auto_increment primary key,
    pass (varchar) not null,
   firstname (varchar) not null,
   lastname (varchar) not null,
   fullname (varchar) not null,  #full name should be a concatination of first name and last name
   consellorid (int) not null ,     #consellor id is mapped to tecaher id of teacher table via foriegn key
                                             FOREIGN KEY (consellorid) REFERENCES teacher(teacherid)

contents of studentmarks table are:
   studentid (int) primary key, #studentid of studantmarks table is linked to studentid of student table
   ia1marks (int) not null,
    ia2marks (int) not null,
    famarks (int) not null,
    average (float) not null,  # average should be the average of(average of ia1 and ia2 marks) and fa marks
                                         #FOREIGN KEY (studentid) REFERENCES student info(studentid)

contents of admins table are:
  adminsid (varchar) primary key,
  pass (varchar) NOT NULL,
  

It consists of 3 portals 
  1)admin portal
  2)teacher's portal
  3)student portal

admin:
  admin can do the following operations:

          1.create new teacher
          2.update teacher salary(based on the condition.i.e avg marks of all student assigned to teacher as councellor should be graether than 50) 
         3.view student marks
         4.update student marks
         5.add new student
        6.update teacherinfo
        7.update password

teacher can do the following opeartions:
           1.add new student
          2.enter student marks # teacher can enter or update marks of his councelling students only
         3.update student marks
         4.viewteacherinfo
         5.update password 
student can do the following operations:
         1.view student info
        2.update student info
       3.view student marks
       4.view your consellor info
       5.update password
        
