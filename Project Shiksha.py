import mysql.connector
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root", # enter your username of your mysql server
  passwd="Sumanth@89",# enter your password of your mysql server
)
mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE DATABASE newdatabase;")
  print("database successfully created")

except Exception as e:
    print(e)

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Sumanth@89",
    database="newdatabase"
  )
  mycursor = mydb.cursor()
  print("connection successfully established")

except Exception as e:
    print(e)



try:
  # creating teacher table to store teacher information
  mycursor.execute("Create table teacher(teacherid int  AUTO_INCREMENT PRIMARY KEY, pass varchar(100) not null,department varchar(255) NOT NULL,salary int NOT NULL,experience int NOT NULL,teachername varchar(255) NOT NULL)")
  print("teacher table successfully created")
except Exception as e:
  print(e)



try:
  # creating student table to store student information
  mycursor.execute(
      "Create table student(studentid int  AUTO_INCREMENT,pass varchar(100) not null,firstname varchar(255) NOT NULL,lastname varchar(255) NOT NULL,fullname varchar(500) not null,consellorid int not null ,PRIMARY KEY(StudentID),FOREIGN KEY (consellorid) REFERENCES teacher(teacherid))")
  print("student table successfully created")
except Exception as e:
  print(e)



try:
  # creating studentmarks table to store student marks
  mycursor.execute(
      "Create table studentmarks(studentid int ,ia1marks int NOT NULL,ia2marks int NOT NULL,famarks int NOT NULL,average float not null,PRIMARY KEY(studentid),FOREIGN KEY (studentid) REFERENCES student(studentid));")
  print("studentmarks table successfully created")
except Exception as e:
  print(e)



try:
  # creating admins table to store admins information
  mycursor.execute(
      "Create table admins(adminsid varchar(255) primary key,pass varchar(255) NOT NULL);")
  print("admins table successfully created")
except Exception as e:
  print(e)

try:
  # creating admins table to store admins information
  mycursor.execute(
      "insert into admins values('admin','open@me');")

except Exception as e:
  print(e)

# main program is at the last i.e line no 420


def login(a):
  user = str(input("enter "+a+"id:"))
  m=[]
  try:
    sql = "select pass from " + a + " where " + a + "id =  " + user

    mycursor.execute(sql)
    m = mycursor.fetchall();

  except:
    print("enter the id in correct format i.e string should be entered within  ''")


  if m == []:
    print("invalid username")
    login(a)
  else:
    if (m[0][0] == str(input("enter the password"))):

      sql = "select * from "+a+ " where "+a+"id = " + user

      mycursor.execute(sql)
      m = mycursor.fetchall()
      m.append(a)
      return m
    else:
      print("password and user name doesn't match \n please try again")
      login(a)


def newteacher(y):
  m = y
  a = str(input(" teacher name: "))
  b = str(input("teacher department: "))
  c = str(input("teacher salary:"))
  d = str(input("teacher experience:"))

  sql = "INSERT INTO teacher (pass,teachername,department,salary,experience)  values('1234','"+a+"','"+b+"',"+c+","+d+")"
  mycursor.execute(sql)

  sql = "SELECT * FROM teacher WHERE teacherid=(SELECT max(teacherid) FROM teacher)"
  mycursor.execute(sql)
  m = mycursor.fetchmany()
  print("teacher Username id for entering the portal : " + str(m[0][0]))
  print("password  for entering the portal           : " + str(m[0][1]))




def updateteachersalary(y):
  m = y
  a=str(input("enter teacherid"))
  sql="select average from studentmarks where studentid in (select studentid from student where consellorid ="+a+ ")"
  mycursor.execute(sql)
  m = mycursor.fetchall()
  s=0
  for i in m:
    s=s+i[0]
  if(s/len(m)>50):
    print("this one is eligible for increment")
    sql="select * from teacher where teacherid ="+a
    mycursor.execute(sql)
    k=mycursor.fetchall()
    sql = "update  teacher set salary = "+str(k[0][3])+ "+10000 where teacherid ="+a
    mycursor.execute(sql)
    sql = "select * from teacher where teacherid =" + a
    mycursor.execute(sql)
    l = mycursor.fetchall()
    print("before update")
    print(k)
    print("------------------------------")
    print("after update")
    print(l)
    print("------------------------------")
  else:
    print("not eligible for increment")




