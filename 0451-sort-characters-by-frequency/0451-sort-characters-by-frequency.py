class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        result=[]
        newarray = sorted(counter.items(), key= lambda x: -x[1])
        for key,value in newarray:
            result.append(key*value)
        
        return ''.join(result)


        