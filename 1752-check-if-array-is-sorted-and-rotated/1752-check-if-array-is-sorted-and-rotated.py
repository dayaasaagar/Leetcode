class Solution:
    def check(self, nums: List[int]) -> bool:
        newlist = sorted(nums)
        newnums=nums[:]

        def rotate(nums):
            res=[0]*len(nums)

            for i in range(len(nums)):
                res[(i+1)%len(nums)]=nums[i]
            nums[:]=res
            return nums

        for _ in range(len(nums)):
            if newnums == newlist:
                return True
            rotate(newnums)
        return False