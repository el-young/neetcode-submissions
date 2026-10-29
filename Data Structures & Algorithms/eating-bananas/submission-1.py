import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def runSim(eatingRate, hoursRemaining):
            for pile in piles:
                hoursRemaining -= math.ceil(pile / eatingRate)
                if hoursRemaining < 0: return False

            return True
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if not runSim(mid, h):
                lo = mid + 1
            else:
                hi = mid
        
        return lo
