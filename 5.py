import pickle
f=open(r"C:\Users\Samridh Girdhar\Documents\Python files\hotel.dat","rb+")

def recordcustomer():
    r={}
    r["room.No"]=input("\nenter room no : ")
    r["Name"]=input("enter name of customer : ")
    r["duration"]=input("enter duration: ")
    return r
for i in range(int(input("enter number of records to load : "))):           #(i)
    pickle.dump(recordcustomer(),f)
f.seek(0)
c=0
while True:                                                                 #(ii)
    try:
        print(pickle.load(f))
        c+=1
    except:
        print("\n               \\ \\REACHED EOF\\ \\")
        break
print("\n\ntotal customers : ", c)                                          #(iii)
f.seek(0)
print("displaying those who have stayed for more than 2 days")              #(iv)
while True:
    try:
        x=pickle.load(f)
        if int(x["duration"])>2:
            print(x)
    except:
        break


