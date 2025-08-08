class Solution:
    def majorityElement(self, nums) -> int:
        count={}
        n=len(nums)
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num, count in count.items():
            if count > n // 2:
                return num
                
               
    ''' count = 0
		candidate = None
		    
		#For better space complexity 
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

            return candidate'''