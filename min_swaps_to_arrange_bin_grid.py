class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        Problem: 1536. Minimum Swaps to Arrange a Binary Grid
        https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
        
        Intuition:
        - n = number of rows
            - you need n-1 rows where: we must have atleast 1 ... (n-1) number of rows from the right
            - this ensures we have a solution
            - First we validate if we have a solution, and early terminate otherwise
            - We can do an O(n^3) solution:
                - go from top to bottom, stop at i where ith row has less zeros than required ,and stop j when you reach something to swap with (atleast enough required zeros for i). You can swap in j-i moves:
                    - this is the greedy step
                    - example: 0 1 2 (represents the num zeros in row0,row1,row2)
                        - 0 1 2 -> 0 2 1 -> 2 0 1 
        Time:
        - O(n^2)

        Space:
        - O(n) 
        
        """
        n = len(grid)
        res = 0
        numZeros = [self.getNumZeros(row,n) for row in grid]
        sorted_numZeros = numZeros.copy()
        sorted_numZeros.sort(reverse=True)

        if not self.doesSolExist(sorted_numZeros,n):
            return -1

        for i in range(n): #outer loop
            if numZeros[i] < (n - i - 1): #matter
                for j in range(i+1,n):
                    if numZeros[j] >= (n - i - 1): #idx to swap with found
                        val = numZeros.pop(j)   # remove that row
                        numZeros.insert(i, val) # insert at i (bubbles it up)
                        res += (j-i)
                        # print(i,j)
                        # print(numZeros)
                        break
        return res

        """
        [0,0,1]
        [1,1,0]
        [1,0,0]
        
        0 1 2 
        """
    
    def doesSolExist(self,numZeros,n):
        for i in range(n):
            if numZeros[i] < (n - i - 1):
                return False
        return True
    
    def getNumZeros(self,row,n):
        res = 0
        for i in range(n-1,-1,-1):
            if row[i] == 1:
                return res
            res += 1
        return res



        