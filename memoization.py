"""A simple memoization algorithm."""


def memoize(fn):
    """Implement memoization."""
    def memoized_function(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    cache = {}
    return memoized_function


@memoize
def fibonacci(n):
    return 0 if n == 0 \
        else 1 if n == 1 \
        else fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(95))
