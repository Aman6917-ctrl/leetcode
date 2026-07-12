class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        copy_arr = sorted(set(arr))

        rank_map = {}

        for i in range(len(copy_arr)):
            rank_map[copy_arr[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = rank_map[arr[i]]

        return arr
        # make a copy of array

# remove duplicates from copied array

# sort the copied array

# traverse original array

# for every element search it in sorted unique array

# rank will be index + 1

# replace/store the rank

        