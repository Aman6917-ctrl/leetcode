class Solution:
    def isValid(self, s: str) -> bool:
        # Map to keep track of matching pairs
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty; otherwise, use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top element
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were correctly matched and closed
        return not stack