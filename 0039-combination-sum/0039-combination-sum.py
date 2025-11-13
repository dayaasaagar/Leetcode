class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        def backtrack(start,total,bag):
            if total == target:
                result.append(bag[:])
                return
            if total > target:
                return 
            
            for i in range(start,len(candidates)):
                bag.append(candidates[i])
                backtrack(i,total+candidates[i],bag)
                bag.pop()
        backtrack(0,0,[])
        return result
    
                
        