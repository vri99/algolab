from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


    def find(self, data: Any) -> int | None:
        head: Node | None = self

        while head:
            if head.data[0] == data[0]:
                return head.data[1]
            head = head.next

        return None


    def append(self, data: Any) -> None:
        new_node: Node = Node(data)
        last = self

        while last.next:
            last = last.next

        last.next = new_node

    # Print Linked list chain
    def __repr__(self) -> str:
        if self.next is None:
            return self.data

        return f"{self.data} -> {self.next.__repr__()})"