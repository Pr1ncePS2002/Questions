def bin2dec(s:str):
    res=0
    p=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='1':
            res+=2**p
        p+=1
    return res
s='1011'
print(bin2dec(s))
            