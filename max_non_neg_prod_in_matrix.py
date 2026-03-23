class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        
        Intuition:
        - we can only move right or down; so at a cell (apart from first row and first col) we came there from the left or from above
        - cant store only max, since a currently max can be multipled by a negative number and become super small
        - to address this, we can use 2 dps, one for max and one for min
            - these 2 dps will help us fill the max and min dps correctly because of the following four cases:
                - filling maxDP[r][c]:
                    - grid[r][c] is negative:
                        - we need to maximize prod, so we need the smallest value from above and left -> get from minDP
                        - why smallest? because the most neg value (smallest) * us = big positive prod
                    - grid[r][c] is positive:
                        - pick the biggest val from above and left -> get from maxDP
                - filling minDP[r][c]:
                    - grid[r][c] is negative:
                        - we need to minimize prod, so use the biggest val (hopefully pos) from above or left -> get from maxDP
                    - grid[r][c] is positive:
                        - we need to minimize prod, so use the smallest val from above or left -> get from minDP
        
        Time:
        - O(n*m)

        Space:
        - O(n*m)
        """

        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        maxDP = [[1]*n for _ in range(m)]
        minDP = [[1]*n for _ in range(m)]

        maxDP[0][0] = grid[0][0]
        minDP[0][0] = grid[0][0]

        #fill first row
        for c in range(1,n):
            maxDP[0][c] = maxDP[0][c-1]*grid[0][c]
            minDP[0][c] = minDP[0][c-1]*grid[0][c]
        
        #fill first col
        for r in range(1,m):
            maxDP[r][0] = maxDP[r-1][0]*grid[r][0]
            minDP[r][0] = minDP[r-1][0]*grid[r][0]
        
        for r in range(1,m):
            for c in range(1,n):
                if grid[r][c] >= 0:
                    maxDP[r][c] = max(maxDP[r-1][c], maxDP[r][c-1]) * grid[r][c]
                    minDP[r][c] = min(minDP[r-1][c], minDP[r][c-1]) * grid[r][c]
                else:
                    maxDP[r][c] = min(minDP[r-1][c], minDP[r][c-1]) * grid[r][c]
                    minDP[r][c] = max(maxDP[r-1][c], maxDP[r][c-1]) * grid[r][c]
        
        return maxDP[m-1][n-1] % MOD if maxDP[m-1][n-1]>=0 else -1

        """
        topdown approach with memo
        O(m*n*(range of products))
        """
    
        memo = {}
        def topdown(r,c,p):
            if r==m-1 and c==n-1:
                p = p*grid[r][c]
                return p if p>=0 else -1
            
            key = (r,c,p)
            if key in memo:
                return memo[key]

            ans = float('-inf')
            p = p * grid[r][c]

            #go down
            if r < m-1:
                ans = max(ans, topdown(r+1,c,p))
            
            #go right
            if c < n-1:
                ans = max(ans, topdown(r,c+1,p))
            
            memo[key] = ans
            return memo[key]

        res = topdown(0,0,1)
        return res % MOD if res>=0 else -1


            