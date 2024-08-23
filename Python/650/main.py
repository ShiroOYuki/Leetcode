class Solution:
    def minSteps(self, n: int) -> int:
        return max(0, self._copy(n, 1, 0)) 

    def _copy(self, n: int, now: int, step: int):
        if now == n: return -1
        step += 1
        copied = now
        p = self._paste(n, copied, now, step)
        return p
        
    def _paste(self, n:int, copied: int, now: int, step: int):
        if now > n: return -1
        if now == n: return step
        
        step += 1
        now += copied
        
        c = self._copy(n, now, step)
        p = self._paste(n, copied, now, step)
        s = max([c, p]) if c == -1 or p == -1 else min([c, p])
        
        return s