class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)


        while low <high:
            mid = (low+high)//2

            total_time = sum(math.ceil(p/mid) for p in piles)

            if total_time <=h:
                high = mid #try a smaller speed
            else:
                low = mid +1 
        return low 

