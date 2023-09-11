from math import ceil

class Solution:
    def mincostTickets(self, days: list, costs: list) -> int:
        # 計算票價划算點
        gate = [costs[1]//costs[0]+1,costs[2]//costs[1]*7+1]
        counter = [0, 0, 0]
        head, tail, headidx, tailidx = 0, 0, 0, 0
        while True:
            if days[tailidx] - days[headidx] >= 30 or tailidx == len(days) - 1:
                tailidx -= 1
                days = tailidx - headidx
                if days > gate[2]:
                    counter[2] += 1
                elif days > gate[1]:
                    counter[1] += ceil((days) / 7)
                else:
                    counter[0] += days
            tailidx += 1
        print(gate)
        
s = Solution()
s.mincostTickets([1,2,3],[2,7,15])