class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = [(abs(e - x), e) for e in arr]
        distances.sort()  # Sort by distance, then value because tuples compare in order
        return sorted([e for _, e in distances[:k]])  #