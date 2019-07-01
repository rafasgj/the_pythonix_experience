"""A simple 'cons' implementation for Python, that you should never use."""


#
# Implementação de auxiliares para funções recursivas.
#

def car(data):
    """Return the first element."""
    assert type(data) == tuple and len(data) == 2
    return data[0]


def cdr(data):
    """Return the trailing elements."""
    assert type(data) == tuple and len(data) == 2
    return data[1]


def cons(x, y=None):
    """Construct a pair (x y)."""
    return (x, y)


def filter(data, fn):
    """Redefine Python 'filter', something you shouldn't do."""
    return None if data is None else \
        filter(cdr(data), fn) if fn(car(data)) \
        else cons(car(data), filter(cdr(data), fn))


def map(data, fn):
    """Apply a function to every element of a list."""
    if data is not None:
        fn(car(data))
        map(cdr(data), fn)


def iterator(data):
    """Obtain an iterator to the data."""
    if not data:
        raise StopIteration
    yield car(data)
    yield from cdr(data)


#
# Implementacao de uma lista encadeada recursiva.
#

def append(linkedlist, data):
    """Append data to the linkedlist."""
    return cons(data, None) if linkedlist is None \
        else cons(car(linkedlist), append(cdr(linkedlist), data))


def search(lst, key):
    """Search for key in the linkedlist."""
    return None if lst is None else \
        car(lst) if car(lst) == key else search(cdr(lst), key)


def remove(lst, key):
    """Remove all elements with key from the linked list."""
    return filter(lst, lambda cmp: cmp == key)


def ordered(lst, key):
    """Insert in a list maintaining its natural order."""
    return cons(key, lst) if lst is None or key < car(lst) else \
        cons(car(lst), ordered(cdr(lst), key))


#
# Implementacao de uma interface orientada a objetos,
# com processamento de stream, para a lista encadeada.
#

class LinkedList:
    """An OO interface to the linked list."""

    def __init__(self):
        """Initialize object."""
        self.data = None

    def append(self, data):
        """Append data."""
        self.data = append(self.data, data)
        return self

    def print(self):
        """Print list to standard output."""
        map(self.data, print)
        return self

    def remove(self, key):
        """Remove elements with hey."""
        self.data = remove(self.data, key)
        return self


# Testes
if __name__ == "__main__":
    ll = cons("Rafael")
    ll = append(ll, "Gustavo")
    ll = append(ll, "Bryan")
    ll = append(ll, "Roberto")
    print(ll)
    ll = remove(ll, "Roberto")
    print(ll)
    ll = append(ll, "Ivonei")
    print(ll)

    ll = LinkedList()
    ll.append("Rafael")\
        .append("Bryan")\
        .append("Roberto")\
        .append("Gustavo")\
        .print()\
        .remove("Rafael")\
        .print()

    ll = ordered(None, "Rafael")
    ll = ordered(ll, "Gustavo")
    ll = ordered(ll, "Bryan")
    ll = ordered(ll, "Roberto")
    ll = ordered(ll, "Marcelo")
    ll = ordered(ll, "Ivonei")
    print(ll)
