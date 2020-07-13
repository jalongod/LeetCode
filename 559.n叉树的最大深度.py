#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # #深度优先
    # def maxDepth(self, root: 'Node') -> int:
    #     if not root:
    #         return 0
    #     res = self.dfs(root,1)
    #     return res
    # def dfs(self,node,d):
    #     maxd = d
    #     for n in node.children:
    #         maxd = max(maxd,self.dfs(n,d+1))
    #     return maxd
    
    # 广度优先
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue, res = [], 0
        queue.append(root)
        while queue:
            cnt = len(queue)
            res += 1
            for i in range(cnt):
                cur = queue.pop(0)
                for n in cur.children:
                    queue.append(n)
        return res
    
# @lc code=end

