class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0,i+1] for i in range(300)]
        return

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        # ts = 301 means (301-1)%300
        idx = int((timestamp - 1)%300)
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][0] = 1            
            self.counter[idx][1] = timestamp            

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        cnt = 0
        for x in self.counter:
            c,t = x[0],x[1]
            if timestamp - t < 300:
                cnt += c
        return cnt
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
