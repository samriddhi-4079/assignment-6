
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def display_levelwise(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print()


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def leaf_nodes(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end=" ")

        leaf_nodes(root.left)
        leaf_nodes(root.right)


# Main Program
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Original BST:")
display_levelwise(root)

print("New Tree:")
display_levelwise(root)

print("Height of BST:", height(root))

print("Leaf Nodes:")
leaf_nodes(root)
print()
