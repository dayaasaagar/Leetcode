class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        result = [0]*len(temperatures)
        prev=0

        for i,temp in enumerate(temperatures):


            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev = stack.pop()
                result[prev]=i-prev
            stack.append(i)
        return result 
            
