class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        ds=0
        for n in nums:
            if n>9:
                while n>0:
                    digit=n%10
                    ds+=digit
                    n//=10
            else:
                ds+=n
        
        return abs(ds-sum(nums))
        




        