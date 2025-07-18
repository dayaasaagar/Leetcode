class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path,used):

            if len(path) == len(nums):
                result.append(path[:])
                return


            for i in range(len(nums)):

                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    backtrack(path,used)
                    path.pop()
                    used[i]=False
        result =[]
        backtrack([],[False]*len(nums))
        return result