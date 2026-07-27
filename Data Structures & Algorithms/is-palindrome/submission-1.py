class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Values of the str without space 
        # Make the array non alphanumeric 
        new_str = "".join([ch for ch in s if ch.isalnum()]).lower()
        rev = new_str[::-1]
        return True if rev == new_str else False