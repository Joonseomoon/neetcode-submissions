class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0] * 26

        for c in s1:
            count[ord(c) - ord("a")] += 1
        
        l = 0
        for r in range(len(s2)):
            count[ord(s2[r]) - ord("a")] -= 1  

            if (r - l + 1) > len(s1):
                count[ord(s2[l]) - ord("a")] += 1
                l += 1

            if not any(count):
                return True
            
        return False