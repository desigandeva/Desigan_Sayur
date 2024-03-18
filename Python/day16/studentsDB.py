# DB problems.
# Create a DB for student data in Mysql. There are three tables. 
# Student details table
#     Student Id,Name, Address, Class (1 to 12), Gender (Male/Female), email id
# Exam details table
#     Exam id, Name (Quarterly, helf yearly , etc), Exam Month (Sep, Dec, etc - the month in which the exam was held
#     ), Subject (Math, Physics,etc)
# Mark table
#     StudentId, Exam id, mark (0-100)
# Create a CSV file with actual data for each of these tables.
# Write a python program to read from this csv file and write to these tables.
# Once the data is loaded in tables, answer the following questions.
# 1. List all the students that scored >90 in Math.
# 2. List the number of students that scores >80 in each Subject
# 3. List the number of male students and number of female students that scored >90 in Math
# 4. List the number of students in each class (1 to 12)
# 5. List the number of students whose name starts with 'A' or 'C'
# 6. List the avg marks for students in each subject in each class
# 7. List all the student details in ascending order of mark and grade (all 12 the grade students 
# first and then 11th etc)
# 8. List all the students who come from Madurai and Trichy
# 9. List all the students who scored >90 in Math in Final exam and Quarterly exam
# 
# DB problems.
# Create a DB for student data in Mysql. There are three tables. 
# Student details table
# Student Id,Name, Address, Class (1 to 12), Gender (Male/Female), email id
# Exam details table
# Exam id, Name (Quarterly, helf yearly , etc), Exam Month (Sep, Dec, etc -exam was held ), Subject (Math, Physics,etc)
# Mark table
# StudentId, Exam id, mark (0-100)
# 
# create table student(sId varchar(10) not null ,sName varchar(25) not null, sAddress varchar(25) not null, sClass int not null, sGender varchar(1) not null, sEmail varchar(30) not null,primary key (sId))
# create table exam(eId varchar(10) not null ,eName varchar(15) not null,eMonth varchar(3) not null,eSubject varchar(15) not null,primary key (eId))
# create table mark(sId varchar(10) not null , eId varchar(10) not null ,Mark int not null)
# 

import mysql.connector
import pandas as pd
# import xlrd
import csv
# import openpyxl

# connect the local database
mysql = mysql.connector.connect(host="localhost",user="root",password="root",database="school")
mycursor = mysql.cursor()

# build aa function for display table
def listTables():
    mycursor.execute("show tables")
    for item in mycursor:
        print(item)

# build a function for list a students
def listStudent():
    # execute the query for list theater owner's
    mycursor.execute("select * from student")

# build a function for list a Exam
def listExam():
    # execute the query for list theater's
    mycursor.execute("select * from exam")

# build a function for list a mark
def listMark():
    # execute the query for list theater's
    mycursor.execute("select * from mark")

# build a function for alter table 
def alterTable():
    # execute the query for altering tables
    query = input("Enter your query : ")
    mycursor.execute(query)

# build a function for store the data in csv file to database
def storeStudentData():
    # data1 = pd.read_excel("./day16/student.xlsx")
    # data1 = data1.to_dict()
    # for i in range(len(data1['sId'])):
    #     query = "insert into student (sId,sName,sAddress,sClass,sGender,sEmail) values (%s,%s,%s,%s,%s,%s)"
    #     data =  (data1["sId"][i],data1["sName"][i],data1["sAddress"][i],data1["sClass"][i],data1["sGender"][i],data1["sEmail"][i])
    #     print(data)
    #     mycursor.execute(query,data)
    #     mysql.commit()
    # open and read csv file 
    data_file = open("./day16/student.csv",'r')
    data_list = csv.reader(data_file)
    for item in data_list:
        # insert mysql query
        query = "insert into student (sId,sName,sAddress,sClass,sGender,sEmail) values (%s,%s,%s,%s,%s,%s)"
        # datas
        data =  (item[0],item[1],item[2],item[3],item[4],item[5])
        print(data)
        # insert the data into table
        mycursor.execute(query,data)
        # commit the database (save)
        mysql.commit()

