w=open(r"C:\Users\Samridh Girdhar\Documents\Python files\file.md", "r+").read().split()
f=open(r"C:\Users\Samridh Girdhar\Documents\Python files\file2.md","w")
for i in w:
    if i[0].lower() not in "aeiou":
        f.write(i+" ")
    else:
        continue