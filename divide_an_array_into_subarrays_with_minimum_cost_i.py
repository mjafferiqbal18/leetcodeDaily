class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        Problem: 3010. Divide an Array Into Subarrays With Minimum Cost I
        https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

        Intuition:
        - First subarray always starts at idx 0
        - the rest can start from 1..n-1
            - one should start at min
            - the second should start a 2nd min
        
        Time:
        - O(n + 2logn) = O(n+logn)

        Space:
        - O(n) but can also be O(1)

        """
        
        minHeap = [n for n in nums[1:]]
        heapq.heapify(minHeap)
        return (nums[0] + heapq.heappop(minHeap) + heapq.heappop(minHeap))

        