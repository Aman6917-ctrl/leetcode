from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0

        # Build prefixGcd
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))
        prefixGcd.sort()
        left = 0
        right = len(prefixGcd) - 1
        ans = 0

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans
#1. Create a new array prefixGcd.
#2. Traverse the array from index 0 to n-1.
#3. For every index i, iterate from index 0 to i to find the maximum element.
#4. Compute gcd(nums[i], maximum) and store it in prefixGcd.
#5. Sort prefixGcd.
#6. Pair the smallest and largest elements, compute their GCD, and add it to the answer.
#7. Ignore the middle element if the array size is odd.
8#. Return the final answer.
       
        