class Solution:
    """
    Problem: 3637. Trionic Array I
    https://leetcode.com/problems/trionic-array-i/

    Intuition:
        - Just record the p,q,last seen and validate that theyre not the same, p isnt 0 and last is well, n-1
    
    Time:
    - O(n)

    Space:
    - O(1)
    """
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i<n:
            if not(nums[i]>nums[i-1]):
                break
            i+=1
        p = (i-1)
        
        while i<n:
            if not (nums[i]<nums[i-1]):
                break
            i+=1
        q = (i-1) #i-1 is supposed to be at q (which cant be n-1)
        
        while i<n:
            if not  (nums[i]>nums[i-1]):
                break
            i+=1
        last = i-1

        if (p!=0) and (q>p) and (last>q) and last==(n-1):
            return True
        return False 
        
    