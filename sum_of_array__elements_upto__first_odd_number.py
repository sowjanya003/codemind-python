n=int(input())
l=list(map(int,input().split()))
a=[]

for i in l:
    if i%2!=0:
        break
    else:
        a.append(i)
print(sum(a))
