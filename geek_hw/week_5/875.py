class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed: int) -> bool:
            return sum([ceil(p / speed) for p in piles]) <= h

        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid) == True:
                right = mid
            else:
                left = mid + 1
        return left

