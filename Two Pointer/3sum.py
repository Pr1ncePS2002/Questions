class Solution:
    def threeSum(self, nums):
        list1=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                total=nums[i]+nums[r]+nums[l]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    list1.append([nums[i],nums[r],nums[l]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return list1

        