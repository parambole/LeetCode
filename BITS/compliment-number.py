class Solution:
    
    # knew logic didn't know how to implement
    
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1
        
        # Do this todo 0
        while todo:
            
            num ^= bit
            
            # we need to shift 001 to 010 to 100
            bit <<= 1
            
            # This means we will do right shift
            todo >>= 1
            
        return num
