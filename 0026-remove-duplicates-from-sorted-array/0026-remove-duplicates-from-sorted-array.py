class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = sorted(set(nums))
        index = 0
        for num in st:
            nums[index] = num
            index+=1
        return index
        