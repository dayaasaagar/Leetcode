class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()
        duplicate =None
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                duplicate = nums[i]


        return duplicate
                
