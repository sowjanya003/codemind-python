n=input()
l=list(n)
num='0123456789'
l1=[]
for i in l:
    if i in num:
        l1.append(int(i))
print(sum(l1))