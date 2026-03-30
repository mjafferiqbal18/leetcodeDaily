class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        2840. Check if Strings Can be Made Equal With Operations II
        https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

        Intuition:
        - If counter values for even idxs are same, and counter values for odd idxs are same, then it is true
        - More brute forcy way is to simulate those swaps

        Time:
        - O(n)

        Space:
        - O(n)

        
        """
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
        if not self.checkIfPossible(s1,s2):
            return False 

        s1charToPosEvenIdxs = {} # maps a char in s1 to even idxs it exists on
        s1charToPosOddIdxs = {} # maps a char in s1 to even idxs it exists on
        for i,c in enumerate(s1):
            if i%2 == 0:
                if c not in s1charToPosEvenIdxs:
                    s1charToPosEvenIdxs[c] = set()
                s1charToPosEvenIdxs[c].add(i)
            else:
                if c not in s1charToPosOddIdxs:
                    s1charToPosOddIdxs[c] = set()
                s1charToPosOddIdxs[c].add(i)

        for i,c in enumerate(s1):
            if i%2 == 0: #we need to swap with another even index
                if s2[i] in s1charToPosEvenIdxs:
                    s1charToPosEvenIdxs[s2[i]].pop() #this has gone in the correct position
                    if len(s1charToPosEvenIdxs[s2[i]]) == 0:
                        del s1charToPosEvenIdxs[s2[i]]
                else:
                    return False
            else: #we need to swap with another odd index
                if s2[i] in s1charToPosOddIdxs:
                    s1charToPosOddIdxs[s2[i]].pop() #this has gone in the correct position
                    if len(s1charToPosOddIdxs[s2[i]]) == 0:
                        del s1charToPosOddIdxs[s2[i]]
                else:
                    return False
        return True

    def checkIfPossible(self,s1,s2):
        l1, l2 = [c for c in s1], [c for c in s2]
        l1.sort()
        l2.sort()
        return l1 == l2