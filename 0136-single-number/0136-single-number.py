class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        n = len(nums)
        w_list = defaultdict(int)

        for i in range(n):
            w_list[nums[i]]+=1

        for key,value in w_list.items():
            if value ==1:
                return key
        
        