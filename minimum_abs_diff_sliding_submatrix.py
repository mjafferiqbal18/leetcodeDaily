class Solution:
    """
    Problem: 3567. Minimum Absolute Difference in Sliding Submatrix
    https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

    Intuition:
    - You gather the elems in each of the submatrices, then find minabsdiff for the gathered elems
        - you gather in a list and sort, then go pair by pair to find min abs diff (while skipping same elems)
        - you need this since elems closest to each other are adjacent, allowing for abs diff to be less
    
    Time:
    - O((m-k)*(n-k)*(k^2 * log(k^2))) -> (m-k)(n-k) submatrices, each submatrix work is k^2 + k^2 log (k^2)

    Space:
    - O(k^2) -> we store this temporarily
    
    """
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        result = [[0]*(n-k+1) for _ in range(m-k+1)]
        for r in range(m-k+1):
            for c in range(n-k+1):
                elems = []
                for i in range(r,r+k):
                    for j in range(c,c+k):
                        elems.append(grid[i][j])
                minabsdiff = self.findAbsMinDiff(elems)
                result[r][c] = minabsdiff if minabsdiff!=float('inf') else 0
        return result

    def findAbsMinDiff(self,elems):
        elems.sort()
        n = len(elems)
        res = float('inf')
        for i in range(1,n):
            if elems[i] != elems[i-1]:  #since we need to find elems with distinct values
                res = min(res, abs(elems[i]-elems[i-1]))
        return res

        

