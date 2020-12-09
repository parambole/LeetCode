class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # The main logic is we need to add two remainders to make it to 60 so that their modulus is also divisible
        remainders = collections.defaultdict(int)
        result = 0
        for t in time:
            if t % 60 == 0:
                # So this will add all the pairs of numbers that eventually will be zero
                # This is good way of doing it other way could be nc2
                result += remainders[0]
                
            else:
                result += remainders[ 60 - ( t % 60) ]
                
            remainders[t % 60 ] += 1
            
        return result
