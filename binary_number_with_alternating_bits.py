class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Problem: 693. Binary Number with Alternating Bits
        https://leetcode.com/problems/binary-number-with-alternating-bits/

        Intuition:
        - Just capture right most bit, keep track of what the prev bit was and continue
        
        Time:
        - O(logn)
        
        Space:
        - O(1)
        
        """
        if n==0:
            return False #all 0s
        elif n==1:
            return True #000001

        isZero = True if (n & 1)==0 else False
        n = n>>1

        while n!=0:
            b = n & 1
            if (b == 1 and not isZero) or (b == 0 and isZero):
                return False
            isZero = not isZero
            n = n>>1
        return True
            
