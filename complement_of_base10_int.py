class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Problem: 1009. Complement of Base 10 Integer
        https://leetcode.com/problems/complement-of-base-10-integer/

        Intuition:
        - You capture the last bit, flip it and place it appropriately in res
            - you left shift the flipped bit and OR with res
        
        Time:
        - O(1)

        Space:
        - O(1)

        """
        
        if n == 0: #base case
            return 1

        res = 0
        c = 0 
        while n != 0: 
            b = n & 1 #capture the right most bit
            res = res | (0 if b == 1 else 1) << c #shift it c times, then OR with res
            n = n >> 1 #shift n right once so we can capture it next bit in the next iteration
            c += 1 #increment the leftshift count
        return res

        