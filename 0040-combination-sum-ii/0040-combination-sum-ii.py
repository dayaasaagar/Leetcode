class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def dfs(index,curr,total):
            if total == target:
                result.append(curr[:])
            if total>target:
                return

            prev =-1
            for i in range(index,len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                dfs(i+1,curr,total+candidates[i])
                curr.pop()
                prev = candidates[i]


        
        dfs(0,[],0)
        return result
