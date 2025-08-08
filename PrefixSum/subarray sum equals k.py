class Solution:
    def subarraySum(self, nums, k: int) -> int:
        new_dict={0:1}
        sum1=0
        count=0
        for num in nums:
            sum1+=num

            if sum1-k in new_dict:
                count+=new_dict[sum1-k]      #total - target element is present in the dictionary or not
            if sum1 in new_dict:          #if there increment the subarray count
                new_dict[sum1]+=1
            else:
                new_dict[sum1]=1
        return count
            

        