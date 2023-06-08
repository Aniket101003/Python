print("menu based program to perform the operations on a stack in python")
print()

#adding item to the top of stack
def push(stack):
    pin=int(input("enter pin code:"))
    city=input("enter city name:")
    stack.append({'pin':pin, 'city':city})

#removing element at top of the stack
def pop(stack):
    if stack==[]:
        print("UNDERFLOW")
        return 0
    else:
        item=stack.pop()
    return item










#viewing the value
def peek(stack):
    if stack==[]:
        print("Stack is empty")
        return 0
    else:
        top=len(stack)-1
        return stack[top]

def display(stack):
    if stack==[]:
        print("Stack is empty")
        return 0
    else:
        top=len(stack)-1
        print("TOP:", stack[top])
        for i in range(top-1,-1,-1):
            print(stack[i])
















def menu():
    stack=[] #implementing stack as list
    while True:
        print("STACK MENU:")
        print("1 Push")
        print("2 Pop")
        print("3 Peek")
        print("4 Display Stack")
        print("5 Exit")
        selection=input(" SELECT (1/2/3/4/5):")
        if selection=="1":
            push(stack)
            continue
        elif selection=="2":
            item=pop(stack)
            if item==0:
                continue
            else:
                print("Popped item is:",item)
                continue
        elif selection=="3":
            item=peek(stack)
            if item==0:
                continue
            else:
                print("Topmost item is:",item)
                continue
        elif selection=="4":
            item=display(stack)
            if item==0:
                continue
            continue
        elif selection=="5":
            break
        else:
            print("INVALID COMMAND")


#MAIN
top=None
menu()














