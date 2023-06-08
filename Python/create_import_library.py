print("jo9")
print("name:Aniket More")
print("grade:12 Div:A")
print("Program to create a library in python and import it in a program. Circle\
 function will display area of circle. Rectangle function will display area of\
 rectangle. Import the function in a third file and see the usage of import")
print()

def Area():
    while True:
        print(" 1. Area of circle")
        print(" 2. Area of Rectangle")
        print(" 3. Exit")
        area=int(input("Enter number corresponding to area of circle/rectangle: "))
        if area==1:
            import Circle
        elif area==2:
            import Rectangle
        elif area==3:
            break
        else:
            print("INVALID NUMBER")
            continue

Area()
             
