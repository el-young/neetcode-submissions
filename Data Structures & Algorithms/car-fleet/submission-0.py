class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - position[i]) / speed[i] for i in range(len(speed))]
        ls = sorted(zip(position, times), reverse=True)
        currT, numFleets = ls[0][1], 0
        for p, t in ls:
            if t > currT:
                numFleets += 1
                currT = t
        return numFleets + 1
        