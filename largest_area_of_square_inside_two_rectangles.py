class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        """
        Problem: 3047. Find the Largest Area of Square Inside Two Rectangles
        https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

        Intuition:
            - Smallest overlap when looking at x-coordinates (THEY NEED TO BE >0):
                - min(topRight[i][0],topRight[j][0]) - max(bottomLeft[i][0],bottomLeft[j][0])
            - Smallest overlap when looking at y-coordinates:
                - min(topRight[i][1],topRight[j][1]) - max(bottomLeft[i][1],bottomLeft[j][1])
            - take the minimum of these and the square of the min will be the area
        
        """
        n=len(bottomLeft)
        area=0

        for i in range(n):
            for j in range(i+1,n):
                s1=max(0,min(topRight[i][0],topRight[j][0]) - max(bottomLeft[i][0],bottomLeft[j][0]))
                s2=max(0,min(topRight[i][1],topRight[j][1]) - max(bottomLeft[i][1],bottomLeft[j][1]))
                s= min(s1,s2)
                area = max(area, s**2)
        return area