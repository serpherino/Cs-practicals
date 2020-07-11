def generatefactors(n):
    l=[]
    s=int(n**0.5)+1
    for i in range(s,0,-1):
        if n%i==0:
            l.append(i)
            n=n//i
            
    return l
def prime(n):
    if n==1:
        return False
    if len(generatefactors(n))==1:
        return True
    else:
        return False
def perfectno(n):
    s=0
    for i in (generatefactors(n)):
        s+=i
    if s==n:
        return True
    else:
        False
while True:
    print("1 : generate factors\n2 : prime\n3 : perfectno")
    n=int(input("enter your choice : "))
    x=int(input("enter the number : "))
    if n==1:
        print("factors : ",generatefactors(x))
    elif n==2:
        print("prime : ",prime(x))
    elif n==3:
        print("perfect number : ",perfectno(x))
    else:
        print("enter valid number")
    if (input("do you want to quit?(Y/N) : ")=="Y"):
        break
    else:
        pass
