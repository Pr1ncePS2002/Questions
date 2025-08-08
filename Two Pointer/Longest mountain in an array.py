class Solution:
    def longestMountain(self, arr) -> int:
        peak={}
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]> arr[i+1]:
                peak[i]=arr[i]
        l,r,val=0,0,0
        for i,j in peak.items():
            l=i-1
            while l>0 and arr[l-1]<arr[l]:
                l-=1
            r=i+1
            while r<len(arr)-1 and arr[r]>arr[r+1]:
                r+=1
            val=max(val,r-l+1) 
        return val