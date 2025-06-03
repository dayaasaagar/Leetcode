class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        num_set={0:1}
        count =0 
        cs =0



        for i in range(len(nums)):
            cs+=nums[i]

            if cs-k in num_set:
                count+=num_set[cs-k]
            num_set[cs]= num_set.get(cs,0)+1
        return count


        