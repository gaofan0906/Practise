# 二叉树的镜像
# 递归

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        # write code here