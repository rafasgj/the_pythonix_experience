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


def insert(bst, k):
    """Insert KEY in the binary search tree BST."""
    return (None, k, None) if bst is None else \
        (insert(left(bst), k), key(bst), right(bst)) if k <= key(bst) \
        else (left(bst), key(bst), insert(right(bst), k))


def search(bst, k):
    """Search for a KEY in the binary search tree BST."""
    return None if bst is None else key(bst) if k == key(bst) else \
        search(left(bst) if k < key(bst) else right(bst), k)


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


def preorder(bst, fn):
    return [] if bst is None else \
        [fn(key(bst))] + preorder(left(bst), fn) + preorder(right(bst), fn)


def inorder(bst, fn):
    return [] if bst is None else \
        inorder(left(bst), fn) + [fn(key(bst))] + inorder(right(bst), fn)


def postorder(bst, fn):
    return [] if bst is None else \
        postorder(left(bst), fn) + postorder(right(bst), fn) + [fn(key(bst))] 


def is_valid(bst):
    def valid_tree(bst, mink, maxk):
        return True if bst is None \
            else False if not (mink <= key(bst) < maxk) else \
            valid_tree(left(bst), mink, key(bst)) and \
            valid_tree(right(bst), key(bst), maxk)
    return valid_tree(bst, float("-INF"), float("+INF"))


if __name__ == "__main__":
    bst = None
    bst = insert(bst, 10)
    bst = insert(bst, 15)
    bst = insert(bst, 17)
    bst = insert(bst, 8)
    bst = insert(bst, 11)
    bst = insert(bst, 6)
    bst = insert(bst, 4)
    bst = insert(bst, 14)
    bst = insert(bst, 3)
    bst = insert(bst, 5)

    print(search(bst, 4))
    print(preorder(bst, lambda n: n))
    print(inorder(bst, lambda n: n))
    print(postorder(bst, lambda n: n))
    print(is_valid(bst))
