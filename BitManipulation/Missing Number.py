class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum1=0
        # x=len(nums)
        # total=x*(x+1)//2
        # for i in nums:
        #     sum1+=i
        # return total-sum1

        # res=len(nums)
        # for i in range(len(nums)):
        #     res+= i-nums[i]
        # return res

        missing=0
        for num in nums:
            missing^=num
        for i in range(len(nums)+1):
            missing^=i
        return missing
        
