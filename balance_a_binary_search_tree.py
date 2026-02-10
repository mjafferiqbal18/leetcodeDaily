# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Problem: 1382. Balance a Binary Search Tree
    https://leetcode.com/problems/balance-a-binary-search-tree/

    Intuition:
    - Do an inorder traversal, that tells you the values 'in-order'
    - Take mid as root, all values to left of mid as left subtree, all values to right as right sub tree
    - Do recursively

    Time:
    - O(n)

    Space:
    - O(n)
    
    """
    def __init__(self):
        nodes=[]
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.nodes= self.getNodes(root)
        nr = self.buildTree(0,len(self.nodes)-1)
        return nr

    
    def buildTree(self,l,r):
        if (l>r) or not(l>=0 and l<len(self.nodes) and r>=0 and r<len(self.nodes)):
            return None
        midIdx = (r+l)//2
        root = TreeNode(val=self.nodes[midIdx])
        root.left = self.buildTree(l,midIdx-1)
        root.right = self.buildTree(midIdx+1,r)
        return root

    def getNodes(self,root):
        nodes = []
        def preorder(root):
            if not root:
                return 
            
            preorder(root.left)
            nodes.append(root.val)
            preorder(root.right)
        preorder(root)
        return nodes