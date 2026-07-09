class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        window_sum = 0
        maxAvg = float('-inf')
        while j < len(nums):
            window_sum += nums[j]
            if j - i + 1 < k:
                j+= 1
            else:
                # j - i + 1 == k:
                current_avg = window_sum / k
                maxAvg = max(maxAvg,current_avg)
                window_sum -= nums[i]
                i+=1
                j+=1
        return maxAvg


        # initialixe max avg
        # traverse the array
        # generate every subaaray of size k
        # cal the sum of current sub array
        # cal avg
        # update max avg
        # return max avg
        # max_avg = 0
        # for i in range(len(nums) - k + 1):
        #     current_sum = 0
        #     for j in range(i,i+k):

        #         current_sum += nums[j]
        #     current_avg = current_sum / k
        #     max_avg = max(max_avg,current_avg)
        # return max_avg

            
        