def viewstudentmarks(y):
  m = y
  a = str(input("enter studentid"))
  sql="select * from studentmarks   where studentid = "+str(a)
  mycursor.execute(sql)
  k = mycursor.fetchall()
  print(k)




def updatestudentmarks_A(a):
  a = str(input("studentid: "))
  try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Sumanth@89",
      database="newdatabase"
    )

    mycursor = mydb.cursor()
    sql = "select * from student where studentid =" + a
    mycursor.execute(sql)
    b = int(input("enter new IA1 marks: "))
    c = int(input("enter new IA2 marks: "))
    d = int(input("enter new FA marks: "))
    e = (((b + c) / 2) + d) / 2
    sql = "update  studentmarks set ia1marks = " + str(b) + " ,ia2marks = " + str(c) + " ,famarks= " + str(
      d) + " ,average=" + str(e) + " where studentid =" + str(a)

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Sumanth@89",
      database="newdatabase"
    )

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    sql = "select * from studentmarks where studentid =" + a
    mycursor.execute(sql)
    y = mycursor.fetchall()
    mycursor.execute("SHOW columns FROM studentmarks")
    k = mycursor.fetchall()
    for i in range(len(k)):
      print(k[i][0], "=", y[0][i])

  except:
    print("no student is registered with that id")




def newstudent(a):

  m=a
  a = str(input("student first name: "))
  b = str(input("student last name: "))
  print("goning to execute")
  mycursor.execute("SELECT COUNT(teacherid) FROM teacher")
  k = mycursor.fetchall()
  l=k[0][0]
  if l==0:
    l=1
  print("executed")
  # we are considering that teachers table has it alteast one teacher present
  c=random.randint(0, l)
  sql = "INSERT INTO student (pass,firstname, lastname,fullname,consellorid) VALUES ('1234','"+a+"','"+b+"','"+a+" "+b+"',"+str(c)+")"
  mycursor.execute(sql)

  sql="SELECT * FROM student WHERE studentid=(SELECT max(studentid) FROM student)"
  mycursor.execute(sql)
  m=mycursor.fetchall()
  print("student Username id for entering the portal : "+str(m[0][0]))
  print("password  for entering the portal           : " + str(m[0][1]))
  print("id  of consellor assigned to you is:",l)

def updateteacherinfo(a):
    a=str(input("enter teacherid"))
    b=str(input("please enter the new teacher name"))
    c=str(input("please enter the new experience"))
    d=str(input("please enter the new department"))
    sql = "select * from teacher   where teacherid = " + a
    mycursor.execute(sql)
    k = mycursor.fetchall()
    mycursor.execute("SHOW columns FROM teacher")
    l = mycursor.fetchall()
    print("before updation")
    print("-----------------------------------")

    for i in range(len(l)):
        if i == 1:
            continue
        print(l[i][0], "=", k[0][i])
    print("----------------------")
    print("after updation")
    print("-----------------------------------")

    sql="update teacher set teachername ='{}',experience = {},department='{}' where teacherid={}".format(b,c,d,a)
    mycursor.execute(sql)
    sql = "select * from teacher   where teacherid = " + a
    mycursor.execute(sql)
    k = mycursor.fetchall()
    for i in range(len(l)):
        if i == 1:
            continue
        print(l[i][0], "=", k[0][i])
    print("----------------------")


