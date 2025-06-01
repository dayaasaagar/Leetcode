class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        newlist = set(nums)
        missing =None

        for i in range(len(nums)+1):

            if i not in newlist:
                missing =i
        return missing

        