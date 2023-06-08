print("jo25")
print("name:Aniket More")
print("grade:12 Div:A")
print("program to insert,update and delete records from a table")
print()

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aniket")
mycursor=mydb.cursor()
#creating database
mycursor.execute("DROP DATABASE IF EXISTS work")
mycursor.execute("CREATE DATABASE work")
mycursor.execute("USE work")
#creating table
mycursor.execute("DROP TABLE IF EXISTS Employee")
mycursor.execute("CREATE TABLE Employee(EmpNo VARCHAR(10), EmpName VARCHAR(50),\
 DOJ date, Designation VARCHAR(50), Salary INT(20))")
#inserting rows into table
def insert():
    while True:
        EmpNo=input("Enter employee number: ")
        EmpName=input("Enter employee name: ")
        DOJ=input("Enter date of joining: ")
        Designation=input("Enter designation: ")
        Salary=int(input("Enter salary: "))
        data=[EmpNo, EmpName, DOJ, Designation, Salary]
        sql="INSERT INTO Employee(EmpNo, EmpName, DOJ, Designation, Salary) \
VALUES (%s, %s, %s, %s, %s)"


        mycursor.execute(sql,data)
        mydb.commit()
        ch=input("Do you want to enter more records??  y/n: ")
        if ch.lower() in ["y","yes"]:
            pass
        else:
            return
#to fetch and display all records
def display():
    print()
    print("DISPLAYING RECORDS.....")
    print()
    mycursor.execute("SELECT*FROM Employee")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#updating a record
def update():
    print()
    print("UPDATING A RECORD:")
    print()
    EmpNo=input("Enter Employee number whose records are to be updated: ")
    EmpName=input("Enter updated Employee name: ")
    DOJ=input("Enter update date of joining: ")
    Designation=input("Enter updated Designation: ")
    Salary=int(input("Enter updated Salary: "))
    data=[EmpNo, EmpName, DOJ, Designation, Salary]



    sql="UPDATE Employee SET \
EmpNo=%s, EmpName=%s, DOJ=%s, Designation=%s, Salary=%s \
WHERE EmpNo='{}'".format(EmpNo)
    mycursor.execute(sql,data)
#displaying records after updating
    print()
    print("DISPLAYING RECORDS AFTER UPDATING.....")
    print()
    mycursor.execute("SELECT*FROM Employee")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#deleting a record
def delete():
    print()
    print("DELETING A RECORD:")
    print()
    EmpNo=input("Enter employee number whose records are to be deleted: ")
    sql="DELETE FROM Employee WHERE EmpNo='{}'".format(EmpNo)
    mycursor.execute(sql)
#to display records after deleting
    print()
    print("DISPLAYING RECORDS AFTER DELETING.....")
    print()
    mycursor.execute("SELECT*FROM Employee")
    result=mycursor.fetchall()
    for x in result:
        print(x)


insert()
display()
update()
delete()























    
