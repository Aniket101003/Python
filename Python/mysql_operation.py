print("jo24")
print("name:Aniket More")
print("grade:12 Div:A:")
print("program to create a table and insert,update and delete records from a \
database")
print()
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aniket")
mycursor=mydb.cursor()
#creating database
mycursor.execute("DROP DATABASE IF EXISTS School")
mycursor.execute("CREATE DATABASE School")
mycursor.execute("USE School")
#creating table
mycursor.execute("DROP TABLE IF EXISTS STUDENT")
mycursor.execute("CREATE TABLE STUDENT(admn_no INT(10) PRIMARY KEY, \
sname VARCHAR(30), gender CHAR(1), DOB date, stream VARCHAR(15), \
marks int(10))")
#inserting rows into table
def insert():
    while True:
        admnno=int(input("Enter the admission number: "))
        sname=input("Enter the students name: ")
        gender=input("Enter students gender M/F : ")
        DOB=input("Enter students date of birth: ")
        stream=input("Enter students stream: ")
        marks=int(input("Enter students marks: "))
        data=[admnno, sname, gender, DOB, stream, marks]


        sql="INSERT INTO STUDENT(admn_no, sname, gender, DOB, stream, marks)\
VALUES(%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql,data)
        mydb.commit()
        ch=input("Do you want to enter more records y/n ? ")
        if ch.lower() in ["y","yes"]:
            pass
        else:
            return
#to fetch and dispaly all records
def display():
    print()
    print("DISPLAYING RECORDS.....")
    print()
    mycursor.execute("SELECT*FROM STUDENT")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#updating a record
def update():
    print()
    print("UPDATING A RECORD.....")
    print()
    admnno=int(input("Enter admn_no of student whose record is to be updated:"))
    sname=input("Enter the students updated name: ")
    gender=input("Enter the students updated gender:" )
    DOB=input("Enter the students updated DOB:" )
    stream=input("Enter the students updated stream: ")


    marks=int(input("Enter the students updated marks: "))
    data=[admnno, sname, gender, DOB, stream, marks]
    sql="UPDATE STUDENT SET\
    admn_no=%s,sname=%s,gender=%s,DOB=%s,stream=%s,marks=%s where\
    admn_no='{}'".format(admnno)
    mycursor.execute(sql,data)
#displaying records after updating
    print()
    print("RECORDS AFTER UPDARING:")
    print()
    mycursor.execute("SELECT*FROM STUDENT")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#deleting a record
def delete():
    print()
    print("DELETING A RECORD")
    print()
    admnno=input("Enter admn_no of student whose record is to be deleted: ")
    sql="DELETE FROM STUDENT WHERE admn_no='{}'".format(admnno)
    mycursor.execute(sql)
#displaying records after deleting
    print()
    print("RECORDS AFTER DELETING:")
    print()
    mycursor.execute("SELECT*FROM STUDENT")
    result=mycursor.fetchall()



















    for x in result:
        print(x)


insert()
display()
update()
delete()






















