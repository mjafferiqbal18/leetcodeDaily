class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Problem: 3510. Minimum Pair Removal to Sort Array II
        https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

        [0,1,2,3]
        [5,2,3,1]
        res=0
        [(4,(2,3)),(6,(1,2)),(7,(0,1))]

        [ 0, 1, 2, 3]
    prev[-1, 0, 1, 2]
    next[ 1, 2, 3,-1]

        [5,2,3,1]
        [(4,(2,3)),(5,(1,2)),(7,(0,1))]

        --------------------
        [ 0, 1, 2, 3]
    prev[-1, 0, 0, 1]
    next[ 1, -1,-1,-1]

        [5,6,6,4]
        [(11,(0,1)),(7,(0,1))]

        3
        [ 4, 7, 14]

        [ 4, 6, 1, 0, 9, 5]
    prev[-1, 0, 1, 2, 3, 4]
    next[ 1, 2, 3, 4, 5,-1]

        [(10,(0,1)),(7,(1,2)),(1,(2,3)),(9,(3,4)),(14,(4,5))]

        1
        [ 4, 7, 7, 1, 9, 5]
    prev[-1, 0, 0, 1, 3, 4]
    next[ 1, 4, 4, 4, 5,-1]

        [(10,(0,1)),(9,(3,4)),(14,(4,5))]
        



        
        """
        




        """
        
        
        """
        res=0
        n=len(nums)
        isValid = [True]*n
        prev = [i-1 for i in range(n)]
        next = [i+1 for i in range(n)]
        next[-1] = -1

        minHeap = []
        for i in range(1,n): #we put everything in minheap
            minHeap.append((nums[i]+nums[i-1],(i-1,i)))
        heapq.heapify(minHeap)
        
        badCount = 0 #stores the number of inverted pairs
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                badCount += 1

        def is_bad(i, j): 
            """
            Returns true if two idxs are valid and are in decreasing order
            """
            return i != -1 and j != -1 and isValid[i] and isValid[j] and nums[i] > nums[j]

        while minHeap and badCount > 0: 
            Sum, idxes = heapq.heappop(minHeap)
            prevIdx, nextIdx = idxes

            #merge if both indexes are valid, are not stale (next[prevIdx]==nextIdx) and their sum==sum
            if (isValid[prevIdx] and isValid[nextIdx]) and (next[prevIdx] == nextIdx) and (nums[prevIdx]+nums[nextIdx]==Sum):# and (nums[prevIdx]>nums[nextIdx]):
                #update res
                res+=1

                #store neighbours
                L = prev[prevIdx]  # left neighbor of prevIdx
                R = next[nextIdx]  # right neighbor of nextIdx (since nextIdx is being removed)

                #
                if is_bad(prevIdx, nextIdx):       badCount -= 1 # we are directly fixing this
                if L != -1 and is_bad(L, prevIdx): badCount -= 1 #
                if R != -1 and is_bad(nextIdx, R): badCount -= 1 

                
                # invalidate
                isValid[nextIdx]=False

                # update nums
                nums[prevIdx]= Sum

                # update indexes
                next[prevIdx] = next[nextIdx]
                if next[prevIdx] != -1:
                    prev[next[prevIdx]] = prevIdx

                if L != -1 and (is_bad(L, prevIdx)): 
                    badCount += 1
                if R != -1 and is_bad(prevIdx, R): 
                    badCount += 1

                # re-que
                if prev[prevIdx]!= -1 and isValid[prev[prevIdx]]: #and nums[prev[prevIdx]]>nums[prevIdx]:
                    heapElem= (nums[prev[prevIdx]]+nums[prevIdx],(prev[prevIdx],prevIdx))
                    heapq.heappush(minHeap,heapElem)
                
                if next[prevIdx]!=-1 and isValid[next[prevIdx]]:# and nums[prevIdx] > nums[next[prevIdx]]:
                    heapElem= (nums[next[prevIdx]]+nums[prevIdx],(prevIdx,next[prevIdx]))
                    heapq.heappush(minHeap,heapElem)

            # print(nums)
            # print(isValid)
            # print(prev)
            # print(next)
            # print(minHeap)
            # print('*******')

        return res


