from typing import Any

# Restriction: cannot delete root element at the current implementation
class BSTree:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: BSTree | None = None
        self.right: BSTree | None = None
        self.parent: BSTree | None = None

    def insert(self, value: int) -> None:
        node: BSTree = BSTree(value)
        node.parent = self

        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node.data)
        elif node.data > self.data:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node.data)
        else:
            return

    def delete(self, target: int) -> None:
        node: BSTree | None = self.search(target)

        if node is None:
            return

        # Case #1: node with no child -> just delete it
        if node.left is None:
            # Case 1 & 2 (No left child or no children)
            self.transplant(node, node.right)
        elif  node.right is None:
            # Case 2 (No right child)
            self.transplant(node, node.left)
        else:
            right_leftmost: BSTree | None = node.right.find_leftmost()
            if right_leftmost is not None:
                if right_leftmost.parent.data != node.data:
                    self.transplant(node, right_leftmost.right)
                    right_leftmost.right = node.right
                    right_leftmost.right.parent = node
                self.transplant(node, right_leftmost)
                right_leftmost.left = node.left
                right_leftmost.left.parent = node

    def find_leftmost(self) -> BSTree | None:
        if self.left is None:
            return self
        return self.left.find_leftmost()

    def transplant(self, u, v):
        if u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def search(self, target: int) -> Any:
        if target is None or type(target) is not int:
            return None

        if self.data == target:
            return self

        if target < self.data:
            if self.left is not None:
                return self.left.search(target)
            return None

        elif target > self.data:
            if self.right is not None:
                return self.right.search(target)
            return None

        else:
            return None

    def __display__(self, level=2):
        result = " " * level + str(self.data) + "\n"
        if self.left:
            result += self.left.__display__(level - 2)
        if self.right:
            result += self.right.__display__(level + 2)
        return result

if __name__ == "__main__":
    test = BSTree(5)
    test.insert(3)
    test.insert(7)
    test.delete(5)
    print(test.__display__())

