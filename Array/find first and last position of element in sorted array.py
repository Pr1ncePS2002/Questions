def searchRange(nums, target):
    count=0
    lst=[-1,-1]
    for i in range(len(nums)):
        if nums[i]==target:
            if lst[0]==-1:
                lst[0]=i
            lst[1]=i
    return lst        
        
'''Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
Output: [3, 4] 
Explanation: The target 8 appears from index 3 to index 4.'''
