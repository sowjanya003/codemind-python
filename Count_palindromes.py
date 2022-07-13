n=int(input())
a=list(map(int,input().split()))
b=[]
p=0
for i in a:
    k=i
    c=0
    while(k>0):
        #Reminder = temp % 10
        c=(c*10)+(k%10)
        k=k//10
    if(i==c):
        b.append(i)
        p+=1
print(p)