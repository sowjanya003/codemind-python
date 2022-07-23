def psq(n):
    s=int(n**0.5)
    if s*s==n:
        return True
    else:
        return False
        
n=int(input())
print(psq(n))
    