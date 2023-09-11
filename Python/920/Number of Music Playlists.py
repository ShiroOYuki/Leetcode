# Uncomplete

class tree:
    def __init__(self, val=None, child=[None]):
        self.val = val
        self.child = child


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        def search_tree(val: int, n: int, goal: int, mask: list, playlist: list):
            playlist[val-1] = False
            if goal == 0:
                if True in playlist:
                    return [False]
                return [None]
            if len(mask) > 0:
                mask.pop(0)
                mask.append(val)
            all_trees = []
            for i in range(1, n+1):
                if i not in mask:
                    child = search_tree(i, n, goal-1, mask.copy(), playlist.copy())
                    for c in child:
                        if c is not False:
                            node = tree(val)
                            node.child = c
                            all_trees.append(node)
            return all_trees
        mask = [None] * k
        cnt = 0
        for i in range(1, n+1):
            cnt += len(search_tree(i, n, goal, mask.copy(), [True]*n))
        return cnt
    
print(Solution().numMusicPlaylists(3, 3, 1))
        
                    
            
            
            