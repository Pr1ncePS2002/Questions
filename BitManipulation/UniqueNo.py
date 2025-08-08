def unique(x):
    res=0
    for i in x:
        res=res^i
    return res
x=[2,3,4,5,5,4,2]
print(unique(x))
