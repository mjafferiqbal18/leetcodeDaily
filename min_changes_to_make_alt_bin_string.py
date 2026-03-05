class Solution:
    def minOperations(self, s: str) -> int:
        """
        Problem: 1758. Minimum Changes To Make Alternating Binary String
        https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

        Intuition:
        - You build the two possibilities of strings (starting with 0 or starting with 1)
        - Then calculate mismatches and return the minimum

        Time:
        - O(n)

        Space:
        - O(n)
        
        """
        n = len(s)
        s = list(s)
        s1 = ['0' if i%2==0 else '1' for i in range(n)]
        s2 = ['1' if i%2==0 else '0' for i in range(n)]

        return min(self.calculateOps(s,s1,n),self.calculateOps(s,s2,n))

    def calculateOps(self,s,sPrime,n):
        res = 0
        for i in range(n):
            res += (1 if s[i]!=sPrime[i] else 0)
        return res
        
        