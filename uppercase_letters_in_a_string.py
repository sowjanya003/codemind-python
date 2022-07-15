n=input()
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=0
for i in n:
    if i in A:
        c+=1
print(c)