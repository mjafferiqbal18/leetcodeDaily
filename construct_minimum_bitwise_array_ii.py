class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        Problem: 3314. Construct the Minimum Bitwise Array II
        https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

        Intuition:
        - It is first important to know what happens at bit level when we add +1 to a number
            - assume binary representation is: 011011 +1 -> 011100 -> so the first 0 beomces one, everything to right becomes 0, and everything to left remains as is
            - so adding 1 to a number will change nothing to the left of the first 0, will flip the first 0 and turn everything to the right of the first 0 to 0s
        - thus number OR (number+1) will never change any bits left of the first 0 in number
        - We can only change bits including and to the right of the first 0
            - Now those 'influence-able' bits would be 0 followed by a number of 1s
                - e.g. 0111, then:
                    - nums[i] could be 11, nums[i]+1 could be 100, and their OR would be 0111
                - e.g. 13-> 1101, influencable bits are 01:
                    - nums[i] could be 1100, nums[i]+1 would be 1101
                - e.g. 31 -> 11111, can be thought of as 011111, influence-able bits are 11111
                    - nums[i] could be 1111, nums[i]+1 could be 10000, thier OR would be 11111
            - we learn that we take the number of 1s to the right of the first 0 -> (x) number of 1s
                - we right-shift that, that makes it our ans[i] -> (x-1) number of 1s
                - because when we add 1 to it, it will become 1(x-1 number of 0s), their OR will be (x) number of 1s 
        
        Time:
        - O(n*log(max(nums)))

        Space:
        - O(max(nums))

        """
        n=len(nums)
        ans=[-1]*n
        for i in range(n):
            if nums[i]%2==0: #it is guaranteed that either one of ans[i] or ans[i]+1 is odd -> their bitwise OR will never be even (so cant equal nums[i])
                continue

            mask=1
            temp=nums[i]
            influencable=0 #we will capture the part to the right of the first 0
            count=0
            # print(nums[i])
            while (temp&mask)==mask: #this runs until we keep seeing 1s
                influencable=influencable|mask #capture the 1
                influencable=influencable<<1 #shift left to make space for next 
                temp=temp>>1 #shift temp right
                count+=1 #count number of times temp is shifted right
            
            #influencable will be <number of 1s to the right of first 0>0 -> e.g. 11011 -> 110, so first right shift it once to get actual influencebale-> 11
            #   11011 -> infulenable: 110 -> 11, then right shift that again to get ans[i], 11-> 01. if ans[i]=01, then ans[i]+1 should be 10, and their OR==influenceable==11
            ans[i]=influencable>>2 | temp<<count
        return ans