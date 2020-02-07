# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


ans = 0


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def findSum(root):
            if(not root):
                pass
            else:
                global ans
                copy = root
                if(root.left):
                    copy = root.left
                    if(not copy.left and not copy.right):
                        ans += copy.val
                    findSum(copy)
                if(root.right):
                    copy = root.right
                    findSum(copy)

        findSum(root)
        global ans
        real_ans = ans
        ans = 0
        return real_ans
