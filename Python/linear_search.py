print("program for linear search")
print()

lst=[]
n=int(input("enter total number of elements:"))
for i in range(0,n):
    element=int(input("enter number:"))
    lst.append(element)
    
num=int(input("enter item to be searched:"))
result=False
for i in range(0,len(lst)):
    if lst[i]==num:
        print("element found at position",i)
        result=True
if result==False:
    print("sorry!!! element not found")

