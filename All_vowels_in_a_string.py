n=input()
v='aeiou'
l=[]
for i in v:
    if i in v and i in n:
        l.append(i)
        #print(l)
if len(l)==len(v):
    print(True)
else:
    print(False)