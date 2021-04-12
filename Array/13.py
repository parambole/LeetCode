class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        dic = {"I":             1,
                "V"    :         5,
                "X"    :         10,
                "L"    :        50,
                "C"    :         100,
                "D"     :        500,
                "M"     :        1000}
        
        
        # Better Approach:
        
        last_sum = dic[s[-1]]
        
        for i in range(len(s) - 2, -1, -1):
            if dic[s[i]] < dic[s[i + 1]]:
                last_sum -= dic[s[i]]
            else:
                last_sum += dic[s[i]]
                
        return last_sum
        
#         n = len(s)
        
#         if n < 1:
#             return 0
#         if n < 2:
#             return dic[s[0]]
        
#         final_sum = 0
#         for i in range(n - 1):
#             if dic[s[i]] < dic[s[i + 1]]:
#                 final_sum -= dic[s[i]]
                
#             else:
#                 final_sum += dic[s[i]]
                
#         final_sum += dic[s[i+1]]
#         return final_sum
            
