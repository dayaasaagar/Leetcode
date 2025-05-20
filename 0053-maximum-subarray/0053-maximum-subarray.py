class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = current_sum = nums[0]


        for num in nums[1:]:

            current_sum= max(num,current_sum+num)

            maxsum = max(current_sum,maxsum)

        return maxsum




