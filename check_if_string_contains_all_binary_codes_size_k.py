class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Problem: 1461. Check If a String Contains All Binary Codes of Size K
        https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

        Intuition:
        - codes are merely numbers from 0 to (2^k - 1) -> this helps since we wont have to use strings
            - if you use backtracking to find all possible strings then youll also have to store them (will cause memory limit exceeded)
            - So its best to stay in int, and loop from 0...(2^k - 1)
        - You use a sliding window over s, convert window of size k into numerical representation, then store
        - At the end, you can loop over 0..maxNum, and see if any is not in the numbers in s

        - The current process of finding all numbers in s is of O(kn)
            - You can improve this by shiftleft and then adding lsb value
            - Lets say window is "01" -> you have the number seen, you shift it left to get "1" and then add whatever s[i] in rightmost pos
            - This can improve the current way to O(n)

        Time:
        - O(kn) -> O(n) in optimized

        Space:
        - O(kn) -> O(n) in optimized
        """
        return self.optimized(s,k) #call to the optimized function with time = O(n)
        maxNum = (2**k) - 1
        numsInS = set()

        l = 0
        n = len(s)

        for r in range(n):
            if (r - l + 1) == k:
                numsInS.add(self.convertToNum(s[l:r+1][::-1],k))
                l += 1
        # print(numsInS)
        for i in range(maxNum+1):
            if i not in numsInS:
                return False
        return True

    def convertToNum(self,s,k):
        """
        expects a reversed string
        """
        ans = 0
        for i in range(k):
            ans += (2**i if s[i]=="1" else 0)
        return ans

    def optimized(self,s,k):
        maxNum = (2**k) - 1
        numsInS = set()

        l = 0
        n = len(s)

        if n < k:
            return False
        
        lastNum = self.convertToNum(s[:k][::-1],k)
        numsInS.add(lastNum)
        mask = (2**(k-1)) - 1

        for i in range(k,n):
            lastNum = (lastNum & mask) << 1
            currNum = lastNum | (1 if s[i]=="1" else 0)
            numsInS.add(currNum)
            lastNum = currNum
        
        # print(numsInS)
        for i in range(maxNum+1):
            if i not in numsInS:
                return False
        return True
        


