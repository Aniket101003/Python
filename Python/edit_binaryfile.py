
print("program to create a binary file with name,marks and roll no. \
and input name and update marks")
print()
import pickle
rec={}
#writting to fiile
students=int(input("Enter no of students:"))
f=open("binaryfile","wb")
for i in range(students):
    rec["roll"]=int(input("enter roll no:"))
    rec["name"]=input("Enter Student Name:")
    rec["percentage"]=float(input("Enter student marks:"))
    pickle.dump(rec,f)
    
f.close()
#reading the file
f=open("binaryfile","rb")
try:
    while True:
        rec=pickle.load(f)
        print(rec)
except EOFError:
    f.close()



#searching and updating
found=False
RollSearch=int(input("Enter roll no. to be searched:"))
f=open("binaryfile","rb+")
try:
    while True:
        pos=f.tell()
        rec=pickle.load(f)
        if (rec["roll"]==RollSearch):
            rec["percentage"]=float(input("enter marks to be updated:"))
            f.seek(pos)
            pickle.dump(rec,f)
            found=True
except EOFError:
    if(found==False):
        print("roll no. not found")
    else:
        print("Student marks updated successfully")
    f.close()
f=open("binaryfile","rb")
try:
    while True:
        rec=pickle.load(f)
        print(rec)
except EOFError:
    f.close()
            
    
    

