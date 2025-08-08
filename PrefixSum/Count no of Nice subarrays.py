class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        count,odd_count=0,0
        prefix={0:1}
        for num in nums:
            if num%2==1:    #iff no is odd add it to odd count
                odd_count+=1
            if odd_count-k in prefix:     #if odd count - target is in dicitonary
                count+=prefix[odd_count-k]     #increment the count same as subarray question
            
            if odd_count in prefix:
                prefix[odd_count]+=1       #same logic as subarray sum equals k
            else:
                prefix[odd_count]=1
        return count