def enterstudentmarks(a):
  m = a
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Sumanth@89",
    database="newdatabase"
  )

  mycursor = mydb.cursor()
  while(1):
    a = str(input("studentid: "))
    try:
      sql = "select * from student where studentid =" + a
      mycursor.execute(sql)
    except:
      print("no student is registered with that id")
      continue
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Sumanth@89",
      database="newdatabase"
    )

    mycursor = mydb.cursor()



    sql= "select consellorid from student where studentid = " +a
    mycursor.execute(sql)
    z=mycursor.fetchall()
    print(z[0][0])
    print(m[0][0])
    if(z[0][0]==m[0][0]):
      try:

        sql1 = "select * from studentmarks where studentid=" + a

        mycursor.execute(sql1)
        z = mycursor.fetchall()
        print(z)
        print("the student marks are already uploaded")
        break
      except:
        b = int(input("enter IA1 marks: "))
        c = int(input("enter IA2 marks: "))
        d = int(input("enter FA marks: "))
        e = (((b + c) / 2) + d) / 2
        sql = "INSERT INTO studentmarks (" + str(a) + "," + str(b) + "," + str(c) + " " + str(d) + "," + str(e) + ")"
        mycursor.execute(sql)

        break
    else:
      print("the student is not assign to you .. you can only add marks to the students who are only assigned to you")
      print("try again")
      break




def updatestudentmarks_T(a):
  m = a
  while (1):
    a = str(input("studentid: "))
    try:

      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Sumanth@89",
        database="newdatabase"
      )
      mycursor = mydb.cursor()
      sql = "select * from student where studentid =" + a
      mycursor.execute(sql)
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Sumanth@89",
        database="newdatabase"
      )

      mycursor = mydb.cursor()

      sql = "select consellorid from student where studentid = " + a
      mycursor.execute(sql)
      z = mycursor.fetchall()
      if (z[0][0] == m[0][0]):
        b = int(input("enter new IA1 marks: "))
        c = int(input("enter new IA2 marks: "))
        d = int(input("enter new FA marks: "))
        e = (((b + c) / 2) + d) / 2
        sql = "update  studentmarks set ia1marks = " + str(b) + " ,ia2marks = " + str(c) + " ,famarks= " + str(
          d) + " ,average=" + str(e) + " where studentid =" + str(a)
        mycursor.execute(sql)
        sql = "select * from studentmarks where studentid =" + a
        mycursor.execute(sql)
        y = mycursor.fetchall()
        mycursor.execute("SHOW columns FROM studentmarks")
        k = mycursor.fetchall()
        for i in range(len(k)):
          print(k[i][0],"=",y[0][i])
        break
    except:
      print("no student is registered with that id")
      continue


    else:
      print(
        "the student is not assign to you .. you can only update marks to the students who are only assigned to you")
      print("try again")
      break




def viewteacherinfo(a):
  m=a
  sql = "select * from teacher   where teacherid = " + str(m[0][0])
  mycursor.execute(sql)
  k = mycursor.fetchall()
  mycursor.execute("SHOW columns FROM teacher")
  l = mycursor.fetchall()
  for i in range(len(l)):
    if i == 1:
      continue
    print(l[i][0], "=", k[0][i])




def viewstudent(a):

  m=a
  mycursor.execute("SHOW columns FROM student")
  k = mycursor.fetchall()
  print("the student informatiom is:")
  print("------------")
  for i in range(len(k)):
    print(k[i][0],"=",m[0][i])
  print("------------")





def updatestudent(a):
  m = a
  mycursor.execute("SHOW columns FROM student")
  k = mycursor.fetchall()

  a=str(input("new first name: "))
  b=str(input("new last name: "))
  c=str(input("enter new password"))
  sql="update  student set firstname = '"+a+"',lastname = '"+b+"' ,pass= '"+c+"',fullname='"+a+" "+b+ "' where studentid ="+str(m[0][0])
  mycursor.execute(sql)
  mycursor.execute("select * from student where studentid="+str(m[0][0]))


  print("-------------")
  print("oringinal info:")
  for i in range(len(k)):
    print(k[i][0],"=",m[0][i])

  print("-------------")
  print("updated info:")
  z = mycursor.fetchall()
  for i in range(len(k)):
    print(k[i][0],"=",z[0][i])

  print("------------------------------")




