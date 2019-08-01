class ListNode(object):
    # Inits a new node with the passed in value X as the .val and assigns .next to none
    def __init__(self, x):
        self.val = x
        self.next = None


class linked_list:
    # Inits a empty object with a single attribute .head set to none
    def __init__(self):
        self.head = None

    # This method calls ListNode to create a newNode with the passed in value, then it assigns the stored value of self.head to its newNode.next attr.
    # Then it assigns the newNode that was just created to self.head. So for the next time its called, the newNode.next of the newNode will
    # actully be the previous node that was made. Thus creating the linked_list in reverse.
    def prefixNode(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    # This method first assigns the value of self.head to currNode, then it checks to see if currNode is true or false. If false it calls ListNode to
    # create a new node with its passed value and assigns it to self.head. The next time this method is called currNode will not be false, it will be
    # the previous node created, causing it to hit our if condition as true. The while loop will run as long as the currNode.next value is not None,
    # (the purpose is to dig through the nodes until it finds the last one) it will then assign currNode.next to the currNode.
    # Finally it wall call ListNode created the next Node and assign its value to currNode.next.
    # This makes the first node created the head, and every node created after that, will be the next of the previous.
    def appendNode(self, val):
        currNode = self.head
        if currNode:
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = ListNode(val)
        else:
            self.head = ListNode(val)


class linkedSolution:
    def addTwoNumbers(self, l1, l2, c=0):
        output = linked_list()
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
            output.appendNode(Sum)
        return output.head
