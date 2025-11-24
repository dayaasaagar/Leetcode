class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        prev = nums[0] 
        start = nums[0]

        for i in range(1,len(nums)):
            curr = nums[i]
            if curr == prev+1:
                prev = curr
            else:
                if start == prev:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{prev}")
                start = curr
                prev = curr
        
        if start ==prev:
            res.append(str(start))
        else:
            res.append(f"{start}->{prev}")
        return res
