class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # WHEN doing a wrap around you need to go from B - A
        # Also A - B means how many steps do you need to go from B to reach A
        
        order_dict = defaultdict(list)
        for i, w in enumerate(strings):
            order = []
            for j in range(1, len(w)):
                tmp = (ord(w[j]) - ord(w[j - 1])) % 26
                order.append(tmp)
            # to hash a list we can map it to a string
            order_dict[str(order)].append(w)


        return list(order_dict.values())
