class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countdic = Counter(nums)
        h = [(count,-num) for num,count in countdic.items()]
        heapify(h)
        result=[]

        while h:
            count,num = heappop(h)
            result.extend([-num]*count)

        return result

        