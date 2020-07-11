import csv
f=open(r"C:\Users\Samridh Girdhar\Documents\Python files\placement.csv","r+")
l=csv.reader(f)
l2=[]
cc=0
for i in l:
    if cc==0:
        cc=1
        continue
        
    else:
        l2.append(i)
l=l2
del l2
del cc
while True:

    f.seek(0)
    x=input("enter question part letter : ")
    if x=="a":
        for i in l:                         #a
            print(i)
        f.seek(0)
    elif x=="b":
        def total_a():                      #b
            c=0
            for i in l:
                c+=1
            return (c)
        print(total_a())
    elif x=="c":
        def toppers(n):                     #c
            f.seek(0)
            t={}
            for i in l:
                m=0
                for j in range(2,7):
                    m+=int(i[j])
                t[i[1]]=m
            q=sorted(t.items(),key=lambda x: x[1], reverse=True)
            for i in range(1,n+1):
                print(q[i-1])
        n=int(input("enter number of toppers required : "))
        toppers(n)
    else:
        print("enter valid letter! \n(a,b,c...)")
    if (input("do you want to quit?(Y/N) : ")=="Y"):
        break
    else:
        pass




            
