class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=qW1O1a40-No&t=360s
        
        THIS IS BASICALLY A VERSION OF LIS IN 2D 
        
        SO WHEN EVER YOU HEAR THE WORD
        1. INCREASING YOU CAN THINK OF BINARY
        2. WHEN EVER YOU THINK OF LONGEST YOU CAN THINK OF DP
        
        SO THE PROBLEM IS TO SOLVE THIS IN NLOGN TIME USING BS + DO
        
        REFER THE VIDEO ABOVE 
        
        1. SO THE BASIC IDEA IS 5 , 3 ARE COMEPTING THEN STORE 3 AFTER 2 AS IT HAS BETTER CHACES OF GIVING YOU THE LIS
        AND IT ALSO DOES NOT DECREASE THE LENGTH


        """
        
        """
        here we want 7 to come before 4 so we have changed the definitation as sort is always in inreasing order
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        def lis(nums):
            
            # This is just to store the length and not the actual numbers
            dp = []
            
            for i in range(len(nums)):
                
                """
                so what bisect left gives you the index of the first number that is equal to or greater than x and that is what we want

                """
                
                
                idx = bisect_left(dp, nums[i])
                # That means that is no such number
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([i[1] for i in envelopes])
