class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1, 2]:
            return 0

        isPrime = [True] * n

        count = 1
        for i in range(3, n, 2):
            if not isPrime[i]:
                continue
            count += 1
            k = i + i
            while k < n:
                isPrime[k] = False
                k += i

        return count
