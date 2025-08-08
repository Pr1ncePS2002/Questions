class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:
        seen=set()
        l,maxsum,window_sum=0,0,0
        for r in range(len(nums)):
            while len(seen)==k or nums[r] in seen: #check if window size is maintained and the 
                                                # element is already not in hashset
                window_sum-=nums[l]
                seen.remove(nums[l])   #remove the element from set and move the pointer
                l+=1
            window_sum+=nums[r]  #update the sum with adding the right element
            seen.add(nums[r]) #add the item to updated set
            if len(seen)==k:
                maxsum=max(maxsum,window_sum)
        return maxsum



                