from typing import Any

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

        if node.left is None and node.right is None:
            node.data = None
            return

        if node.left is None and node.right is not None:
            node.data = node.right.data
            node.right = None
            return

        if node.right is None and node.left is not None:
            node.data = node.left.data
            node.left = None
            return

        

    def search(self, target: int) -> Any:
        if target is None:
            return

        if type(target) is not int:
            return

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

    test.insert(7)
    test.insert(2)
    test.insert(3)

    print(test.__display__())

    print(test.search(1))
    print(test.search(5).data)
    print(test.search(7).data)
    print(test.search(7).data)

