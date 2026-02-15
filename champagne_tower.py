class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """ 
        Problem: 799. Champagne Tower
        https://leetcode.com/problems/champagne-tower/

        Intuition:
        - We pour into the first cup, excess = poured - 1
        - Then pour the excess into the next row, and then so on
        - If we have a excess at a glass at (r+1,c) then half its excess will flow to (r+1,c+1) and half to (r+1,c+1) 
            - for example, (0,0) pours excess to (1,0) and (1,1)

        Time:
        - O(r^2) where r is query row

        Space:
        - O(r^2) where r is query row

        Solution taken from Jayant Patel's uploaded solution
        """
        tower = [[0] * 102 for _ in range(102)] #values range from 0 to 101
        tower[0][0] = poured
        
        for r in range(query_row + 1): #row should go up to and including query row
            for c in range(r + 1):  #col should go up to an including row (row=0, go up to col=0 | row=1, go up to col=1)
                if tower[r][c] > 1: # i.e we have some access amount 
                    excess = (tower[r][c] - 1.0) / 2.0 #this is the excess that has to go to the next row
                    tower[r][c] = 1 #you fill this cup
                    tower[r+1][c] += excess #pour excess
                    tower[r+1][c+1] += excess #pour excess
        
        #we have processed all rows up to and including query row
        return tower[query_row][query_glass]