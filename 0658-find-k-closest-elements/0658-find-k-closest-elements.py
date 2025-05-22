class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left =0 
        right = len(arr)-k

        while left<right:

            mid = (left+right)//2

            if abs(x-arr[mid])>abs(arr[mid]-x):
                left = mid +1 
            else:
                right = mid

        return arr[left:left+k]
