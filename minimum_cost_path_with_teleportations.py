class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        """
        Problem: 3651. Minimum Cost Path with Teleportations
        https://leetcode.com/problems/minimum-cost-path-with-teleportations/

        Intuition:
        - Need a way to check if sorted -> make a function for that -> O(n)
        - Then just record the idx of the min pair, rebuild nums and repeat until nums is sorted


        we can do a recursive solution with DP
        That will give TLE, but its good to understand it 
        - O(n * m * k)[num dp states] * O(n*m) [since we can teleport to any cell per recursive call]
        - O(n^2 * m^2 * k)
        

        Rest i copied from the solution (too complex :-x)
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        
        dp = {}


        def topdown(i,j,k):
            if (not (i>=0 and i<ROWS and j>=0 and j<COLS)): #out of bounds
                return float('inf')
            
            if i==ROWS-1 and j==COLS-1: #at destination
                return 0

            key=(i,j,k)
            if key in dp:
                return dp[key]

            #go right
            rightCost = float('inf')
            if j+1<COLS:
                rightCost = min(rightCost, grid[i][j+1]+topdown(i,j+1,k))
            
            #go down
            downCost = float('inf')
            if i+1<ROWS:
                downCost = min(downCost, grid[i+1][j]+topdown(i+1,j,k))

            #teleportation cost
            telepCost = float('inf')
            for r in range(ROWS):
                for c in range(COLS):
                    if (r!=i or c!=j) and (grid[r][c]<= grid[i][j]) and (k>0):
                        telepCost = min(telepCost, topdown(r,c,k-1))

            dp[key] = min(rightCost,downCost,telepCost)
            return dp[key]
        
        return topdown(0,0,k)

        """
        Editorial solution
        """
        
        m, n = len(grid), len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key=lambda p: grid[p[0]][p[1]])
        costs = [[float("inf")] * n for _ in range(m)]
        for t in range(k + 1):
            minCost = float("inf")
            j = 0
            for i in range(len(points)):
                minCost = min(minCost, costs[points[i][0]][points[i][1]])
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i + 1][0]][points[i + 1][1]]
                ):
                    i += 1
                    continue
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = minCost
                j = i + 1
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i != m - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i + 1][j] + grid[i + 1][j]
                        )
                    if j != n - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i][j + 1] + grid[i][j + 1]
                        )
        return costs[0][0]