class TreeNode:
    """
    Class representing a node in a binary search tree.

    Attributes:
    - val: The value of the node.
    - left: The left child node.
    - right: The right child node.
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a new instance of the TreeNode class.

        Parameters:
        - val: The value of the node. Defaults to 0.
        - left: The left child node. Defaults to None.
        - right: The right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class BST:
    """
    Class representing a binary search tree.

    Attributes:
    - root: The root node of the binary search tree.
    """

    def __init__(self):
        """
        Initializes a new instance of the BST class.
        """
        self.root = None

    def insert(self, val):
        """
        Inserts a new node with the given value into the binary search tree.

        Parameters:
        - val: The value of the new node to be inserted.
        """
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        """
        Recursively inserts a new node with the given value into the binary search tree.

        Parameters:
        - val: The value of the new node to be inserted.
        - node: The current node being compared against for insertion.

        Returns:
        - None
        """
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def search(self, val):
        """
        Searches for a node with the given value in the binary search tree.

        Parameters:
        - val: The value to search for.

        Returns:
        - True if the value is found, False otherwise.
        """
        return self._search(val, self.root)

    def _search(self, val, node):
        """
        Recursively searches for a node with the given value in the binary search tree.

        Parameters:
        - val: The value to search for.
        - node: The current node being compared against for the search.

        Returns:
        - True if the value is found, False otherwise.
        """
        if not node:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)
