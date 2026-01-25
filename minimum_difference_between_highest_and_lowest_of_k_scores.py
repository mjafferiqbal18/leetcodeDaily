class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Problem: 1984. Minimum Difference Between Highest and Lowest of K Scores
        https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

        Intuition:
        - Sort array so that k consecutive elements will have the minimum difference
        - Then iterate over the array and find minimum res

        Time:
        - O(nlogn)

        Space:
        - O(1)


        """
        nums.sort()
        n=len(nums)
        l=0
        r=min(k-1,n-1) #right pointer
        res=float('inf')
        
        for i in range(r,n):
            res= min(res, abs(nums[i]-nums[l]))
            l+=1
        return res


        