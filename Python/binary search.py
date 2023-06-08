print("program to search an element entered by the user using\
recursive binary search method")
print()

def BinarySearch(Arr,L,R,X):
    if R>=L:
        mid=L+(R-L)//2
        if Arr[mid]==X:
            return mid
        elif Arr[mid]>X:
            return BinarySearch(Arr,L,mid-1,X)
        else:
            return BinarySearch(Arr,mid+1,R,X)
    else:
        return-1
Arr=[2,3,23,10,25]
X=int(input("Enter element to be searched:"))
result=BinarySearch(Arr,0,len(Arr)-1,X)
if result != -1:
    print("Element is present at index",result)
else:
    print("Element not found")

