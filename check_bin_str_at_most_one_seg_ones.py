class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Problem: 1784. Check if Binary String Has at Most One Segment of Ones
        https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

        Intuition:
        - No leading 0s means that the string starts with 1
        - So for it to be true, it has to have 1s in the start, then only 0s
            - if theres a 1 after the 0, then itll be false

        Time:
        - O(len(s))

        Space:
        - O(1)
        """
        return not ("01" in s)
        