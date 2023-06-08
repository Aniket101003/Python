print("jo21")
print("name: Aniket More")
print("grade:12 Div:A")
print("program to insert,update and delete data in a database")
print()

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aniket")
mycursor=mydb.cursor()
#creating database
mycursor.execute("DROP DATABASE IF EXISTS bus")
mycursor.execute("CREATE DATABASE bus")
mycursor.execute("USE bus")
#creating table
mycursor.execute("DROP TABLE IF EXISTS SchoolBus")
mycursor.execute("CREATE TABLE SchoolBus(BusNo INT(10), \
Area_covered VARCHAR(100), Capacity INT(10), Noofstudents INT(10), \
Distance INT(10), Transporter VARCHAR(100), Charges INT(10))")
#inserting rows into table
def insert():
    while True:
        BusNo=int(input("Enter Bus Number: "))
        Area_Covered=input("Enter area covered: ")
        Capacity=int(input("Enter capacity of the bus: "))
        Noofstudents=int(input("enter total no of students: "))
        Distance=int(input("Enter distance in km: "))
        Transporter=input("Enter name of transporter: ")
        Charges=int(input("Enter charges per year: "))



        data=[BusNo, Area_Covered, Capacity, Noofstudents, Distance, \
              Transporter, Charges]
        sql="INSERT INTO SchoolBus(BusNo, Area_Covered, Capacity, Noofstudents,\
Distance, Transporter, Charges)VALUES(%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql,data)
        mydb.commit()
        ch=input("Do you want to enter more records y/n :")
        if ch.lower() in ["y","yes"]:
            pass
        else:
            return
#to fetch and dispaly the records
def display():
    print()
    print("DISPLAYING RECORDS.....")
    print()
    mycursor.execute("SELECT*FROM SchoolBus")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#updating a record
def update():
    print()
    print("UPDATING A RECORD.....")
    print()
    BusNo=int(input("Enter Bus number whose details are to be updated:"))
    Area_Covered=input("Enter the Area updated:")
    Capacity=int(input("Enter the updated capacity of students:"))


    Noofstudents=int(input("Enter the updated no of students:"))
    Distance=int(input("Enter updated distance in km:"))
    Transporter=input("Enter updated transporter:")
    Charges=int(input("Enter updated charges:"))
    data=[BusNo, Area_Covered, Capacity, Noofstudents, Distance, Transporter, \
          Charges]
    sql="UPDATE SchoolBus SET \
BusNo=%s, Area_Covered=%s, Capacity=%s, Noofstudents=%s, Distance=%s, \
Transporter=%s, Charges=%s WHERE BusNo='{}'".format(BusNo)
    mycursor.execute(sql,data)
#to display records after updating
def updated_display():
        print()
        print("RECORDS AFTER UPDATING.....")
        print()
        mycursor.execute("SELECT*FROM SchoolBus")
        result=mycursor.fetchall()
        for x in result:
            print(x)
#deleting a record
def delete():
    print()
    print("DELETING A RECORD.....")
    print()
    BusNo=int(input("Enter BusNo to be deleted: "))
    sql="DELETE FROM SchoolBus WHERE BusNo='{}'".format(BusNo)
    mycursor.execute(sql)



#to display records after deleting
    print()
    print("records after deleting")
    print()
    mycursor.execute("SELECT*FROM SchoolBus")
    result=mycursor.fetchall()
    for x in result:
        print(x)

insert()
display()
update()
updated_display()
delete()






















        
