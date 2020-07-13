#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,queue,level = [],[],0
        queue.append(root)
        while(len(queue)):
            size = len(queue)
            while(size):
                size -=1
                if(level>=len(res)):
                    res.insert(0,[])
                cur = queue.pop(0)
                res[0].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level+=1
        return res
            
        
# @lc code=end


node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

sol = Solution()
res = sol.levelOrderBottom(node3)
print(res)
