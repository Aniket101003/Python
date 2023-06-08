print("program to check if a given number is a palindrome")
print()

num=int(input("enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=int(num//10)
if (temp==rev):
    print("The number is a palindrome")
else:    
    print("The number is not a palindrome")
    