# build a function for store the data in csv file to database
def storeExamData():
    # data1 = pd.read_excel("./day16/exam.xlsx")
    # data1 = data1.to_dict()
    # for i in range(len(data1['eId'])):
    #     query = "insert into exam (eId,eName,eMonth,eSubject) values (%s,%s,%s,%s)"
    #     data = (data1["eId"][i],data1["eName"][i],data1["eMonth"][i],data1["eSubject"][i])
    #     print(data)
    #     mycursor.execute(query,data)
    #     mysql.commit()
    data_file = open("./day16/exam.csv",'r')
    data_list = csv.reader(data_file)
    for item in data_list:
        query = "insert into exam (eId,eName,eMonth,eSubject) values (%s,%s,%s,%s)"
        data = (item[0],item[1],item[2],item[3])
        print(data)
        mycursor.execute(query,data)
        mysql.commit()

# build a function for store the data in csv file to database
def storeMarkData():
    # data1 = pd.read_excel("./day16/mark.xlsx")
    # data1 = data1.to_dict()
    # for i in range(len(data1['sId'])):
    #     query = "insert into mark (sId,eId,Mark) values (%s,%s,%s)"
    #     data = (data1["sId"][i],data1["eId"][i],data1["Mark"][i])
    #     print(data)
    #     mycursor.execute(query,data)
    #     mysql.commit()
    data_file = open("./day16/mark.csv",'r')
    data_list = csv.reader(data_file)
    for item in data_list:
        query = "insert into mark (sId,eId,Mark) values (%s,%s,%s)"
        data = (item[0],item[1],item[2])
        print(data)
        mycursor.execute(query,data)
        mysql.commit()

# build a function for call all store function to store the data
def csvToDatabase():
    storeStudentData()
    storeExamData()
    storeMarkData()


# List all the students that scored >90 in Math.
query1 = "select student.sName from student join mark on student.sId=mark.sId join exam on exam.eSubject='Math' where mark.Mark > 90;"
# List the number of students that scores >80 in each Subject
query2 = "select count(student.sName) from student join mark on student.sId=mark.sId where mark.Mark > 80"
# List the number of male students and number of female students that scored >90 in Math
query3 = "select count(student.sName) from student join mark on student.sId=mark.sId join exam on exam.eSubject='Math' where mark.Mark > 90 and student.sGender='M'"
query3 = "select count(student.sName) from student join mark on student.sId=mark.sId join exam on exam.eSubject='Math' where mark.Mark > 90 and student.sGender='F'"
# List the number of students in each class (1 to 12)
query4 = "select count(sName) from student"
# List the number of students whose name starts with 'A' or 'C'
query5 = "select count(sName) from student where sName like 'A%' or 'C%'"
# List the avg marks for students in each subject in each class
query6 = "select student.sName from student join mark on student.sId = mark.sId where mark.Mark > 50"
# List all the student details in ascending order of mark and grade (all 12 the grade students first and then 11th etc)
query7 = "select student.sName,student.sAddress,student.sClass,student.sGender,student.sEmail,mark.Mark from student join mark  on student.sId = mark.sId order by student.sClass desc,mark.Mark"
# List all the students who come from Madurai and Trichy
query8 = "select sName,sAddress from student where sAddress='Madurai' or sAddress='Trichy'"
# List all the students who scored >90 in Math in Final exam and Quarterly exam
query9 = "select student.sName,exam.eName,mark.Mark from student join mark on student.sId=mark.sId join exam on exam.eId=mark.eId where (exam.eName='Final'or exam.eName='Quarterly') and mark.Mark>90"

# store the data to data basae 
csvToDatabase()
# execute the query
mycursor.execute(query1)
# print the value
for item in mycursor:
    print(item)