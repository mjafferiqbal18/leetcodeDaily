class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        """
        Problem: 3640. Trionic Array II
        https://leetcode.com/problems/trionic-array-ii/

        Intuition:
        -  We can fix p,q and then see where l and r lie
            - To fix p,q you keep iterating as long as you have a decreasing sequence, p,q will lie on boundary
            - If not decreasing, then set q=p, and q+=1
            - You increment q until you come across first q such that nums[q]>= nums[q-1]
                - your 'q'(the one in question) would be at idx q-1 (if q-1 != p), and if nums[q]>nums[q-1] (check for trionic array property)
                - you would want the following sum:
                    - lp + pq + qr
                    - pq is sum between idx p and idx q inclusive (found with prefix sum)
                    - qr is found with previously done backWardPass, specifically backWardPass[q] (so backWardPass[q-1 + 1])
                    - lp is found with previously done forwardPass, specifically forwardPass[p-1]
            - how to find qr?
                - we want to find the max sum starting at q+1 all the way to r inclusive
                - r can lie between q+1 and n-1 inclusive
                - Remember max sum of subarry 
                    - we define a backWardPass memo of size n, each value == nums[i]
                    - backWardPass[i] denotes the max sum you can get, starting at i and going right, given then the sequence is increasing
                    - You can use opposite logic for a forward pass, where starting at i and going left, whats the max sum you can get given sequence is increasing
            
            Time:
            - O(n)

            Space:
            - O(n)
        

        - To see where r lies, you can 


        """
        n = len(nums)
        backWardPass = [0]*n
        backWardPass[n-1]= nums[n-1]
        forwardPass = [0]*n
        forwardPass[0] = nums[0]
        prefixSum = [0]*n

        for i in range(n-2,-1,-1): 
            backWardPass[i] = nums[i]
            if nums[i]<nums[i+1]: #only look at increasing slope
                if backWardPass[i+1]>0: #then we will increase our sum
                    backWardPass[i] += backWardPass[i+1]
        
        for i in range(1,n):
            forwardPass[i]=nums[i]
            if nums[i]>nums[i-1]: #increasing slope
                if forwardPass[i-1]>0: #it will increase our sum
                    forwardPass[i]+=forwardPass[i-1]

        currSum = 0
        for i in range(n):
            currSum+= nums[i]
            prefixSum[i] = currSum

        res=float('-inf')
        p = 1
        q = 2

        while q<=(n-1):
            # print(p,q)
            if nums[q]<nums[q-1]:
                pass
            else: 
                #q is supposed to be at q-1
                if q-1 != p and (q-1)<(n-1) and nums[q]>nums[q-1]:  #optionally also check if nums[p-1]>nums[p]
                    pq = prefixSum[q-1] - prefixSum[p-1]
                    lp = forwardPass[p-1]
                    qr = backWardPass[q]
                    res = max(res, lp+pq+qr) 
                    print(p,q-1,lp,pq,qr,lp+pq+qr)
                p=q
            q+=1

        # print(res)
        # print(forwardPass)
        # print(backWardPass)

        return res
        