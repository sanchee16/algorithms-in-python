"""Code for binary tree."""


class Node:
    """Class defines a node that forms the basic structure of a tree."""

    def __init__(self, value, left, right):
        """Initialise the node's value and the value of it's left and right."""
        self.key = value
        self.left = left
        self.right = right

    def get_node(self):
        """Return node's value and the value of it's left and right."""
        return [self.key, self.left, self.right]


class BinaryTree:
    """Class defines a Binary tree."""

    def __init__(self, elements):
        """Initialise the tree and values."""
        self.values = elements

    def get_binary_tree(self):
        """Yield the binary tree values."""
        for i in range(0, (len(self.values) / 2)):
            node = Node(
                self.values[i],
                self.values[i * 2 + 1],
                self.values[i * 2 + 2]
            )
            yield node.get_node()

    def get_binary_tree_as_list(self):
        """Return the binary tree as a list."""
        return list(self.get_binary_tree())
