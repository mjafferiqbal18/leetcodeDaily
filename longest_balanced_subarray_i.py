class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        """
        Problem: 3719. Longest Balanced Subarray I
        https://leetcode.com/problems/longest-balanced-subarray-i/

        Intuition:
        - Brute force works here, just use 2 for loops 

        Time:
        - O(n^2)

        Space:
        - O(n)

        brute force n^2 solution (passes test cases)
        """
        res = 0
        n = len(nums)
        for i in range(n):
            evenSet = defaultdict(int)
            oddSet = defaultdict(int)
            for j in range(i,n):
                if nums[j]%2==0:
                    evenSet[nums[j]]+=1
                else:
                    oddSet[nums[j]]+=1

                if len(evenSet) == len(oddSet):
                    res = max(res, j-i+1)

        return res 