class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Problem: 868. Binary Gap
        https://leetcode.com/problems/binary-gap/

        Intuition:
        - Very simple

        Time:
        - O(logn)

        Space:
        - O(1)


        """
        i = 0
        res = 0
        LastOneIdx = -1

        while n != 0:
            b = n & 1
            if b == 1:
                tempRes = ((i-LastOneIdx) if LastOneIdx != -1 else 0)
                res = max(res, tempRes)
                LastOneIdx = i
            i += 1
            n = n >> 1
        
        return res
        
