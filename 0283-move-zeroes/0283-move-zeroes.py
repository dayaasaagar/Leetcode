class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzeros = []
        zeros=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zeros.append(nums[i])
            else:
                nonzeros.append(nums[i])
        nums[:]=nonzeros+zeros
        