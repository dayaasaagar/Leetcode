class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        single= 0
        double =0

        for i in range(len(nums)):
            if nums[i]<10:
                single+=nums[i]
            else:
                double+=nums[i]
        
        if single>double or double>single:
            return True
        return False
        







        