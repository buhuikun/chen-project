class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addLists(self, l1, l2):
        flag = 0
        fun = lambda x, y: x + y
        # 定义头节点
        head = tem = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                val = fun(l1.val, l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next

            if val + flag < 10:
                tem.next = ListNode(val + flag)
                flag_next = 0
            else:
                tem.next = ListNode(val + flag - 10)
                flag_next = 1
            flag = flag_next
            tem = tem.next
        if flag == 1:
            tem.next = ListNode(1)

        return head.next
l1 = 1
l2 = 2
a = Solution()
print(a.addLists(ListNode(243), ListNode(564)).val)

