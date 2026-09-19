class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Find the rightmost position i where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no such position exists, reverse entire array
        if i == -1:
            nums.reverse()
            return
        
        # Find rightmost position j where nums[j] > nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the suffix starting at nums[i+1]
        nums[i + 1:] = reversed(nums[i + 1:])