def q(s):
    s=s.split()
    return(s[2])

def p(s):
    s=s.split()
    return(int(s[3]))

def q(s):
    s=s.split()
    return(s[4])

f=open(r"C:\Users\Samridh Girdhar\Documents\Python files\student.txt","r+").readlines()
x=input("enter question part letter: ") 
while True
    if x=="a": 
        l=[]
        for i in f:
            l.append(tuple(i.split()))      #a
    elif x=="b":
        f.sort(key=q)
        print(f)                            #b.1

        for i in f:                         #b.2
            if p(i)<3:
                print(i)
            else:
                continue
        d={}
        for i in f:                         #b.3
            if q(i) not in d:
                d[q(i)]=1
            else:
                d[q(i)]+=1
        print(d)
    else:
        print("enter valid letter! \n(a,b,c...)")
    if (input("do you want to quit?(Y/N) : ")=="Y"):
            break
        else:
            continue
