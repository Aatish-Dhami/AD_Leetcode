carry = 0
head = None
curr = None

while l1 is not None or l2 is not None:
    sum = carry
    if l1 is not None:
        sum += l1.val
        l1 = l1.next
    if l2 is not None:
        sum += l2.val
        l2 = l2.next
    node = ListNode(sum%10)
    carry = sum // 10

    if curr is None:
        curr = head = node
    else:
        curr.next = node
        curr = curr.next

if carry>0:
    curr.next = ListNode(carry)
return head
