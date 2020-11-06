class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        "nums = [1,2,5,9], threshold = 6"
        
        """
        1. Find the upper limit
        2. lower limit is 1
        3. BS by choosing number between the lower and upper limit
        4. if the sum > Threshold then increase the divisor 
        5. if sum < Threshold then decrease the divisor
        6. Keep increasing the divisor till you get the max divisor
        """
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        left, right = 1, nums[-1]
        ans = 0
        while left <= right:
            pivot = (right + left) >> 1
            divSum = compute_sum(pivot)
            if divSum > threshold:
                left = pivot + 1
            else:
                ans = pivot
                right = pivot - 1
        return ans
        
