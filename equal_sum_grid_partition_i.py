class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        Problem: 3546. Equal Sum Grid Partition I
        https://leetcode.com/problems/equal-sum-grid-partition-i/

        Intuition:
        - Constraints show that we can do at max one pass over the matrix
        - We do one pass to calculate total, and update row and column totals as well
        - We then go over the row total and carry a prefix sum, if prefix*2 == total, that means we can place a divider there, return True
        - Same case for col total
        - You cant do total // 2 == prefix (because total could be odd) -> best to do prefix*2 == total

        Time:
        - O(n*m)

        Space:
        - O(n+m)
        
        """

        m = len(grid)
        n = len(grid[0])

        #sum all the elems
        total = 0
        rowSum = [0]*m
        colSum = [0]*n
        for r in range(m):
            for c in range(n):
                total += grid[r][c]
                rowSum[r] += grid[r][c]
                colSum[c] += grid[r][c]
        
        if total%2 != 0:
            return False
        
        #go row by row
        prefix = 0
        for r in range(m):
            prefix += rowSum[r]
            if prefix*2 == total:
                return True
        
        #go column by column
        prefix = 0
        for c in range(n):
            prefix += colSum[c]
            if prefix*2 == total:
                return True
        
        return False

        