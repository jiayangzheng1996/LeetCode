# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        carry = False
        prev = None
        head = None
        while p1 is not None or p2 is not None:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            val = val1 + val2 + carry
            if val >= 10:
                carry = True
                val -= 10
                tmp = ListNode(val=val)
            else:
                carry = False
                tmp = ListNode(val=val)
            if prev is None:
                prev = tmp
                head = tmp
            else:
                prev.next = tmp
                prev = tmp
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if carry:
            prev.next = ListNode(val=1)

        return head


def printlist(l: ListNode):
    p = l
    string = ''
    while p is not None:
        if p.next is None:
            string = string + str(p.val) + '\n'
        else:
            string = string + str(p.val) + " -> "
        p = p.next
    print(string)


def main():
    list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=ListNode(val=1))))
    list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    solution = Solution()
    printlist(solution.addTwoNumbers(list1, list2))


if __name__ == '__main__':
    main()
