"""Impements a binary search tree with one line methods."""


def left(node):
    """Retrieve the left node of a binary tree node."""
    return node[0]


def right(node):
    """Retrieve the right node of a binary tree node."""
    return node[2]


def key(node):
    """Retrieve the key value of a binary tree node."""
    return node[1]


def insert(bst, k):
    """Insert a key in a Binary Search Tree."""
    return (None, k, None) if bst is None \
        else (insert(left(bst), k), key(bst), right(bst)) if k < key(bst) \
        else (left(bst), key(bst), insert(right(bst), k))


def search(bst, k):
    return None if bst is None else bst if k == key(bst) \
        else search(left(bst), k) if k < key(bst) \
        else search(right(bst), k)


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