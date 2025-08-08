class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        l,cursum=0,0
        minlen= float('inf')
        for r in range(len(nums)):
            cursum+=nums[r]    #adding next element to current sum
            while cursum>=target: #loop till current sum is greater than target
                if r-l+1<minlen:  #if the current window size is smaller than minlen
                    minlen=r-l+1  #update minlen
                cursum-=nums[l]   #else remove value of left element and move the left pointer right
                l+=1
        return 0 if minlen==float('inf') else minlen