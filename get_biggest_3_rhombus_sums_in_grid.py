class Solution:
    """
    1878. Get Biggest Three Rhombus Sums in a Grid
    https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

    Intuition:
    - The constraints are small enough to allow you to traverse over all rhombuses
    - You see if a rhombus is possible, then traverse, store total, and return top3 biggest totals (they have to unique)

    Time:
    - O(n*m*min(n,m)) -> the last n because for each elem we iterate from size 1 to minside

    Space:
    - O(n*m*min(n,m))
    
    """
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        minSide = min(m,n) 

        totals = []
        for r in range(m):
            for c in range(n):
                for size in range(1,minSide+1):
                    if self.canFit(m,n,r,c,size):
                        tot = self.traverseRhombus(m,n,grid,r,c,size)
                        totals.append(tot)
        totals = list(set(totals))
        totals.sort(reverse=True)
        return totals[0:3]
    
    def canFit(self,m,n,r,c,size):
        if size == 1:
            return True
        
        # if left corner and right corner and bottom corner
        if (c-(size-1)>=0 and r+(size-1)<m) and (c+(size-1)<n and r+(size-1)<m) and (r+2*(size-1)<m):
            return True

    def traverseRhombus(self,m,n,grid,r,c,size):
        lcR, lcC = r+(size-1), c-(size-1)
        rcR, rcC = r+(size-1), c+(size-1)
        bcR, bcC = r+2*(size-1), c

        total = grid[r][c]
        #go from top to lc
        for i in range(1,size):
            total += grid[r+i][c-i]

        #go from top to rc
        for i in range(1,size):
            total += grid[r+i][c+i]
        
        #go from lc to bottom corner
        for i in range(1,size):
            total += grid[lcR+i][lcC+i]

        #go from rc to bottom
        for i in range(1,size-1): #the size-1 is added to make sure we dont double count bottom
            total += grid[rcR+i][rcC-i]

        return total




