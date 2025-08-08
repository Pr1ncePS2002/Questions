class Solution:
    def pivotIndex(self, nums) -> int:
        total=0
        for num in nums:
            total+=num          #take total sum
        leftsum=0
        for i in range(len(nums)):
            rightsum=total-nums[i]-leftsum     #generate right sum by excluding the current element
            if rightsum==leftsum:    #if both sum are equal return the index 
                return i
            leftsum+=nums[i]
        return -1
    
''' [1,3,7,6,5,6]=  leftsum =[1,4,11,"17",22,28]
                    rightsum=[28,27,24,"17",11,6]
    since 17 is at same index and equal then that is pivot index                  '''