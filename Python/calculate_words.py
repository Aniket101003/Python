print("program to count number of words in a binary file")
print()

file=open("binaryfile","rb")
count=0
content=file.read()
for i in content:
    count+=1
print("Total number of words in binary file :",count)
    
file.close()

