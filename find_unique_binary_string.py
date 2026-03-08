class Solution:
    """
    Problem: 1980. Find Unique Binary String
    https://leetcode.com/problems/find-unique-binary-string/

    Intuition:
    - You can just convert each str_num to an actual number and put in set
    - given an n, nums can contain numbers from 0 to 2^n -1
    - just iterate from 0 to 2^n-1, and return the num thats not in numset
        - before returning, convert to binary string
    
    Time:
    - O(n^2 [for scanning n chars in each of the n strings] + 2^n [for iterating from 0..2^n-1]) -> O(2^n)
    
    Space:
    - O(n)
    
    """
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numbers = set([self.convertToDeci(num,n) for num in nums])
        maxNum = 2**(n) - 1
        for i in range(maxNum+1):
            if i not in numbers:
                return self.convertToBinString(i,n)
        return -1
    
    def convertToDeci(self,s,n):
        res = 0
        for i in range(n):
            res += (2**(i) if s[n-1-i]=='1' else 0)
        return res
    
    def convertToBinString(self,i,n):
        res = ""
        while i != 0:
            bit = i & 1
            res = str(bit) + res
            i = i >> 1
        padding = n - len(res)
        res = '0'*padding + res
        return res




        