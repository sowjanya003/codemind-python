def pl(n):
    p=n.lower()
    l=p[::-1]
    if p==l:
        return True
    else:
        return False
n=input()
print(pl(n))
