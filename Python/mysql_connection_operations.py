print("jo22")
print("name:Aniket More")
print("grade:12 Div:A")
print("program to connect python with mysql using database connectivity and \
perform fetch,update and delete the data")
print()

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aniket")
mycursor=mydb.cursor()
#creating database
mycursor.execute("DROP DATABASE IF EXISTS airways")
mycursor.execute("CREATE DATABASE airways")
mycursor.execute("USE airways")
#creating table
mycursor.execute("DROP TABLE IF EXISTS Flights")
mycursor.execute("CREATE TABLE Flights(Fl_No  VARCHAR(10), Start VARCHAR(50), \
Ending VARCHAR(50), No_of_Flights INT(10), No_of_Stops INT(10), \
No_of_Seats INT(10))")
#inserting rows into table
sql="INSERT INTO Flights(Fl_No, Start, Ending, No_of_Flights, No_of_Stops, \
No_of_Seats) VALUES (%s, %s, %s, %s, %s, %s)"
rows=[('F101','Mumbai','Delhi',3,0,150),
      ('F102','Chennai','Sydney',1,1,200),
      ('F103','Kolkata','Goa',4,0,150),
      ('F104','Mumbai','New York',2,2,250)]
mycursor.executemany(sql,rows)
mydb.commit()



#to fetch and display the records
mycursor.execute("SELECT*FROM Flights")
result=mycursor.fetchall()
for x in result:
    print(x)
#updating the data
mycursor.execute("UPDATE Flights SET No_of_Seats=200 WHERE Fl_No='F103'")
mydb.commit()
#to display data after updating
print("RECORDS AFTER UPDATING")
mycursor.execute("SELECT*FROM Flights")
result=mycursor.fetchall()
for x in result:
    print(x)
#deleting the data
mycursor.execute("DELETE FROM Flights WHERE Fl_No='F104'")
mydb.commit()
#to dispay records after deleting
print("RECORDS AFTER DELETING")
mycursor.execute("SELECT*FROM Flights")
result=mycursor.fetchall()
for x in result:
    print(x)




    
    

