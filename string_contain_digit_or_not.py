n=input()
l=list(n)
num='0123456789'
l1=[]
for i in l:
    if i in num:
        l1.append(i)
n1=len(l1)
if n1==0:
    print("Doesn't contain digit")
else:
   print("Contains",n1,"digit")