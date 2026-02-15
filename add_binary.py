class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Problem: 67. Add Binary
        https://leetcode.com/problems/add-binary/

        Intuition:
        - Just reverse and padd, then add, take care of carry at the end, then unpad

        Time:
        - O(n)

        Space:
        - O(n)

        """
        a = a[::-1]
        b = b[::-1]
        L = min(len(a),len(b))
        maxL = max(len(a),len(b))
        a += "0"*(maxL - L) #padding
        b += "0"*(maxL - L) #padding

        i = 0
        carry = 0
        res = ""

        while i < maxL:
            temp = int(a[i]) + int(b[i]) + carry
            carry = 0
            if temp == 2:
                carry = 1
                temp = 0
            elif temp == 3:
                carry = 1
                temp = 1
            res += str(temp)
            i += 1
        
        if carry == 1:
            res += "1"
        
        res = res[::-1]

        #remove padding from the start
        ans = ""
        i = 0
        L = len(res)

        while res[i]==0:
            i+=1
        ans = res[i::]
        return ans
        