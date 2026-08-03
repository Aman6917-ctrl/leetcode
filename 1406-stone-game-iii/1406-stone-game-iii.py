class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # State variables representing dp[i+1], dp[i+2], dp[i+3]
        next1, next2, next3 = 0, 0, 0
        
        # Traverse backwards from the end of the array
        for i in range(n - 1, -1, -1):
            # Option 1: Take 1 stone
            ans = stoneValue[i] - next1
            
            # Option 2: Take 2 stones
            if i + 1 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i+1] - next2)
                
            # Option 3: Take 3 stones
            if i + 2 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - next3)
            
            # Move state variables one step left
            next3 = next2
            next2 = next1
            next1 = ans
            
        # next1 now contains the relative score difference for Alice at index 0
        if next1 > 0:
            return "Alice"
        elif next1 < 0:
            return "Bob"
        else:
            return "Tie"