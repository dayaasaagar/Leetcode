class Solution:
    def frequencySort(self, s: str) -> str:
        countdic = Counter(s)

        h = [(-count,character) for character,count in countdic.items()]
        heapify(h)
        result=[]
        while h:
            count,character = heappop(h)
            result.append(character*-count)

        return ''.join(result)





        