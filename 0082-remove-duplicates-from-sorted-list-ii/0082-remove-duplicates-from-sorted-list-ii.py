class Solution:
    def deleteDuplicates(self,head):
        dummy=ListNode(0)
        dummy.next = head
        cur= head
        prev = dummy
        dup=False
        while cur!=None and cur.next!=None:
            if(cur.val == cur.next.val):
                cur=cur.next
                dup=True
            else:
                if dup:
                    prev.next=cur.next
                    cur = cur.next
                    dup=False
                else:
                    prev=cur
                    cur= cur.next
        if dup==1:
            prev.next=cur.next
            cur=cur.next
        return dummy.next