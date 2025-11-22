class Solution:
    def triangleType(self, nums: List[int]) -> str:

        a,b,c = sorted(nums)

        if a+b<=c:
            return "none"

        c_new = Counter(nums)


        if len(c_new)==1:
            return "equilateral"
        elif len(c_new)==2:
            return "isosceles"
        else:
            return "scalene"




        