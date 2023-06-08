print("menu based program for bubble sort and insertion sort")
print()

def bubble_sort():
    list1=[]
    n=int(input("enter number of elements:"))
    for i in range(0,n):
        num=int(input("enter the number:"))
        list1.append(num)
    print("original list is:",list1)

    length=len(list1)
    for i in range(length):
        for j in range(0,length-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    print("List through bubble sort:",list1)
def insertion_sort():
    list2=[]
    a=int(input("enter number of elements:"))
    for i in range(0,a):
        num1=int(input("enter the number:"))
        list2.append(num1)
    print("the original list is:",list2)
    for i in range(0,len(list2)):
        key=list2[i]
        j=i-1
        while j>=0 and key<list2[j]:
            list2[j+1]=list2[j]
            j=j-1
        else:
            list2[j+1]=key
    print("list through inertion sort is:",list2)

bubble_sort()
insertion_sort()








                    
                   
    
                    