def consellorinfo(y):
  sql = "select * from teacher   where teacherid = " + str(y[0][5])
  mycursor.execute(sql)
  k = mycursor.fetchall()
  mycursor.execute("SHOW columns FROM teacher")
  l = mycursor.fetchall()
  for i in range(len(l)):
    if i==1:
      continue
    print(l[i][0],"=",k[0][i])


def updatepassword(a):
    while(1):
        m = str(input("enter the old password"))
        if (str(a[0][1]) == m):
            print("password doesn't match")
            print("try again")
        else:
            break
    z=str(input("enter new password"))
    y=str(input("re enter the new password"))
    if(z==y):
        sql="upadate {} set pass= '{}' where {}id={}".format(a[1],z,a[1],a[0][0])
        mycursor.execute(sql)
        print("password updated")

    else:
        print("re entered password doesn't match")
        print("try again")





# main program starts here
print("prerequisites for processing this project is a working python ide and mysql server installined in your computer ")
print("if this is the first time running this project login with admin portal using \n username : admin \n password:open@me")
print("create some teacher portals and continue")
print("----------------------------")
n=input("press enter to contiue")
print("----------------------------")
while(1):
  print("1.Admistrator")
  print("2.Teacher")
  print("3.student")
  print("4.quit")
  print("-----------------------------------------------------------------------")
  a = int(input("enter your choice:"))
  print("-----------------------------------------------------------------------")
  if(a==4):
    break
  if a == 1:
    k = login("admins")
    
    while(1):

      print("-----------------------------------------------------------------------")
      print("1.create new teacher")
      print("2.update teacher salary")
      print("3.view student marks")
      print("4.update student marks")
      print("5.add new student")
      print("6.update teacherinfo")
      print("7.update password")
      print("8.logout from admin portal")
      print("-----------------------------------------------------------------------")
      c1 = {1: newteacher, 2: updateteachersalary, 3: viewstudentmarks, 4: updatestudentmarks_A,5:newstudent,6:updateteacherinfo,7:updatepassword}
      z1 = int(input("enter your choice"))
      if(z1==8):
        break
      print("----------------------------------------------")
      try:
        d1 = c1[z1](k)
        print("----------------------------------------------")
        op=input("press enter to continue")
      except Exception as e:
        print(e)
        print("please enter the correct choice")




  elif a == 2:
    k = login("teacher")

    while(1):

      print("---------------------------------------------------------------------")
      print("1.add new student")
      print("2.enter student marks")
      print("3.update student marks")
      print("4.viewteacherinfo")
      print("5.update password ")
      print("6.logout from teacher portal")
      print("---------------------------------------------------------------------")
      c1 = {1: newstudent, 2: enterstudentmarks, 3: updatestudentmarks_T ,4:viewteacherinfo,5:updatepassword}
      z1 = int(input("enter your choice"))
      print("-----------------------------------")
      if(z1==6):
        break
      try:
        d1 = c1[z1](k)
        print("----------------------------------------------")
        op = input("press enter to continue")
      except Exception as e:
        print(e)
        print("please enter the correct choice")

  elif a == 3:
    k = login("student")
  
    while(1):

      print("---------------------------------------------------------------------")
      print("1.view student info")
      print("2.update student info")
      print("3.view student marks")
      print("4.view your consellor info")
      print("5.update password")
      print("6.logout from student portal")
      print("-----------------------------------------------------------------------")
      if (k == 5):
        break
      c = {1: viewstudent, 2: updatestudent, 3: viewstudentmarks, 4: consellorinfo,5:updatepassword}
      z = int(input("enter your choice"))
      print("-----------------------------------")
      try:
        d = c[z](k)
        print("----------------------------------------------")
        op = input("press enter to continue")
      except Exception as e:
        print(e)
        print("please enter the right choice")


  else:
    print("enter the right choice ")






































