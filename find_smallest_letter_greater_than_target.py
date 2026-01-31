class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Problem: 744. Find Smallest Letter Greater Than Target
        https://leetcode.com/problems/find-smallest-letter-greater-than-target/

        Just do it! (there isnt much in the name of intuition here honestly)
        
        """
        res = letters[0]
        letters = list(set(letters))
        n= len(letters)
        ans = ""
        ansOrd = float('inf')

        for i in range(n):
            if ord(letters[i])>ord(target):
                if ord(letters[i])<ansOrd:
                    ansOrd = ord(letters[i])
                    ans = letters[i]
        
        return ans if ansOrd!=float('inf') else res

        