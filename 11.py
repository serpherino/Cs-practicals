def bubbleSort(list): 
    efficiency=0
    n=len(list) 
    for i in range(n-1):  
        for j in range(n-i-1): 
            if list[j]>list[j+1]: 
                list[j],list[j+1]=list[j+1],list[j]
                efficiency+=1
    return list, efficiency

a,b=bubbleSort(list(map(int,input("enter list : ").split())))
print("sorted list : ",a)
print("efficiency :  ",b)