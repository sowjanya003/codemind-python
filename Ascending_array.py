n=int(input())
l=list(map(int,input().split()))
t=[]
c=0
for i in range(len(l)-1):
    if l[i]>=l[i+1]:
        c+=1
if c==0:
    print('yes')
else:
    print('no')