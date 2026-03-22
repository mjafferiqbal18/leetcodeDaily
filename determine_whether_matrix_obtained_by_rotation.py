class Solution:
    """
    Problem: 1886. Determine Whether Matrix Can Be Obtained By Rotation
    https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

    Intuition:
    - You can rotate a matrix 90 degrees by at max 3 times
    - Just rotate and compare
        - to rotate in place, take transpose and reverse rows
    
    Time:
    - O(n^2)

    Space:
    - O(n^2) -> O(1) extra since we do everything in place

    """
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if self.checkIfEqual(mat,target,n):
            return True

        for _ in range(3):
            mat = self.rotateMat90(mat,n)
            if self.checkIfEqual(mat,target,n):
                return True
        
        return False

    def checkIfEqual(self,m1,m2,n):
        for r in range(n):
            for c in range(n):
                if m1[r][c] != m2[r][c]:
                    return False
        return True

    def rotateMat90(self,mat,n):
        """
        You do an inplace transpose, then reverse each row
        """
        for r in range(n):
            for c in range(r+1,n):
                mat[r][c],mat[c][r] = mat[c][r],mat[r][c]
        
        for row in range(n):
            l,r = 0,n-1
            while l<=r:
                mat[row][l], mat[row][r] = mat[row][r], mat[row][l]
                l += 1
                r -= 1
        return mat
        





