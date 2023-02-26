Binary Search Tree
This code provides a class TreeNode representing a node in a binary search tree, and a class BST representing a binary search tree. The BST class has methods for inserting nodes and searching for nodes with a given value.

TreeNode
TreeNode has the following attributes:

val: The value of the node.
left: The left child node.
right: The right child node.
BST
BST has the following attribute:

root: The root node of the binary search tree.
BST has the following methods:

__init__
Initializes a new instance of the BST class.

insert
Inserts a new node with the given value into the binary search tree.

Parameters:

val: The value of the new node to be inserted.
_insert
Recursively inserts a new node with the given value into the binary search tree.

Parameters:

val: The value of the new node to be inserted.
node: The current node being compared against for insertion.
search
Searches for a node with the given value in the binary search tree.

Parameters:

val: The value to search for.
Returns:

True if the value is found, False otherwise.
_search
Recursively searches for a node with the given value in the binary search tree.

Parameters:

val: The value to search for.
node: The current node being compared against for the search.
Returns:

True if the value is found, False otherwise.
