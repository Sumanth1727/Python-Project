use  pythondb;

show tables;
select * from teacher;
insert into teacher(teachername,pass,department,salary,experience)
  values('MBK','1234','ECE',90000,12);
 
select * from student
insert into student(pass,firstname,lastname,fullname,consellorid)
  values('1234','vikas','pani','vikas pani',4);

alter table student
drop experience;

select * from studentmarks
insert into studentmarks
values(9,80,40,60,60);
select * from studentmarks
where studentid in (select studentid from student where consellorid =1);

select * from admins
alter table admins
rename column username to adminsid;

INSERT INTO student (pass,firstname, lastname,fullname,consellorid) VALUES ('1234','eswar','yaswanth','eswar yaswanth',2)

update  student set firstname = '1',lastname = 'pranav' ,pass= '1234',fullname='1 pranav' where studentid =1

select consellorid from student where studentid =1
select consellorid from student where studentid = 4






SELECT student.fullname FROM student FULL OUTER JOIN studentmarks ON student.studentid = studentmarks.studentid where student.studentid=1;