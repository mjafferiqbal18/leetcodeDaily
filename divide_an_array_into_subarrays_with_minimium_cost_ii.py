class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        """
        Problem: 3013. Divide an Array Into Subarrays With Minimum Cost II
        https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

        Intuition:
        - You can use topdown dp to solve it -> O(kn) time and space
        
        """
        n = len(nums)
        sol=[]
        res=[]
        memo={}
        chosen_Is = [] #should be of atleast length 2
        chosen_Vals = []
 
        def topdown(i,kLeft):
            if kLeft==0:
                if chosen_Is[0]!=chosen_Is[-1] and (chosen_Is[0]-chosen_Is[-1])<=dist:
                    return sum(chosen_Vals)
                else:
                    return  float('inf')
            
            if i==n: #end of array, havent divided array properly
                return float('inf')
            
            key = (i,kLeft)
            if key in memo:
                return memo[key]
            
            cost = float('inf')
            #either choose this idx to divide
            chosen_Is.append(i)
            chosen_Vals.append(nums[i])
            cost = min(cost, topdown(i+1,kLeft-1))
            chosen_Is.pop()
            chosen_Vals.pop()

            #dont choose this idx to divide
            cost = min(cost, topdown(i+1,kLeft))

            memo[key] = cost
            return cost
            
        return topdown(1,k-1)