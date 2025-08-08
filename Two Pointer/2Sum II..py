class Solution:
    def twoSum(self, nums,target) :
        left,right=0,len(nums)-1
        while left<right:
            cur_sum=nums[left]+nums[right]
            if cur_sum==target:
                return [left+1,right+1]
            elif cur_sum<target:
                left+=1
            else:
                right-=1
