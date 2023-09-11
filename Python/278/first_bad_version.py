def isBadVersion(version: int) -> bool:
    return version == 1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        head = 0
        tail = n
        while True:
            now = (tail + head) // 2
            nv = isBadVersion(now)
            pre = isBadVersion(now-1)
            if nv != pre:
                return now
            if tail == head+1:
                return tail
            if nv:
                tail = now
            else:
                head = now
            
    
if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(1))
    