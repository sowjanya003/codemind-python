n=input()
l=list(n)
num='0123456789'
l1=[]
s=0
for i in l:
    if i in num:
        l1.append(i)
for i in l1:
    i=int(i)
    s+=i
print(s)
        
        