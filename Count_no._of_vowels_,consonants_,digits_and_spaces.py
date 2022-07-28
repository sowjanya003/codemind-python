n=input()
l=list(n)
v='AEIOUaeiou'
num='0123456789'
sp=' '
cv=0
cn=0
cs=0
cc=0
for i in l:
    if i in v:
        cv+=1
    elif i in num:
        cn+=1
    elif i in sp:
        cs+=1
    else:
        cc+=1
print('Vowels:',cv)
print('Consonants:',cc)
print('Digits:',cn)
print('White spaces:',cs)
