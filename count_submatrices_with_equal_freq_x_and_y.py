class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        Problem: 3212. Count Submatrices With Equal Frequency of X and Y
        https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

        Intuition:
        - grid[0][0] has to be in there
        - we can use a 2d prefix sum:
            - prefixSum[i][j] represents the rectangle formed by grid[0][0] and grid[r][c]
            - you record the prefix as 2 values: countX, countY
            - Fill prefix row by row (by keeping prefix counts)
            - row 1 is special case, and further rows use prefixes of previous rows as well
        - We can improve this as well by keeping 2 rows (instead of m rows) -> m*n prefix is commented out

        Time:
        - O(m*n)

        Space:
        - O(n) 
        
        """
        m = len(grid)
        n = len(grid[0])
        prefix = [[0]*n for _ in range(m)] #represents countX, countY
        prev = [0]*n
        curr = [0]*n 
        res = 0

        for r in range(m):
            rowX, rowY = 0,0
            for c in range(n):
                rowX += (1 if grid[r][c] == 'X' else 0)
                rowY += (1 if grid[r][c] == 'Y' else 0)
                
                if r == 0:
                    # prefix[r][c] = [rowX, rowY]
                    curr[c] = [rowX, rowY]
                else:
                    # prefix[r][c] = [rowX+prefix[r-1][c][0], rowY+prefix[r-1][c][1]]
                    curr[c] = [rowX+prev[c][0], rowY+prev[c][1]]
                
                # res += (1 if (prefix[r][c][0] > 0 and prefix[r][c][0] == prefix[r][c][1]) else 0)
                res += (1 if (curr[c][0] > 0 and curr[c][0] == curr[c][1]) else 0)
            prev = curr.copy()
            curr = [0]*n
        return res

        