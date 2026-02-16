class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Problem: 190. Reverse Bits
        https://leetcode.com/problems/reverse-bits/

        Intuition:
        - Capture bit
        - shift left the current res, and then OR the bit (dont or bit and then shift left because then in the last iteration you would be shifting an extra left)
            - e.g. 0110 -> 0110
            - (shift left then OR) 4 times: 0000 -> 0001 -> 0011 -> 0110
            - (OR then shift left) 4 times: 0000 -> 0010 -> 0110 -> 1100 (incorrect)

        Time:
        - O(logn)

        Space:
        - O(1)
        """
        res = 0
        for i in range(32):
            b = n & 1  #capture the right most bit of n
            res = res << 1  # first shift existing res once to the left, to make space for the bit
            res = res | b # or the bit to 'add' it to res
            n = n >> 1 #update right most bit of n
        return res