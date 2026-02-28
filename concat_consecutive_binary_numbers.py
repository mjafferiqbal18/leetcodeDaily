import math
class Solution:
    """
    Problem: 1680. Concatenation of Consecutive Binary Numbers
    https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

    Intuition:
    - Had to go through example first to immediately see that you need to left shift the running binary number
    - You need to find the num bits required by i, left shift res by that ammount and then do OR with i
        - num bits required by i  = floor( log2 (i) ) + 1
    - Remember to take mod as you go to prevent the number from becoming too big
    
    Time:
    - O(n)

    Space:
    - O(1)

    
    """
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        i = 2
        res = 1
        while i<= n:
            req = floor(math.log2(i)) + 1 #bits required by i
            res = ((res << req) | i) % MOD 
            # print(format(res, 'b')) ##best way to print the number in binary form for debugging
            i += 1
        return res % MOD
