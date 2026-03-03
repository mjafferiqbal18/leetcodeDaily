class Solution:
    """
    Problem: 1545. Find Kth Bit in Nth Binary String
    https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

    Intuition:
    - Just solve via recursion lol

    Time:
    - O(2^n) -> because it is O(string length), and string length = 2^n -1

    Space:
    - O(2^n)
    
    """
    def findKthBit(self, n: int, k: int) -> str:
        def findBits(n):
            if n == 1:
                return "0"
            prevS = findBits(n-1)
            return prevS + "1" + self.reverse(self.invert(prevS))
        
        s = findBits(n)
        return s[k-1]
    
    def reverse(self,x):
        return x[::-1]
    
    def invert(self,x):
        res = ""
        for c in x:
            if c == "0":
                res += "1"
            else:
                res += "0"
        return res

        