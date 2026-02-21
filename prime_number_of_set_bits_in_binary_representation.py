class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Problem: 762. Prime Number of Set Bits in Binary Representation
        https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

        Intuition:
        - just find num bits, then see if that num bits is prime (and also memoize the answer)

        Time:
        - O((right-left)*(logn)*(3..num))

        Space:
        - O(prime seen)

        """
        res = 0
        bitsToIsPrime = {}
        for i in range(left,right+1):
            numBits = self.countBits(i)
            if numBits not in bitsToIsPrime:
                bitsToIsPrime[numBits] = self.isPrime(numBits)
            res += (1 if bitsToIsPrime[numBits] else 0)
        return res
    
    def isPrimeOptimized(self,num):
        if num <= 1: #not a prime
            return False
        if num==2 or num==3: #easy case: if 2 or 3, return true
            return True
        if num % 2 == 0: #any even number cant be a prime because it can be divided by 2
            return False

        #then you find the largest number which is the sqrt of num
        #then you iterate 3 ... sqrt(num) to find a factor

    def isPrime(self,num):
        if num <= 1:
            return False
        i = 2
        while i<num:
            if num%i == 0:
                return False
            i+=1
        return True

    def countBits(self,num):
        res = 0
        while num!=0:
            res += num & 1
            num = num >> 1
        return res
        