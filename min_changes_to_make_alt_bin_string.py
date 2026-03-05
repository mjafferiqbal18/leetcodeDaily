class Solution:
    """
        Problem: 1758. Minimum Changes To Make Alternating Binary String
        https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

        Intuition:
        - You build the two possibilities of strings (starting with 0 or starting with 1)
        - Then calculate mismatches and return the minimum
        - You can also observe that the two counts have the following property:
            - if c1 = x, c2 = n-x

        Time:
        - O(n)

        Space:
        - O(n)
        
    """
    def minOperations(self, s: str) -> int:
        return self.optimized(s)
        n = len(s)
        s = list(s)
        s1 = ['0' if i%2==0 else '1' for i in range(n)]
        s2 = ['1' if i%2==0 else '0' for i in range(n)]

        return min(self.calculateOps(s,s1,n),self.calculateOps(s,s2,n))
    
    def optimized(self,s):
        """
        We'll try to do in O(1) space and O(n) time
        We observe that count1 = x, then count2 = n - x
        Lets try to do in O(1) space
        """
        n = len(s)
        zero = True
        count = 0

        #we only check the pattern starting from 0 
        for i in range(n):
            if (zero and s[i] == '1') or (not zero and s[i]=='0'):
                count += 1
            zero = not zero
        
        return min(count, n - count)


    def calculateOps(self,s,sPrime,n):
        res = 0
        for i in range(n):
            res += (1 if s[i]!=sPrime[i] else 0)
        return res
        
        