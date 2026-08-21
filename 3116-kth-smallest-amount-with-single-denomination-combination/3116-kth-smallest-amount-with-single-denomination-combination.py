import math
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            total = 0
            m = len(coins)

            for mask in range(1,1<<m):
                lcm = 1
                bits = 0

                for i in range(m):
                    if mask & (1 << i):
                        bits+=1
                        lcm = lcm * coins[i] // math.gcd(lcm, coins[i])
                        if lcm > x:
                            break
                if lcm > x:
                    continue
                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x//lcm
            return total
        low = min(coins)
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
        

        

        