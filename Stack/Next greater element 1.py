class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater_map = {}

        # Step 1: Loop through nums2 and build the map
        for num in nums2:
            # Pop all elements from stack smaller than current num
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater_map[prev] = num
            stack.append(num)

        # Step 2: For all elements left in the stack, no greater element exists
        while stack:
            next_greater_map[stack.pop()] = -1

        # Step 3: Build result for nums1 using the map
        result = []
        for num in nums1:
            result.append(next_greater_map[num])

        return result