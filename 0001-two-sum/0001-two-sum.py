class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # first we will loop the input array
        # now we will take first element of the input array
        # and store it 
        # now we will loop 2 nd timefor fetting 2 nd elemnt in loop we use i+1
        # and add 1 st element with the 2 element of the array
        # if the addition of 1 st and 2 nd == to target we will return the index of that both element
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i+1,len(nums)):
                next_element = nums[j]
                sum = current + next_element
                if sum == target:
                    return[i,j]
       

            
        