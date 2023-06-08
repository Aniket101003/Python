print("program to test if a string is a palindrome or not")
print()

string=input("Enter string: ")
string2=string[::-1]
if (string==string2):
    print("The string is a palindrome!!")
else:
    print("The string is not a palindrome")

