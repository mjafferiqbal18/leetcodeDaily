class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Problem: 696. Count Binary Substrings
        https://leetcode.com/problems/count-binary-substrings/

        Intuition:
        - This was a bit of a wierd question + my solution isnt good, but is still linear time and passes tests
        - You recognize that there are two patterns (zeros then ones) and (ones then zeros)
        - So you can write separate implementations for both cases

        Time:
        - O(n)

        Space:
        - O(1)
        
        """


        return self.countZerosThenOnes(s) + self.countOnesThenZeros(s)
    

    def countZerosThenOnes(self,s):
        n = len(s)
        zero = True if s[0]=='0' else False
        consecZeros = 1 if s[0]=='0' else 0
        consecOnes = 1 if s[0]=='1' else 0
        res = 0

        for i in range(1,n):
            if s[i] == '0' and zero:
                consecZeros+=1
            elif s[i] == '0' and not zero:  #reset
                consecZeros = 1
                consecOnes = 0
            elif s[i] == '1' and zero: 
                consecOnes = 1
                if consecZeros >= consecOnes:
                    res += 1
            elif s[i] == '1' and not zero:
                consecOnes += 1
                if consecZeros >= consecOnes:
                    res += 1
            
            #update zeros
            zero = True if s[i]=='0' else False
        return res
    
    def countOnesThenZeros(self,s):
        n = len(s)
        zero = True if s[0]=='0' else False
        consecZeros = 1 if s[0]=='0' else 0
        consecOnes = 1 if s[0]=='1' else 0
        res = 0

        for i in range(1,n):
            if s[i] == '0' and zero:
                consecZeros += 1
                if consecOnes >= consecZeros:
                    res += 1
            elif s[i] == '0' and not zero: 
                consecZeros = 1
                if consecOnes >= consecZeros:
                    res += 1
            elif s[i] == '1' and zero:  #reset
                consecOnes = 1
                consecZeros = 0
            elif s[i] == '1' and not zero:
                consecOnes += 1
            
            #update zeros
            zero = True if s[i]=='0' else False
        return res
    

    



       