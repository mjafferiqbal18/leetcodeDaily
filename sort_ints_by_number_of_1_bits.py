class Solution:
    """
    Problem: 1356. Sort Integers by The Number of 1 Bits
    https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

    Intuition:
    - Just get the number of ones in each num, and sort by the WHOLE tuple so that ties are broken based on the number itself
    - NOTE: Lets say you had to break ties by:
        - descending order of numbers -> you would store (ones,-num) in tuples then
        - or you first sort based on tiebreaker, then sort based on the primary way

    Time:
    - O(nlogn)

    Space:
    - O(n)

    """

    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = []
        for num in arr:
            nums.append((self.findNumOnes(num),num))
        nums.sort() #sort by both keys: if you give a specific key then it will only sort on that

        res = []
        for ones,n in nums:
            res.append(n)
        return res
        
    def findNumOnes(self,num):
        res = 0
        while num!=0:
            res += num & 1
            num = num >> 1
        return res

        