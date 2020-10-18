class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(numbers) - 1
        
        while low <= high:
            
            a = numbers[low]
            b = numbers[high]
            two_sum = a + b
            if two_sum > target:
                high -= 1
                
            elif two_sum < target:
                low += 1
            else:
                return [low + 1, high + 1]
            
        return []
