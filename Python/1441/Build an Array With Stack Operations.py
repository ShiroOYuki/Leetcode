class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ansPT = -1
        stackPT = -1
        stack = [None]*n
        res = []
        for i in range(n):
            stackPT += 1
            ansPT += 1
            stack[stackPT] = i+1
            res.append("Push")
            print(stack, target, stackPT, ansPT)
            if ansPT+1 == len(target) and stack[stackPT] == target[ansPT]:
                break
            if ansPT+1 == len(target) or stack[stackPT] != target[ansPT]:
                stack[stackPT] = None
                stackPT -= 1
                ansPT -= 1
                res.append("Pop")
        return res
    
print(Solution().buildArray([1,2], 3))