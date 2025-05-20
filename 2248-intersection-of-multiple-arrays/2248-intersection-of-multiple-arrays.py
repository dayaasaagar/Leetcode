class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        result_set = set(nums[0])

        for i in nums[1:]:
            result_set&=set(i)
                   
        return sorted(result_set)
                