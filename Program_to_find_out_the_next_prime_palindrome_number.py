def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True

def pal(n):
    if str(n)==str(n)[::-1]:
       return True
    else:
        return False
        

n=int(input())
n+=1
while True:
    if prime(n) and pal(n):
        print(n)
        break
    n+=1