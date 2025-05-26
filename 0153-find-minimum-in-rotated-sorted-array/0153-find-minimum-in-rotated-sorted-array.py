class Solution:
    def findMin(self, nums: List[int]) -> int:

        hmap = {i:v for i,v in enumerate(nums)}

        min_value = min(hmap.values())

        return min_value
        