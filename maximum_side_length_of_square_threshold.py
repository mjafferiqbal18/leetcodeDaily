class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Problem: 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
        https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

        Intuition:
        - Brute force would be to start at each r,c and then build squares -> O((m*n)^2)
        - We make a prefix array, in which prefix[r][c] is the bottom right corner of the square
        - Then we start at each r,c and for each length in range 1<=x<=maxLen, we check if area <= threshold

        Time:
        - O(m*m*(min(m,n))) 
            - We can improve this by doing a binary search: minSide=0,maxSide=min(ROWS,COLS)
            - then a binary search would have us go over the matrix to find a topleft (r,c) such that its square of size==mid is <=threshold
                - if yes, then we increase the side size
                - else decrease the side size
            - this improves the time complexity to O(m*n*log(min(m,n)))

        Space:
        - O(m*n)
        """

        ROWS=len(mat)
        COLS=len(mat[0])
        prefix= [[0]*COLS for _ in range(ROWS)]

        #fill prefix arr
        for r in range(ROWS):
            rowSum=0
            for c in range(COLS):
                rowSum+=mat[r][c]
                prefix[r][c]= rowSum + (prefix[r-1][c] if r-1>=0 else 0) #the prefix sum here is everything above
        
        res=0
        for r in range(ROWS):
            for c in range(COLS):
                maxLen =  min(ROWS-r, COLS-c)
                
                nr,nc = r,c
                for currLen in range(1,maxLen+1): #length range is 1..maxLen inclusive
                    allArea = prefix[nr][nc]
                    leftArea = (prefix[nr][c-1] if c-1>=0 else 0) #everything to the left
                    allAboveArea = (prefix[r-1][nc] if r-1>=0 else 0) #everything above
                    aboveArea = max(0,(allAboveArea-(prefix[r-1][c-1] if r-1>=0 and c-1>=0 else 0))) #required above
                    squareArea = allArea - leftArea - aboveArea 

                    if squareArea <= threshold:
                        res= max(res, currLen)
                        nr,nc = nr+1,nc+1
                        if not(nr<ROWS and nc<COLS): #if we're out of bounds now, just break
                            break
                    else:
                        break
        return res

                    
                    


                



                


        