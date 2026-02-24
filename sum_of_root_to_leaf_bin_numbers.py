# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Problem: 1022. Sum of Root To Leaf Binary Numbers
    https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

    Intuition:
    - You could do a post order traversal, build binary strings and process them later
    - A better approach is to build the binary number as you co by left shifting current num so far
        - this left shift = number * 2
        - Once you reach a leaf you return the number built so far
            - Otherwise, you recurse on left and right and provide them current so far, and return their sum
    
    Optimized:
    - Time: O(n)
    - Space: O(1)
    
    """

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def preOrder(root,current):
            if not root:
                return 0 
            
            current = current*2 + root.val
            if not root.left and not root.right: #if we are a leaf
                return current
            
            left = preOrder(root.left,current)
            right = preOrder(root.right,current)

            return left + right
        
        return preOrder(root,0)


        def postOrder(root):
            if not root:
                return []
            
            left = postOrder(root.left)
            right = postOrder(root.right)

            if not left and not right:
                return [str(root.val)]
            
            ans = []
            for l in left:
                ans.append(l)
            for r in right:
                ans.append(r)
            for i in range(len(ans)):
                ans[i] = ans[i] + str(root.val)
            return ans
        
        binStrings = postOrder(root)
        
        res = 0
        for bS in binStrings:
            res += self.binToNum(bS)
        return res
    
    def binToNum(self,s):
        # s = s[::-1] #reverse the string
        n = len(s)
        res = 0

        for i in range(n):
            res += (2**i if s[i]=='1' else 0)
        return res


            
            

        