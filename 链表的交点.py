'''
寻找两个单项链表的交点
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 在确认有交点的情况下，查找两个链表的交点 用栈 或者比较长度
    def findJiaoDian(self, l1: ListNode, l2: ListNode) -> ListNode:
        def sol1(l1, l2):
            len1, len2, h1, h2 = 0, 0, l1, l2
            while h1.next:
                h1 = h1.next
                len1 += 1
                pass
            while h2.next:
                h2 = h2.next
                len2 += 1
            if len1 > len2:
                h1 = l1
                minus = len1 - len2
                while minus > 0:
                    minus -= 1
                    h1 = h1.next
                return h1
            elif len2 > len1:
                h2 = l2
                minus = len2 - len1
                while minus > 0:
                    minus -= 1
                    h2 = h2.next
                return h2
            else:
                h1, h2 = l1, l2
                while not (h1 is h2):
                    h1 = h1.next
                    h2 = h2.next
                return h1
            pass

        def sol2(l1, l2):
            h1, h2, stack1, stack2 = l1, l2, [], []
            while (h1 or h2):
                if h1:
                    stack1.append(h1)
                    h1 = h1.next
                if h2:
                    stack2.append(h2)
                    h2 = h2.next
            while (stack1[len(stack1) - 1] is stack2[len(stack2) - 1]):
                stack1.pop()
                stack2.pop()
            return stack1[len(stack1) - 1].next

        return sol2(l1, l2)
        pass

    # 查找两个链表是否有交点 用栈
    def checkJiaoDian(self, l1: ListNode, l2: ListNode) -> ListNode:
        def sol1(l1, l2):
            h1, h2, stack1, stack2 = l1, l2, [], []
            while (h1 or h2):
                if h1:
                    stack1.append(h1)
                    h1 = h1.next
                if h2:
                    stack2.append(h2)
                    h2 = h2.next
            return stack1[len(stack1) - 1] is stack2[len(stack2) - 1]

        return sol1(l1, l2)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

n1 = ListNode(1)
n2 = ListNode(2)
# n4 = ListNode(4)
n1.next = n2
n2.next = node3
sol = Solution()
# res = sol.mergeKLists([node1, n1])
res = sol.findJiaoDian(node1, n1)
print(res.val)

res = sol.checkJiaoDian(node1, n1)
print(res)
