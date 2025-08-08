class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        prefix={0:1}
        cur_sum=0
        count=0
        for num in nums:
            cur_sum+=num    #get the total sum
            if cur_sum-goal in prefix:  #subtract the goal if present in dict
                count+=prefix[cur_sum-goal]   #increase the count of subtracted value
            if cur_sum in prefix:       #since subtracted value is there with count 3
                prefix[cur_sum]+=1  #then no of subarrays with goal will be there as well
            else:                    
                prefix[cur_sum]=1
        return count