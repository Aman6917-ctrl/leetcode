from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        start = 0
        end = len(nums) - 1

        while start < end:

            mid = start + (end - start) // 2

            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid

        return start
        

        # if len(nums) == 1:
        #     return 0
        # if nums[0] > nums[1]:
        #     return 0
        # for i in range(1, len(nums) - 1):
        #     if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        #         return i

        # if nums[len(nums) - 1] > nums[len(nums) - 2]:
        #     return len(nums) - 1
        # brute force

# if array has only one element

    # return 0

# check if first element is peak

# if yes

    # return 0

# traverse from second element to second last element

# compare current element with left and right neighbour

# if current element is greater than both

    # return its index

# check if last element is peak

# if yes

    # return last index
       
        