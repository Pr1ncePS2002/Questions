class Solution:
    def removeElement(self, nums,val) -> int:
        k = 0  # Pointer for the new position

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
