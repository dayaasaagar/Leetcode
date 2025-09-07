class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = Counter(nums)


        return [num for num, _ in heapq.nlargest(k,most_freq.items(),key = lambda x:x[1])]
            