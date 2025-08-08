class Solution:
    def maxArea(self, height) -> int:
        n=len(height)
        l,r=0,n-1
        max_area=0

        while l<r:
            w=r-l  #width is difference bw both pointers
            h=min(height[l],height[r])  #minimum height is stored for area calculation
            a=w*h
            max_area=max(max_area,a)

            if height[l]<height[r]: #if height of left pillar is small, move it right else move the right pointer
                l+=1
            else:
                r-=1
        return max_area
        