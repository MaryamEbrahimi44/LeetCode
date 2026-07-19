class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        return nodes[len(nodes) // 2]