class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        """
        Problem: 3296. Minimum Number of Seconds to Make Mountain Height Zero
        https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

        Brute force is O(n^2)
        optimized is nlogn
        """
        # return self.bruteForce(mountainHeight, workerTimes)
        return self.optimizedNlogN(mountainHeight, workerTimes)
    
    def optimizedNlogN(self, mountainHeight, workerTimes):
        """
        - Binary search range:
            - min = 1 (because mountainHeight > 0 always, we have to have one time step at least)
            - max = max(workerTimes) * (mH*(mH+1))/2; this picks the slowest worker, and assumes mH steps
        """
        n = len(workerTimes)
        l = 0
        r = ceil((max(workerTimes)) * ((mountainHeight*(mountainHeight+1))/2))
        res = r
        while l <= r:
            mid = (l+r)//2
            if self.canHeightBeReduced(mountainHeight, workerTimes, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

    
    def canHeightBeReduced(self, mountainHeight, workerTimes, t):
        """
        To know how much height is reduced by worker[i]:
            - think of height reduced as steps
            - steps can take values 1,2,3,4,5
            - time taken by worker[i] at step = x:
                - (sum 1..x)*(worker[i]) => x=n, ((n*(n+1))/2)*(worker[i])
            - so for a time t, we need to find the largest value of step=x, such that:
                - ((x*(x+1))/2)*(worker[i]) <= t
                - ((x*(x+1))/2) <= (t/(worker[i]))
                - x^2 + x <= 2*(t/(worker[i]))
                - x^2 + x -2*(t/(worker[i])) <= 0
                - use the formula -> x = (-b +- sqrt(b^2 - 4ac))/2a; where ax^2 + bx + c = 0
                - a=1, b=1, c = -2*(t/(worker[i]))
                - x = [-1 +- sqrt(1 - 4(-2*(t/(worker[i]))))]/2
            - x = [-1 + sqrt(1 - 4(-2*(t/(worker[i]))))]/2
            - we find x for each worker, if sum of x vals >= mountainHeight, t is an applicable answer, we reduce the boundary accordingly and update answer
    
        """
        xVals = 0
        for wt in workerTimes:
            xVals += floor((-1 + sqrt(1-4*(-2*(t/wt))))/2) #we take floor cause x has to be an int
        return (xVals >= mountainHeight)
    
    def bruteForce(self, mountainHeight, workerTimes):
        resT = 0
        n = len(workerTimes)
        muls = [1] * n
        workerTimesOG = workerTimes.copy()
        while mountainHeight > 0: 
            resT += 1
            mountainHeight = self.updateHeight(mountainHeight, muls, workerTimes, workerTimesOG, n, resT)
        return resT


    def updateHeight(self, mountainHeight, multipliers, workerTimes, workerTimesOG, n, t):
        hRed = 0
        for i in range(n):
            if workerTimes[i] == t:
                hRed += 1
                multipliers[i] += 1
                workerTimes[i] += (workerTimesOG[i]*multipliers[i])
        return mountainHeight - hRed
        
            