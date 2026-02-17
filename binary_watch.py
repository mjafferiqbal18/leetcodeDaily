class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        Problem: 401. Binary Watch
        https://leetcode.com/problems/binary-watch/

        Intuition:
        - You need backtracking to generate the bits 
        - Then you can convert the bits to time (can also filter invalid time)
        - Another approach would be to enumerate all combinations that exist for these hours and minutes
            - Then, you can filter by cases where number of bits == turnedOn

        Time:
        - O(10^n) -> O(1)

        Space:
        - O(1)
        
        """

        sol = []
        res =[] 
        n = 10
        def backtrack(left,i):
            if i==n and left==0:
                res.append(sol.copy())
                return
            elif i==n:
                return

            #turn current bit on if left >0
            if left>0:
                sol.append(i)
                backtrack(left-1,i+1) 
                sol.pop()

            #dont turn current bit on
            backtrack(left,i+1)

        backtrack(turnedOn,0)
        return self.convertBitIdxesToTimes(res)
    
    def convertBitIdxesToTimes(self,bitArr):
        """
        Interpret bitArr as follows:
        - first 6 idxes are mins:
            - 1 2 4 8 16 32
        - last 4 idxes are hours:
            - 1 2 4 8
        """
        res = []

        for rowThatHasBeenSet in bitArr:
            hours = 0
            mins = 0
            for idx in rowThatHasBeenSet:
                if idx <= 3: #we process hours # 0 -> 1, 1 -> 2, 2 -> 4, 3 -> 8
                    hours += 2**idx
                else:
                    mins += 2**(idx-4) 
            
            if (hours>11) or (mins>59):  #this is invalid, so we dont use it
                continue 

            h = str(hours)
            m = (str(mins) if mins>9 else "0"+str(mins)) 
            res.append((hours*60+mins,h+":"+m))
        res.sort(key=lambda x:x[0])

        ans = []
        for minutes,timeStr in res:
            ans.append(timeStr)
        return ans

        
