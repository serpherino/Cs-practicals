f=open(r"C:\Users\Samridh Girdhar\Documents\Python files\q1.asc","w+")
f.write("Neither apple nor pine are in pineapple. Boxing rings are square.\nWriters write, but fingers don’t fing. Overlook and oversee are opposites.\nA house can burn up as it burns down. An alarm goes off by going on")
while True:
    f.seek(0)
    a=input("enter question part letter: ")
    if a=="a":
        for i in f.readlines():                         #a
            print(i)
    elif a=="b":
        f.seek(0,2)
        f.write("\nthis is the last line")              #b
    elif a=="c":
        f.seek(0)
        r=f.readlines()
        print(r[-1])                                    #c
    elif a=="d":
        f.seek(9,0)
        r=f.readline()
        print(r)                                        #d
    elif a=="e":
        f.seek(0)
        r=f.readlines()
        print(r[int(input("enter line number: "))-1])   #e
    elif a=="f":
        f.seek(0)
        r=f.read().split()
        d={}
        for i in r:
            i=i.lower()
            if i[0] not in d.keys():
                d[i[0]]=1
            else:
                d[i[0]]+=1
        for i in d.keys():
            print("words starting with {} appears {} times".format(i,d[i]))     #f
    else:
        print("enter valid letter! \n(a,b,c...)")
    v=5
    while v!="Y" or v!="N":
        v=input("do you want to quit? (Y/N)\nanswer in Y or N! : ")
        if v=="Y":
            break
        elif v=="N":
            break
    if v=="Y":
            break
        