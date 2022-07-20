n=list(map(str,input().split()))
m=min(n[-1])
p=m.lower()
if m and p in n[-1]:
    print(p)
else:
    print(m)

