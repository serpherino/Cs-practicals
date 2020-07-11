def count(n):
    return len(n)
def reverse(n):
    return int(n[::-1])
def hasdigit(n):
    if n.isdigit():
        return True
    else:
        return False
def show(n):
    for i in range(len(n)):
        if i!=(len(n)-1):
            print(int(n[i])*10**(len(n)-i-1),end=" + ")
        else:
            print(int(n[i])*10**(len(n)-i-1))
while True:
    y=input("\n\n\nenter \n1 for count()\n2 for reverse()\n3 for hasdigit()\n4 for show()\n")
    x=input("enter the number : ")
    if y=="1":
        print("count : ",count(x))
    elif y=="2":
        print("reverse : ",reverse(x))
    elif y=="3":
        print("hasdigit : ",hasdigit(x))
    elif y=="4":
        print("show : ",end="")
        show(x)
    else:
        print("enter valid number!")
    if (input("do you want to quit?(Y/N) : ")=="Y"):
        break
    else:
        pass
