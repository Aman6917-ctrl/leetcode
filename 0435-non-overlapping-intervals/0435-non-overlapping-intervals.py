class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If the current interval starts before the previous one ends, it overlaps
            if intervals[i][0] < prev_end:
                count += 1
            else:
                # Otherwise, update the end time to the current interval's end
                prev_end = intervals[i][1]
                
        return count