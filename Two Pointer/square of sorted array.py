class Solution:
    def sortedSquares(self, nums) :
        # return sorted(num**2 for num in nums)
        result=[]
        l,r=0,len(nums)-1
        p=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                result.append(nums[l]**2)
                l+=1
            else:
                result.append(nums[r]**2)
                r-=1
            p-=1
        result.reverse()
        return result
