class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        countdic = Counter(nums)
        pairs=0
        nonpairs=0

        for freq in countdic.values():
            pairs+=freq//2
            nonpairs+=freq%2
        return [pairs,nonpairs]
