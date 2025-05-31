class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n =len(nums)
        k = k%n
        res =[0]*n

        for i in range(n):
            res[(i+k)%len(nums)]=nums[i]
        nums[:]=res
