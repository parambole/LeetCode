class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:        
        degreeFromMin = 0.5 * minutes
        degreeFromHour = hour % 12 * 30 + (degreeFromMin)
        
        val = abs(degreeFromHour - (minutes * 6))

        return min(val, 360 - val)
