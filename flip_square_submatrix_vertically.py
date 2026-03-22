class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        """
        Problem: 3643. Flip Square Submatrix Vertically
        https://leetcode.com/problems/flip-square-submatrix-vertically/

        Intuition:
        - Just go column by column and flip the row elems

        Time:
        - O(n^2)

        Space:
        - O(1)
        
        
        """
        for col in range(y,y+k):
            st = x
            end = x + k - 1
            while st <= end:
                grid[st][col], grid[end][col] = grid[end][col], grid[st][col]
                st += 1
                end -= 1
        return grid

