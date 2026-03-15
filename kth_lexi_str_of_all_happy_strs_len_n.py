class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Problem: 1415. The k-th Lexicographical String of All Happy Strings of Length n
        https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

        Intuition:
        - From constraints we can see that we can generate all string permutations 
        - We generate valid permuations using backtracking, then index via k

        Time:
        - O(2^(n)) because O(3*(2^(n-1))) 3 choices for first pos, 2 choices for every position apart from first

        Space:
        - O(2^(n))
        
        """
        sol = []
        res = []
        def backTrack(i):
            if i == n:
                res.append(''.join(sol))
                return
            
            if i == 0:
                for c in range(97,100):
                    sol.append(chr(c))
                    backTrack(i+1)
                    sol.pop()
            else:
                for c in range(97,100):
                    if chr(c) == sol[-1]:
                        continue
                    else:
                        sol.append(chr(c))
                        backTrack(i+1)
                        sol.pop()
        
        backTrack(0)
        return res[k-1] if (k-1)<len(res) else ""