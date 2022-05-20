n=int(input())
l=len(str(n))
sqr=n**2
ld=sqr%pow(10,l)
if ld==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")