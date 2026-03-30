# class Solution:
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        1727. Largest Submatrix With Rearrangements
        https://leetcode.com/problems/largest-submatrix-with-rearrangements/

        Intuition:
        - Swapping columns changes the alignment of the 1s, though we cant control it 
        - If we can record at idx i,j how many 1s are consecutively above it, then we can think of alignment
            - then if we sort this row desc (which records num consec ones above) we can build rectanges based on the height 
            - as we go from l to r, we would see height decrease and base increase

        Time:
        - O(m*nlogn)

        Space:
        - O(m*n)


        """
        m = len(matrix)
        n = len(matrix[0])
        res = 0

        for r in range(m): #iterate over each row
            for c in range(n): #go over each col
                if matrix[r][c] != 0 and r > 0: 
                    matrix[r][c] += matrix[r-1][c] #this way you add the number of 1s above this row
                
            tempRow = sorted(matrix[r],reverse=True) #now we temporarily sort this row
            for tempC in range(n):
                res = max(res, tempRow[tempC]*(tempC+1)) #height * width
        return res