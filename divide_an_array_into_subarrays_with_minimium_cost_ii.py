class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        """
        Problem: 3013. Divide an Array Into Subarrays With Minimum Cost II
        https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

        Intuition:
            https://www.youtube.com/watch?v=gNf2bNGg294
        
        
        """
        # from containers import SortedList()
        n=len(nums)

        smallestValsInWindow = SortedList()
        largestValsInWindow = SortedList()

        l = 1
        #building initial window
        for r in range(1,1+dist+1):
            smallestValsInWindow.add((nums[r],r))
        
        while len(smallestValsInWindow)>k-1:
            largestValsInWindow.add(smallestValsInWindow.pop(-1))
        
        #now we have built our window out of smallest k-1 and largest values in window
        windowSum = 0
        for val,idx in smallestValsInWindow:
            windowSum+=val
        
        res=windowSum
        
        # now we iterate
        for r in range(1+dist+1,n):
            #remove the left most element in the window
            elemIdxToBeRemoved = r - dist - 1
            elemValToBeRemoved = nums[elemIdxToBeRemoved]
            key = (elemValToBeRemoved,elemIdxToBeRemoved)

            if key in smallestValsInWindow:
                windowSum -= elemValToBeRemoved
                smallestValsInWindow.discard(key) #remove that element

                if largestValsInWindow:
                    sVal, sIdx = largestValsInWindow.pop(0)
                    smallestValsInWindow.add((sVal,sIdx))
                    windowSum += sVal
            elif key in largestValsInWindow:
                largestValsInWindow.discard(key)
            
            #add the new elem (at nums[r])
            smallestValsInWindow.add((nums[r],r))
            windowSum += nums[r]

            if len(smallestValsInWindow)>(k-1):
                sVal,sIdx = smallestValsInWindow.pop(-1)
                windowSum -= sVal
                largestValsInWindow.add((sVal,sIdx))
            
            res = min(res, windowSum)

        return nums[0]+res        
            

       