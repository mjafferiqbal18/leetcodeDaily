class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Problem: 3719. Longest Balanced Substring II
        https://leetcode.com/problems/longest-balanced-substring-ii/
        
        Intuition (seen from yt):
        - You have to split input into 3 cases:
            - (i) only one char:
                - look for the longest substring such that it has only 1 char
            - (ii) 2 chars:
                - look for the longest substring such that it has 2 chars
                    - if you encounter any other char, treat that as a break
                    - assign +1 to char1, -1 to char2, and you can use a strategy similar to subarray sum = k (k=0)
                    - this is essentially (char1 - char2) computation at each step
            - (iii) 3 chars:
                - similar to (ii):
                    - you have 2 sub cases: (char1 - char2), (char1 - char3)
                    - you can store this information as a tuple
                    - then use prefixes to see if youve seen it before
                        - if youve seen the tuple, then the diff = 0    
                        - THIS MEANS: the quantities of char1,char2,char3 are equal
        
        Time:
        - O(n)

        Space:
        - O(n)
        
        """
        maxOneChar= max(self.onlyOneChar('a',s),self.onlyOneChar('b',s),self.onlyOneChar('c',s))
        maxTwoChars= max(self.twoChars('a','b',s),self.twoChars('b','c',s),self.twoChars('a','c',s))
        maxThreeChars= self.threeChars(s)
        return max(maxOneChar,maxTwoChars,maxThreeChars)

    
    def onlyOneChar(self,c,s):
        n = len(s)
        l = 0
        res = 0

        for r in range(n):
            if s[r]==c:
                res = max(res, r-l+1)
            else:
                l=r+1
        return res
    
    def twoChars(self,char1,char2,s):
        """
        We can take count(char1)-count(char2) -
            - same thing as doing +1 when you see char1 and a -1 when you see char2
        Use same strategy as subarray sum = k, with an adjustment:
            - we dont need to know how many -> we need to know max size
            - so if curr diff is new, store it (dont overwrite it when you see it again)
        """
        c1 = 0
        c2 = 0
        n = len(s)        
        prefix = {0:-1} #maps a diff to idx (diff of 0 starts 'before' the array)
        res = 0

        for i in range(n):
            if (s[i]!=char1 and s[i]!=char2): #break encountered
                prefix = {0:i} #reset everything
                c1,c2 = 0,0
                continue
            c1 += (1 if s[i]==char1 else 0)
            c2 += (1 if s[i]==char2 else 0)
            diff = c1 - c2
            if diff in prefix:
                res = max(res, i-prefix[diff])
            else:
                prefix[diff]=i
        return res
    
    def threeChars(self,s):
        """
        The three chars are a,b,c, so char1=a, char2=b, char3=c
        Similar approach to twochars, but here we use tuples, and store:
            - char1-char2 = diff1
            - char1-char3 = diff2
        No need for a 'break'
        """

        c1,c2,c3 = 0,0,0
        prefix = {(0,0):-1}
        n = len(s)
        res = 0

        for i in range(n):
            c1 += (1 if s[i]=='a' else 0)
            c2 += (1 if s[i]=='b' else 0)
            c3 += (1 if s[i]=='c' else 0)

            diff1 = c1 - c2
            diff2 = c1 - c3
            key = (diff1, diff2)

            if key in prefix:
                res = max(res, i - prefix[key])
            else:
                prefix[key] = i
        return res