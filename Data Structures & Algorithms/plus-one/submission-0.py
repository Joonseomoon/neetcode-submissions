class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) - 1, -1, -1):
            cur = digits[i]
            cur += 1
            if cur < 10:
                digits[i] = cur
                break
            else: 
                digits[i] = cur - 10
        
        if not digits[0]:
            digits = [1] + digits
        
        return digits