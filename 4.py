z=open(r"C:\Users\Samridh Girdhar\Documents\Python files\f.asc","r+").read().split()
d,c1,c2,d2={},0,0,{}
for i in z:
    i=i.lower()
    if i.isalnum():
        c1+=1
        if i not in d.keys():
            d[i]=1
            c2+=1
        else:
            d[i]+=1
def b(key):
    return d[key]
print("total number of words are : {} and\ntotal unique words are : {}".format(c1,c2))
s = sorted(d.items(), key=lambda x: x[1], reverse=True)
print("\nwords arranged by decreasing frequency:  \n")
for i in s:
    print(i)
for i in z:
    if i[-1]!=".":
        l=len(i)
    else:
        l=len(i)-1
    if l not in d2.keys():
        d2[l]=[i]
    else:
        d2[l].append(i)
print("\n")
def find_longest_word(x):
    v=0
    for i in sorted(x.keys(),reverse=True):
        if v==0: 
            print(i,x[i],"----------------------------------> LONGEST WORDS")
            v=1
        else:
            print(i,x[i])
find_longest_word(d2)
def filter_long_words(d) :
    n=int(input("\nenter length n : "))
    f=sorted(d.keys())
    print("\n\nlists of words with length larger than or equal to ,",n)
    for i in f:
        if i<=n:
            print(d[i])
filter_long_words(d2)
  

