print("menu based program to perform the operation on a queue of integers")
print()

def Enqueue(queue):
    item=int(input("Enter an integer:"))
    queue.append(item)

def Dequeue(queue):
    if queue==[]:
        print("UNDERFLOW!")
        return 0
    else:
        item=queue.pop(0)
    if len(queue)==0:
        front=rear=None
    return item

def Peek(queue):
    if queue==[]:
        print("Queue is empty!")
        return 0
    else:
        return queue[0]




def Display(queue):
    if queue==[]:
        print("Queue is empty")
        return 0
    elif len(queue)==1:
        print(queue[0],"<------Front-end, Rear-end")
    else:
        front=0
        rear=len(queue)-1
        print(queue[front],"<------Front-end")
        for i in range(1,rear):
            print(queue[i])
        print(queue[rear],"<------Rear-end")


def menu():
    queue=[]
    while True:
        print("==========================QUEUE MENU===========================")
        print(" 1) Enqueue")
        print(" 2) Dequeue")
        print(" 3) Peek")
        print(" 4) Display Queue")
        print(" 5) Exit")
        choice=input("Select [ 1/2/3/4/5 ]:")
        if choice=='1':
            Enqueue(queue)
            continue
        elif choice=='2':
            item=Dequeue(queue)
            if item==0:
                continue
            else:
                print("Dequeue-ed item is:", item)
            continue
        elif choice=='3':
            item=Peek(queue)
            if item==0:
                continue
            else:
                print("Front-end item id:", item)
                continue
        elif choice=='4':
            item=Display(queue)
            if item==0:
                continue
            continue
        elif choice=='5':
            break
        else:
            print("INVALID COMMAND")

#main
front = None
menu()












