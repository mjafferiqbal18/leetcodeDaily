class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        """
        Problem: 3379. Transformed Array
        https://leetcode.com/problems/transformed-array/

        Intuition:
        - Just use mods to ensure you're at a valid index (mods of negative numbers are fine too (they are correctly mapped to 0..n-1))

        Time:
        - O(n)

        Space:
        - O(n)
        
        """
        n = len(nums)
        res = [0]*n
        
        for i in range(n):
            if nums[i] == 0:
                res[i] == nums[i]
            elif nums[i] > 0:
                res[i] = nums[(i+nums[i])%n]
            elif nums[i] < 0:
                res[i] = nums[(i-abs(nums[i]))%n]
        return res
