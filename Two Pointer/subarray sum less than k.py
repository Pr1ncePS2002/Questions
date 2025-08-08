class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        res=0
        l=0
        prod=1
        for i in range(len(nums)):
            prod*=nums[i]
            while l<=i and prod>=k:
                prod=prod//nums[l]
                l+=1
            res+=(i-l+1)
        return res