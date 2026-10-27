class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            if matrix[i][0] <= target:
                row = i
                if matrix[i][0] == target:
                    return True
                left = 0
                right = c-1
                while left<=right:
                    mid = left + ((right-left)//2)
                    print("ele ", matrix[row][mid])
                    if matrix[row][mid] == target:
                        return True
                    if matrix[row][mid] >= target:
                        right = mid-1
                    else:
                        left = mid+1
        return False
