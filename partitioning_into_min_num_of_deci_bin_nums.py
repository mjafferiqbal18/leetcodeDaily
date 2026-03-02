class Solution:
    """
    Problem: 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
    https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

    Intuition:
    - the answer should be equal to the max digit in the string 
        - for example, 2380, to reduce 8 to 0 you have to minus 1 8times
    
    Time:
    - O(len(s))

    Space:
    - O(1)
    """
    def minPartitions(self, n: str) -> int:
        maxDigit = "0"
        for character in n:
            if ord(character) > ord(maxDigit):
                maxDigit = character
        return int(maxDigit)
        # return int(max(s))