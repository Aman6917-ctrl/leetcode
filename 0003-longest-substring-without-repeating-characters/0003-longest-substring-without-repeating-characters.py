class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # If the character is a duplicate and is inside the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer past the previous occurrence
                left = char_map[s[right]] + 1
            
            # Record/Update the index of the current character
            char_map[s[right]] = right
            
            # Calculate the window size and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len
