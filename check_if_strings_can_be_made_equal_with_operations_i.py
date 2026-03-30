class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """
        2839. Check if Strings Can be Made Equal With Operations I
        https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

        Intuition:
        - they can be same if str[0] and str[2] converted to set is same in both strings (or sorted)
        - similar logic applies to str[1] and str[3]
        - We can do this hardcoded logic since string length has to be 4

        Time:
        - O(1)

        Space:
        - O(1)
        """
        # return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
        return ({s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]})


        


        