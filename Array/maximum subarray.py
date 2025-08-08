class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either start a new subarray at nums[i], or extend the current one
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum