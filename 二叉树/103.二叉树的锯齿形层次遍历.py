#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res,queue,level = [],[],0
        queue.append(root)

        while(len(queue)):
            sa = []
            for i in queue:
                if i:
                    sa.append(i.val)
            if len(sa):
                res.append(sa)

            subqueue = []
            while(queue):
                cur = queue.pop()
                if not cur:
                    continue
                if level%2==0: #当前队列为正序
                    subqueue.append(cur.right)
                    subqueue.append(cur.left)
                else: # 当前队列为逆序
                    subqueue.append(cur.left)
                    subqueue.append(cur.right)
            queue = subqueue
            level+=1

        return res
# @lc code=end


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

sol = Solution()
res = sol.zigzagLevelOrder(node1)
print(res)
