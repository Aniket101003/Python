print("program to create and read a binary file")
print()
import pickle
def WriteToFile():
    file=open("binaryfile","wb")
    n=int(input("Total number of record: "))
    for i in range(n):
        name=input("enter your name:")
        phone=int(input("enter phone number:"))
        game=input("enter game:")
        rec=[name,phone,game]
        pickle.dump(rec,file)
    file.close()
def read():
    file=open("binaryfile","rb")
    try:
        while True:
            binaryfile=pickle.load(file)
            print(binaryfile)
    except EOFError:
        pass
    file.close()
WriteToFile()
read()

    

                  
    
