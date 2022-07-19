n=input().lower().split()
c=0
for i in n:
    l=i[::-1]
    if i==l:
        c+=1
print(c)