class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        n=len(nums)
        w_sum=0
        for i in range(k):
            w_sum+=nums[i]   #add sum till the window size
        max_sum=w_sum  #set it to max sum
        for i in range(k,n):  #iterate from the kth index now 
            w_sum=w_sum-nums[i-k]+nums[i]  #remove the left element from window sum 
            if w_sum>max_sum:    #add right element
                max_sum=w_sum  #if window sum is greater than max sum
        return max_sum/k  #find the avg 