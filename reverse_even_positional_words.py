n=input()
l=n.split()
for i in range(len(l)):
    if i%2==0:
        e=str(l[i])
        print(e[::-1],end=' ')
    else:
        e=str(l[i])
        print(e,end=' ')