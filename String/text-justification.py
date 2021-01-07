class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append( cur[0] + ' '*(maxWidth - num_of_letters) )
                else:
                    num_spaces = maxWidth - num_of_letters
                    space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1)
                    for i in range(num_extra_spaces):
                        cur[i] += ' '
                    res.append( (' '*space_between_words).join(cur) )
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
            
        """
        This is for those cases when we never enter the if in the for loop
        """
        res.append( ' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1) )
        return res      
