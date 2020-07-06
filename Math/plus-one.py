class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        summation = 1
        for i in range(1, len(digits) + 1):
            summation += digits[-i]
            digits[-i] = summation % 10
            summation //= 10
        if summation > 0:
            digits.insert(0, summation)
        return digits
