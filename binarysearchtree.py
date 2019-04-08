"""Implements a Binary Search Tree using one line functions."""

from collections import namedtuple


_bst_node = namedtuple("bst_node", "left right key")


def left(node):
    """Get the left element of a BST node."""
    return node[0]


def right(node):
    """Get the right element of a BST node."""
    return node[2]


def key(node):
    """Get the key element of a BST node."""
    return node[1]


def insert(bst, key):
    """Insert KEY in the binary search tree BST."""
    return (None, key, None) if bst is None else \
        (insert(left(bst), key), key(bst), right(bst)) if key <= key(bst) \
        else (left(bst), key(bst), insert(right(bst), key))


def search(bst, key):
    """Search for a KEY in the binary search tree BST."""
    return None if bst is None else \
        key(bst) if key == key(bst) else \
        search(left(bst), key) if key < key(bst) else search(right(bst), key)


def max(bst):
    """Retrieve the maximum value of the binary search tree BST."""
    return key(bst) if right(bst) is None else max(right(bst))


def min(bst):
    """Retrieve the minimum value of the binary search tree BST."""
    return key(bst) if left(bst) is None else min(left(bst))


def repr(bst):
    """Get a string represenation of the binary search tree BST."""
    return "_" if bst is None \
        else "({} {} {})".format(bst.key, repr(bst.left), repr(bst.right))


def remove(bst, key):
    """Remove a node with the given key."""
    return None if bst is None else \
        None if left(bst) is None and right(bst) is None else \
        right(bst) if left(bst) is None and key == key(bst) else \
        left(bst) if right(bst) is None and key == key(bst) else \
        (left(bst), min(right(bst)), remove(right(bst), min(right(bst)))) \
        if key == key(bst) else \
        (remove(left(bst), key), key(bst), right(bst)) \
        if key < key(bst) else (left(bst), key(bst), remove(right(bst), key))
