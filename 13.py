print("\t"*10,"RING DIAMETER GAME !\n\n")
while input("\nDO YOU WANT TO PLAY (Y/N) : ").upper()=="Y":
    ring_stand=[]
    spare_stand=[]
    def push(element):
        ring_stand.append(element)
    def pop():
        try:
            return ring_stand.pop()
        except:
            return None
    def peep():
        try:
            return ring_stand[-1]
        except:
            return None

    for i in range(int(input("Enter no. of rings : "))):
        new_ring=int(input("Enter ring {} diameter : ".format(i+1)))
        l=len(ring_stand)
        position=0
        for j in reversed(range(l)):
            if ring_stand[j]<new_ring:
                break
            else:
                position+=1
        for k in range(position):
            spare_stand.append(pop())
        push(new_ring)
        for h in range(position):
            push(spare_stand.pop())
    print()
    for i in reversed(ring_stand):
        print(i,end="")
        if i==len(ring_stand):
            print("\t~ring with largest diameter")
        elif i==1:
            print("\t~ring with smallest diameter")
        else:
            print()
else:
    print("\nTHANK YOU !\n~Crafted by Samridh Girdhar")