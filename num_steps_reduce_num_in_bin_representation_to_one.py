class Solution:
    def numSteps(self, s: str) -> int:
        """
        Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
        https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

        Intuition:
        - We know lenght of s is max 500, so we can try for an O(n^2) solution
        - Convert to a list, use st and end to track the string, then you can think about the case:
            - if even, then we divide by 2, so we can just shift the end ptr one pos to the right (we simulate shift right)
            - if odd, we change s[end] to 0, and then keep changing all consec 1s we see from end to 0s, until we come across the first 0, which we turn to 1

        Time:
        - O(n^2) because while processing the odd case we could iterate n times 

        Space:
        - O(n) to convert to list

        """

        s = [c for c in s]
        st = 0
        n = len(s)
        end = n - 1
        res = 0

        while (end>=0) and not(st == end and s[st] == "1") :
            if s[end] == "0":
                end -= 1 #you reduce the size
            else: #odd
                s[end] = "0"
                i = end - 1
                while i >= st:
                    if s[i] == "0":
                        s[i] = "1"
                        break
                    else:
                        s[i] = "0"
                    i -= 1
            res += 1
        return res