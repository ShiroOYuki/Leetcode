class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        res = []
        n = 0
        group = [-1]*max(groupSizes)
        for i in range(len(groupSizes)):
            if group[groupSizes[i]-1] == -1 or len(res[group[groupSizes[i]-1]]) >= groupSizes[i]:
                group[groupSizes[i]-1] = n
                n += 1
                res.append([i])
            else:
                res[group[groupSizes[i]-1]].append(i)
        return res

print(Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3]))