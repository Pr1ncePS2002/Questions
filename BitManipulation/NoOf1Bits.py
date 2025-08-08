def onebits(n):
    count=0
    while n:
        count+=1 if n&1 else 0
        n>>=1
    return count

print(onebits(0b0011000110010))