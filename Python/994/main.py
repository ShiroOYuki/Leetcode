class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        openset = []
        closeset = []
        steps = 0
        orange = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    closeset.append((i,j))
                elif grid[i][j] == 2:
                    openset.append((i,j))
                else:
                    orange += 1
                    
        while openset:
            now = openset[0]
            closeset.append(now)
            openset.pop(0)
            old_len = len(openset)
            
            y,x = now[0],now[1]
            if y-1 > -1 and (y-1,x) not in closeset:
                openset.append((y-1,x))
            if y+1 < 3 and (y+1,x) not in closeset:
                openset.append((y+1,x))
            if x-1 > -1 and (y,x-1) not in closeset:
                openset.append((y,x-1))
            if x+1 < 3 and (y,x+1) not in closeset:
                openset.append((y,x+1))
            if len(openset) > old_len:
                steps+=1
        
        if orange > steps:
            return -1
        return steps
        
        