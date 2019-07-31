class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        output = ListNode(0)
        temp = output
        while l1 != None and l2 != None:
            if l1 is None:
                first = 0
            else:
                first = l1.val
            if l2 is None:
                second = 0
            else:
                second = l2.val
            Sum = first + second + c
            if Sum > 9:
                c = 1
                Sum = Sum - 10
            else:
                c = 0
            l1 = l1.next
            l2 = l2.next
            hold = ListNode(Sum)
            temp.next = hold
            temp = temp.next
        return output.next


l1 = linked_list()
l1.addNode(2)
l1.addNode(4)
l1.addNode(3)

l2 = linked_list()
l2.addNode(5)
l2.addNode(6)
l2.addNode(4)

result = Solution().addTwoNumbers(l1.head, l2.head)
while result:
    print(result.val)
    result = result.next

# finished coding on 07/31/19
