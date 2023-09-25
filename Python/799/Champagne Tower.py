class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 倒 poured 杯香檳
        # 共有 query_row 層
        # 求最後一層的第 query_glass 杯
        # 0 <= query_glass <= query_row < 100
        query_row += 1
        tower = list(list(0 for _ in range(query_row+1)) for __ in range(2))
        tower[0][0] = poured
        for i in range(1, query_row):
            for j in range(i):
                if tower[0][j] >= 1: # 溢出
                    tower[0][j] -= 1 # 實際溢出量
                    tower[1][j] += tower[0][j] / 2
                    tower[1][j+1] += tower[0][j] / 2
            tower[0] = tower[1]
            tower[1] = list(0 for _ in range(query_row+1))
        return min(1, tower[0][query_glass])
        
print(Solution().champagneTower(25, 6, 1))