class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Intuition:
        - First thought is to take total product of the grid, and then divide each num 
            - while m*n is of 10^5, the product and division operation is what will cost a tle
            - So from our understanding, tle is caused by multiplying super large numbers 
            - To fix, one can think about pushing the MOD inwards (instead of just at the end)
                - the issue with that is that the solution doesnt retain correctness, considering that we divide at the end
        - So to push MODs inwards (i.e. while taking products), we think if we can solve without dividing
        - We can solve without dividing by using prefix and suffix -> and the running prefix can be modded along the way
        - using a prefix suffix approach is better and passes tests

        Time:
        - O(m*n)

        Space:
        - O(1)

        """
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        # we iterate in reverse by carrying a running suffix, and imaginign the grid as one long array
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD

        # next, we iterate in the forward manner by carrying a running prefix
        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD

        return p