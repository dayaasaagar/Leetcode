class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nmap = {v:i for i,v in enumerate(nums)}
        newnums = sorted(nums)
        low = 0
        high = len(newnums)-1
        while low <=high:
            mid = (low+high)//2
            if newnums[mid]>target:
                high = mid-1
            elif newnums[mid]<target:
                low = mid+1
            elif newnums[mid]==target:
                return nmap[newnums[mid]]

        return -1