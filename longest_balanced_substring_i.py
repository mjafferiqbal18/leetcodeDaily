class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Problem: 3719. Longest Balanced Subarray I
        https://leetcode.com/problems/longest-balanced-subarray-i/

        Intuition:
        - Simple brute force implementation using 2 for loops

        Time:
        - O(n^2)

        Space:
        - O(1)
        """

        return self.bruteForce(s)
    def bruteForce(self,s):
        """
        Runs in O(n^2) -> passes test cases
        """
        n = len(s)
        res = 0

        for l in range(n):
            window = [0]*26
            for r in range(l,n):
                window[ord(s[r])-97]+=1

                if self.checkAllSame(window):
                    res = max(res, r-l+1)
        return res
    
    def checkAllSame(self,window):
        ref = -1
        for val in window:
            if val>0 and ref==-1: #first non zero value encountered
                ref = val

            if val>0 and ref!=val:
                return False
        return True
        