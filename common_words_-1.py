s1=input().lower().split()
s2=input().lower().split()
c=0
for i in s2:
    for j in s1:
        if i==j:
            c+=1
print(c)