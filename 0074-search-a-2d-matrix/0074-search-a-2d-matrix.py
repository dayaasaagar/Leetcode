class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows,cols = len(matrix), len(matrix[0])
        result = []
        for i in range(rows):
            for j in range(cols):
                result.append(matrix[i][j])
        low = 0
        high = len(result)-1

        while low<=high:
            mid = (low + high)//2

            if result[mid]>target:
                high = mid -1
            elif result[mid]<target:
                low = mid +1
            elif result[mid]==target:
                return True
        return False

