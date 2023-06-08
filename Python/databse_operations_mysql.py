print("jo23")
print("name:Aniket More")
print("grade:12 Div:A")
print("program to insert,update and delete rows in a database")
print()

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aniket")
mycursor=mydb.cursor()
#creating database
mycursor.execute("DROP DATABASE IF EXISTS food")
mycursor.execute("CREATE DATABASE food")
mycursor.execute("USE food")
#creating table
mycursor.execute("DROP TABLE IF EXISTS Supplier")
mycursor.execute("CREATE TABLE Supplier(SuppNo VARCHAR(10), \
SuppName VARCHAR(50), Status CHAR(10), City VARCHAR(50), qtySupp INT(10), \
ItemNo INT(10))")
#inserting rows into table
def insert():
    while True:
        SuppNo=input("Enter supplier number: ")
        SuppName=input("Enter supplier name: ")
        Status=input("Enter Status: ")
        City=input("Enter City: ")
        qtySupp=int(input("Enter quantity Supply: "))
        ItemNo=int(input("Enter Item Number: "))
        data=[SuppNo, SuppName, Status, City, qtySupp, ItemNo]


        sql="INSERT INTO Supplier(SuppNo, SuppName, Status, City, qtySupp, \
ItemNo) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, data)
        mydb.commit()
        ch=input("Do you want to enter more records  y/n : ")
        if ch.lower() in ["y", "yes"]:
            pass
        else:
            return
#to fetch display the records
def display():
    print()
    print("DISPLAYING RECORDS.....")
    print()
    mycursor.execute("SELECT*FROM Supplier")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#updating a record
def update():
    print()
    print("UPDATING A RECORD")
    print()
    SuppNo=input("Enter SuppNo whose record is to be updated: ")
    SuppName=input("Enter updated SuppName: ")
    Status=input("Enter updated status: ")
    City=input("Enter updated City: ")
    qtySupp=int(input("Enter updated qtySupp: "))


    ItemNo=int(input("Enter updated ItemNo: "))
    data=[SuppNo, SuppName, Status, City, qtySupp, ItemNo]
    sql="UPDATE Supplier SET \
SuppNo=%s, SuppName=%s, Status=%s, City=%s, qtySupp=%s, ItemNo=%s \
WHERE SuppNo='{}'".format(SuppNo)
    mycursor.execute(sql, data)
#to display records after updating
    print()
    print("RECORDS AFTER UPDATING:")
    print()
    mycursor.execute("SELECT*FROM Supplier")
    result=mycursor.fetchall()
    for x in result:
        print(x)
#deleting a record
def delete():
    print()
    print("DELETING A RECORD.....")
    print()
    SuppNo=input("Enter SuppNo whose records are to be deleted: ")
    sql="DELETE FROM Supplier WHERE SuppNo='{}'".format(SuppNo)
    mycursor.execute(sql)
#to display records after deleting
    print()
    print("RECORDS AFTER DELETING:")
    print()
    mycursor.execute("SELECT*FROM Supplier")
    result=mycursor.fetchall()
    for x in result:
        print(x)


insert()
display()
update()
delete()





















    
