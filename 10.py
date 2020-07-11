def f():
    n=int(input("enter number : "))
    c=input("enter conversion : \nB : binary\nO : octal\nH : hexadecimal\n")
    if c=="B":
        print(bin(n))
    elif c=="O":
        print(oct(n))
    elif c=="H":
        print(hex(n))
    else:
        print("enter valid option!")
while True:
    f()
    if (input("do you want to quit?(Y/N) : ")=="Y"):
        break
    else:
        continue