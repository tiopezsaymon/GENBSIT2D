
"""
Assessment 3.6: DFS Method in Tree
Name: TIOPEZ
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """Binary Tree for TIOPEZ."""
    root = TreeNode("T")

    root.left, root.right = TreeNode("I"), TreeNode("O")
    root.left.left, root.left.right = TreeNode("P"), TreeNode("E")
    root.right.left = TreeNode("Z")

    return root


def tree_dfs(node, order=None):
    """Preorder Traversal (DFS)."""

    if order is None:
        order = []

    if node is None:
        return order

    order.append(node.value)

    tree_dfs(node.left, order)
    tree_dfs(node.right, order)

    return order


if __name__ == "__main__":
    root = build_tree()

    print("=== Assessment 3.6: DFS Method in Tree ===")
    print("Name: TIOPEZ")
    print("DFS (preorder):", " -> ".join(tree_dfs(root)))
