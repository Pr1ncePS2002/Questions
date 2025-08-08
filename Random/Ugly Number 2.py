def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        i2=i3=i5=0
        for x in range(1,n):
            next2,next3,next5=ugly[i2]*2,ugly[i3]*3,ugly[i5]*5
            next_num=min(next2,next3,next5)
            ugly.append(next_num)
            if next_num==next2:
                i2+=1
            if next_num==next3:
                i3+=1
            if next_num==next5:
                i5+=1
        return ugly[-1]