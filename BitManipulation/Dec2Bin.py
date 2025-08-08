def dec2bin(n):
    res=""
    if n==0:
        return '0'
    while n>0:
        res=str(n%2)+res
        n=n//2
        
    return res

print(dec2bin(5))



        
    