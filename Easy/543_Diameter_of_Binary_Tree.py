# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def DFS(node, node_stack):
            if node:
                node_stack.append(node)
                if node.left:
                    DFS(node.left, node_stack)
                if node.right:
                    DFS(node.right, node_stack)
        ans = 0
        node_stack = []
        DFS(root, node_stack)
        if len(node_stack) <= 2:
            return len(node_stack) - 1
        while node_stack:
            cur = node_stack.pop(-1)
            # print(cur)
            if cur.left and cur.right:
                cur.val = max(cur.left.val, cur.right.val) + 1
                ans = max(ans, cur.left.val + cur.right.val)
            elif cur.left:
                cur.val = cur.left.val + 1
            elif cur.right:
                cur.val = cur.right.val + 1
            else:
                cur.val = 1
            if cur == root:
                if cur.left and not cur.right or not cur.left and cur.right:
                    cur.val -= 1
            ans = max(ans, cur.val)
        return ans