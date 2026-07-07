class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # for i in range(1,len(arr) - 1):
        #     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        #         return i
# brute force
# traverse the array from second element to second last element
# compare current element with left neighbour
# compare current element with right neighbour
# if current element is greater than both
# return current index
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid+1]:
                start = mid+1
            else:
                end = mid - 1
        return start
        