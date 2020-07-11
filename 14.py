queue=[]
def enqueue(element):
    queue.append(element)
def dequeue():
    try:
        return queue.pop(0)
    except:
        return None
def peep():
    try:    
        return queue[0]
    except:
        return None
def inputmember():
    return list(map(str,input("reg_no, Name,admission_to_class (Nursery, KG, I) : ").split()))

for i in range(int(input("enter number of students : "))):
    enqueue(inputmember())

print("total children : ",len(queue))

Nursery=[]
kg=[]
I=[]
for j in queue:
    if j[2]=="Nursery":
        Nursery.append(j)
    elif j[2]=="KG":
        kg.append(j)
    elif j[2]=="I":
        I.append(j)
print("nursery kids : ",Nursery)
print("kg kids : ", kg)
print("I kids : ",I)