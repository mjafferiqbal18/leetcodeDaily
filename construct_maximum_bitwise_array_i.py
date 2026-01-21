class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        Problem: 3314. Construct the Minimum Bitwise Array I
        https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

        Intuition:
        - One can simply try finding a satisying number in the range 1..(nums[i]-1)

        Time:
        - O(m*n) -> n is len(nums) and m=max(nums)

        Space:
        - O(1)

        """
        n=len(nums)
        ans=[-1]*n

        for i in range(n):
            for j in range(1,nums[i]):
                if j|(j+1)==nums[i]:
                    ans[i]=j
                    break        
        return ans