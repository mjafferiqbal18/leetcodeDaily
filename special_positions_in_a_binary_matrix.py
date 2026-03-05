class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Problem: 1582. Special Positions in a Binary Matrix
        https://leetcode.com/problems/special-positions-in-a-binary-matrix/

        Intuition:
        - Record num 1s for each row, and for each column by iterating over each elem
        - iterate again, and add to res if mat[r][c]==1 and that row has only 1 one and column also has only 1 one

        Time:
        - O(mn)

        Space:
        - O(m+n)
        
        """

        rows = len(mat)
        cols = len(mat[0])

        r_ones = [0]*rows
        c_ones = [0]*cols

        for r in range(rows):
            for c in range(cols):
                r_ones[r] += mat[r][c]
                c_ones[c] += mat[r][c]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if r_ones[r]==1 and c_ones[c]==1 and mat[r][c]==1:
                    res+=1
        return res