n=input()
l=n.split()
a=[]
for i in l:
    a.append(len(i))
print(max(a))