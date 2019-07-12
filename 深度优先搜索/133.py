# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        self.dic = {}  # store all the copy nodes: dic[node] = copy
        return self.dfs(node)

    def dfs(self, node):
        if not node in self.dic:
            self.dic[node] = Node(node.val, [])
            for n in node.neighbors:
                self.dic[node].neighbors.append(self.dfs(n))
        return self.dic[node]


if __name__ == '__main__':
    l1 = Node(1, [])
    l2 = Node(2, [])
    l3 = Node(3, [])
    l4 = Node(4, [])
    l1.neighbors = [l2, l4]
    l2.neighbors = [l1, l3]
    l3.neighbors = [l2, l4]
    l4.neighbors = [l1, l3]
    # l2.left = l3
    # l2.right = l4
    # l5.right = l6

    sol = Solution()
    max = sol.cloneGraph(l1)
    print(max)
