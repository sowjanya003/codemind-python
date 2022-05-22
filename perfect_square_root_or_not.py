n=int(input())
c=0
for i in range(1,n):
    if(i*i==n):
        print('True')
        c=1
        break
if(c==0):
    print('False')