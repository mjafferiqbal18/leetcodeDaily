class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        """
        Problem: 3634. Minimum Removals to Balance Array
        https://leetcode.com/problems/minimum-removals-to-balance-array/

        Intuition:
        - Naiive solution would opt to sort and start evictling largest (but in that case it may have been best to evict smallest)
        - Use a sliding window, and store the size of the valid sliding window 
        - Size of sliding window will be the size of maximum balanced subarray, n-that = minimum number of elements you need to remove

        Time:
        - O(n)

        Space:
        - O(1)

        """

        nums.sort()
        l = 0
        res = 0
        n = len(nums)

        for r in range(n):
            while not(nums[r]<=k*nums[l]) and l<=r:
                l+=1
            #now array is balanced
            res = max(res, r-l+1)
        return n-res