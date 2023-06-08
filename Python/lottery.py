print("program to generate random number between 1 to 6 and check \
whether the user won a lottery or not")
print()

import random
a=random.randint(1,6)
user=int(input("enter a number:"))
if user==a:
    print("congratulation!!! you won the lottery")
else:
    print("better luck next time")

print("The number is",a)    
    
               
