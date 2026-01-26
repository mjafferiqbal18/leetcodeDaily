class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        Problem: 1200. Minimum Absolute Difference
        https://leetcode.com/problems/minimum-absolute-difference/

        Intuition:
        - Sort array, then for finding the minimum abs differnce youll only have to look at adjacent elements
        - Go over elem pairs, find the minAbsDifference, then go over pairs again and record the pairs

        Time:
        - O(nlogn)

        Space:
        - O(n)

        
        """
        n=len(arr)
        arr.sort()
        minAbsDifference=float('inf')
        for i in range(1,n):
            minAbsDifference = min(minAbsDifference, arr[i]-arr[i-1])

        res=[]
        for i in range(1,n):
            if arr[i]-arr[i-1] == minAbsDifference:
                res.append([arr[i-1],arr[i]])
        return res


        