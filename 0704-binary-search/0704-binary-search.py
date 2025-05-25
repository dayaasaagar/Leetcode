class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low =0 
        high = len(nums)-1
        nums.sort()
        if nums[0] == target:
            return 0

        while low <= high:
            mid = (low+high)//2
            if nums[mid]>target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
            else:
                return mid
        return -1

        
            