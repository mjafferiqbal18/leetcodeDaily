class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        Problem: 1895. Largest Magic Square
        https://leetcode.com/problems/largest-magic-square/

        Intuition:
            - You make prefix arrs for rows, cols, posDiag, negDiag 
            - NOTE: you can do all that in one go
            - Then you fix an idx r,c and start at the max k you can and go inwards (allows for early termination)
                - in this you see if posDiag==negDiag==sum(rows)==sum(cols)
        
        Time:
        - O(m*n*(min(m*n)))

        Space:
        - O(m*n)

        """
        return self.findLargestK(grid)

    def findLargestK(self,grid):
        ROWS=len(grid)
        COLS=len(grid[0])
        res=1

        RowPrefix= [[0]*COLS for _ in range(ROWS)]
        ColPrefix= [[0]*COLS for _ in range(ROWS)]
        PosDiagPrefix= [[0]*COLS for _ in range(ROWS)] #r+c
        NegDiagPrefix= [[0]*COLS for _ in range(ROWS)] #r-c

        #fill prefix arrays  -> you can do this in one loop
        for r in range(ROWS):
            for c in range(COLS):
                RowPrefix[r][c]= grid[r][c] + (RowPrefix[r][c-1] if c-1>=0 else 0)
                ColPrefix[r][c]= grid[r][c] + (ColPrefix[r-1][c] if r-1>=0 else 0)
                PosDiagPrefix[r][c]= grid[r][c] + (PosDiagPrefix[r-1][c+1] if r-1>=0 and c+1<COLS else 0) #youd want to add yourself+topright sum
                NegDiagPrefix[r][c]= grid[r][c] + (NegDiagPrefix[r-1][c-1] if r-1>=0 and c-1>=0 else 0) #youd want to add youself + topleft sum

        for r in range(ROWS):
            for c in range(COLS): 
                #r,c in topleft corner
                maxIdx= min(ROWS-1-r,COLS-1-c) #r+maxIdx,c+maxIdx is bottomright

                for k in range(maxIdx,-1,-1): #k denotes max len of square, give topleft is at r,c
                    #while calculating sum, it is VERY important to subtract the sum beyond r,c
                    posDiag= PosDiagPrefix[r+k][c] - (PosDiagPrefix[r-1][c+k+1] if r-1>=0 and c+k+1<COLS else 0)
                    negDiag= NegDiagPrefix[r+k][c+k] - (NegDiagPrefix[r-1][c-1] if r-1>=0 and c-1>=0 else 0)
                    
                    if posDiag!=negDiag:
                        continue
                    else:
                        valid=True #to allow for early termination
                        for nr in range(r,r+k+1):
                            rp = RowPrefix[nr][c+k]-(RowPrefix[nr][c-1] if c-1>=0 else 0)
                            if rp!=posDiag:
                                valid=False
                                break

                        if not valid:
                            continue

                        valid=True
                        for nc in range(c,c+k+1):
                            cp = ColPrefix[r+k][nc] - (ColPrefix[r-1][nc] if r-1>=0 else 0)
                            if cp!=posDiag:
                                valid=False
                                break
                        
                        if not valid:
                            continue
                        
                        res=max(res,k+1) #because res is supposed to hold side length
                        break
        return res
                        



