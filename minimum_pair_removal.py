class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Problem: 3507. Minimum Pair Removal to Sort Array I
        https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

        Intuition:
        - Need a way to check if sorted -> make a function for that -> O(n)
        - Then just record the idx of the min pair, rebuild nums and repeat until nums is sorted

        Time:
        - O(n^2)

        Space:
        - O(n)
        
        """
        res=0
        while not self.isSorted(nums):
            n=len(nums)
            minIdx=0
            minSum=nums[0]+nums[1]

            for i in range(2,n):
                if (nums[i]+nums[i-1])<minSum:
                    minIdx=i-1
                    minSum=nums[i]+nums[i-1]
            
            temp=[]
            i=0
            while i<n:
                if i==minIdx:
                    temp.append(minSum)
                    res+=1
                    i+=1
                else:
                    temp.append(nums[i])
                i+=1
            nums=temp
        return res
            
    def isSorted(self,nums):
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                return False
        return True


        
        