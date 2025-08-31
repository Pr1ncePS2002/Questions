class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        goal=n-1
        for i in range(n-2,-1,-1):   # traverse backward and check if from which index we can reach end
            if i+ nums[i]>=goal:
                goal =i
        return goal==0

        
