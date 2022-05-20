def isHappyNumber(n):
    rem =0
    sum = 0
    while(n>0):
        rem = n%10
        sum = sum + (rem*rem)
        n = n//10
    return sum  
n = int(input( )) 
result = n   
while(result != 1 and result != 4):
    result = isHappyNumber(result)
    if(result == 1):
        print("True")
        break
    elif(result==4):
        print("False")
        break