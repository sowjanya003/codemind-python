def psq(n):
    s=int(n**0.5)
    if s*s==n:
        return True
    else:
        return False
        
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if psq(i):
        l1.append(i)
print(sum(l1))