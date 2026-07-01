class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # traverse top row, left -> right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # traverse right column, top -> bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # traverse bottom row, right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # traverse left column, bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result