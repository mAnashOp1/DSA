from typing import List
class Solution:
    def getOperations(self, n: int) -> int:
        if n <= 0:
            return 0
        res, ops = 0, 0
        powerOfFour = 1

        while powerOfFour <= n:
            l = powerOfFour
            r = min(n, powerOfFour * 4 - 1)
            ops += 1
            res += (r - l + 1) * ops
            powerOfFour *= 4
        
        return res

    def minOperations(self, queries: List[List[int]]) -> int:
        total = 0
        for l,r in queries:
            total += (self.getOperations(r) - self.getOperations(l - 1) + 1) // 2
        return total