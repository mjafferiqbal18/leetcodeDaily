class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Problem: 1877. Minimize Maximum Pair Sum in Array
        https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

        Intuition:
        - Sort the array, and pair the min elem with max elem, move pointer inwards
        - record the max sum

        Time:
        - O(nlogn)

        Space:
        - O(1)

        """
        nums.sort()
        l,r=0,len(nums)-1

        res=float("-inf")
        while l<r:
            res=max(res, nums[l]+nums[r])
            l+=1
            r-=1
        return res
