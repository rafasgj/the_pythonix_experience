"""A simple 'cons' implementation for Python, that you should never use."""

#-------------------
# Implementação de auxiliares para funções recursivas.
#-------------------

def car(data):
    """Return the first element."""
    assert type(data) == tuple and len(data) == 2
    return data[0]


def cdr(data):
    """Return the trailing elements."""
    assert type(data) == tuple and len(data) == 2
    return data[1]

def cons(x, y=None):
    return (x, y)

def filter(data, fn):
    """Redefine Python 'filter', something you shouldn't do. """
    return None if data is None else \
        filter(cdr(data), fn) if fn(car(data)) \
            else cons(car(data), filter(cdr(data), fn))

def map(data, fn):
    if data is not None:
        fn(car(data))
        map(cdr(data), fn)


#-------------------
# Implementacao de uma lista encadeada recursiva.
#-------------------

def append(linkedlist, data):
    return cons(data, None) if linkedlist is None \
        else cons(car(linkedlist), append(cdr(linkedlist), data))


def search(lst, key):
    return None if lst is None else \
        car(lst) if car(lst) == key else search(cdr(lst), key)


def remove(lst, key):
    return filter(lst, lambda cmp: cmp == key)


#-------------------
# Implementacao de uma interface orientada a objetos,
# com processamento de stream, para a lista encadeada.
#-------------------

class LinkedList:
    def __init__(self):
        self.data = None

    def append(self, data):
        self.data = append(self.data, data)
        return self

    def print(self):
        map(self.data, print)
        return self

    def remove(self, key):
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
