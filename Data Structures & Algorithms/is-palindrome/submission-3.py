class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c.lower() for c in s if c.isalnum())
        for i in range(0, len(string) // 2 , 1):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True