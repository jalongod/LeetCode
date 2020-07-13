'''
133. 克隆图
给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）。

'''


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        lookup = {}

        def process(node):
            if not node:
                return None
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(process(n))
            return clone

        return process(node)


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            # print(node.val)
            if not node:
                return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)


sol = Solution()
n1 = Node(1, [])
n2 = Node(2, [])
n3 = Node(3, [])
n4 = Node(4, [])
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]
max6 = sol.cloneGraph(n1)
print('=======' + max6)
