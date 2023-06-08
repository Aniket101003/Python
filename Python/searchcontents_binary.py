import pickle

print("jo11")
print("name: Anike More")
print("grade: 12  Div: A ")
print("program to create binary file with name and roll no. Search\
for a given rollno and display the name")

dict={}

def Write_To_File():
    file=open("student","wb")
    num=int(input("Enter no. of students:"))
    for i in range(num):
        dict['roll']=int(input("Enter roll number:"))
        dict['name']=input("Enter name:")
        pickle.dump(dict,file)
    file.close()
def Display():
    file=open("student","rb")
    try:
        while True:
            student=pickle.load(file)
            print(student)
    except EOFError:
        pass
    file.close()
def Search():
    file=open("student","rb")
    rollno=int(input("Enter rollno to be search:"))
    found=0
    try:
        while True:
            data=pickle.load(file)
            if data['roll']==rollno:
                print("The rollno =",rollno," record found")
                print(data)
                found=1
                break
    except EOFError:
        pass
    if found==0:
        print("The rollno=",r," record is not found")
    file.close()

Write_To_File()
Display()
Search()







        
            
