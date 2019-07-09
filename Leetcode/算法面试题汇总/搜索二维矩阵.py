"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false

"""

class Solution(object):
    def searchMatrix(self,matrix,target):
        """
                :type matrix: List[List[int]]
                :type target: int
                :rtype: bool
                """
        # print(len(matrix))

        # i = 0
        # j = len(matrix) - 1
        # while i < len(matrix) and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] > target:
        #         j -= 1
        #     else:
        #         i += 1
        # return False

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        r = rows - 1
        c = 0
        while c < cols and r >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False

"""
j = -1
        for row in matrix:
            while j > -len(row) and row[j] > target:
                j -= 1
            if row and row[j] == target:
                return True
        return False
"""

"""
if len(matrix) == 0 or len(matrix[0]) == 0:
                return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        r = rows - 1
        c = 0
        while c < cols and r >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False
"""


search_matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(Solution().searchMatrix(search_matrix,110))