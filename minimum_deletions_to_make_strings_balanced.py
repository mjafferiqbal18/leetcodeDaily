class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Problem: 1653. Minimum Deletions to Make String Balanced
        https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

        Intuition:
        - At every index, (assume you can keep the character at s[idx]):
            - num deletions=B's on the left + A's on the right
            - You can precompute using a prefix sum
        
        Time:
        - O(n)

        Space:
        - O(n)

        """
        n = len(s)
        BsToLeft = [0]*n
        AsToRight = [0]*n

        #forward pass
        numBs=0
        for i in range(n):
            BsToLeft[i] = numBs
            numBs += (1 if s[i]=='b' else 0)
        
        #backward pass
        numAs = 0
        for i in range(n-1,-1,-1):
            AsToRight[i] = numAs
            numAs += (1 if s[i]=='a' else 0)        

        res = float('inf')

        for i in range(n):
            res = min(res, BsToLeft[i]+AsToRight[i])
        return res