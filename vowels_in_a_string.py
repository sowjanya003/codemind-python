c=input()
v=input()
for i in range(len(c)):
    if v==c[i]:
        print('True')
        print(i)
        break
else:
    print('False')
    
    