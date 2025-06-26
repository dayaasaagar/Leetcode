class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        numset = set()

        for i in range(len(nums)):

            if nums[i]>0:
                numset.add(nums[i])

        
        for i in range(1,len(nums)+1):

            if i not in numset:
                return i

        return len(nums)+1
