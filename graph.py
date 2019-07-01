"""A small Graph API."""

import collections


class Graph:
    """Implement a simple Graph API."""

    def __init__(self, directed=False):
        """Inititalize an empty graph."""
        self._vertices = 0
        self._edges = []
        self._directed = directed

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self._vertices = v if v > self._vertices else self._vertices

    def remove_vertex(self, v):
        """Remove a vertex from the graph."""
        self._edges = [t for t in self._edges if t[0] != v and t[1] != v]

    def add_edge(self, v, u, w=1):
        """Add an edge to the graph."""
        self.remove_edge(v, u)
        self._edges.append((v, u, w))

    def remove_edge(self, v, u):
        """Remove an edge from the graph."""
        self._edges = [t for t in self._edges if t[0:2] != (v, u)]

    def adjacent(self, v, u):
        """Verify if two vertices are adjacent."""
        if self._directed:
            return bool([t for t in self._edges if t[0:2] == (v, u)])
        return bool([t for t in self._edges if t[0:2] == (v, u)
                     or t[0:2] == (u, v)])

    def neighbors(self, v):
        """Retrieve the list of neighbor vertices of a vertex."""
        result = [u for (t, u, _) in self._edges if t == v]
        if not self._directed:
            result.extend([u for (u, t, _) in self._edges if t == v])
        return result

    def dfs(self, v, fn=lambda u: u):
        """Apply a function fn to the vertices in a Depth First Search."""
        stack = []
        visited = set()
        stack.append(v)
        while stack:
            v = stack.pop()
            if v not in visited:
                for u in self.neighbors(v):
                    if v not in visited:
                        stack.append(u)
                fn(v)
                visited.add(v)

    def bfs(self, v, fn=lambda u: u):
        """Apply a function fn to the vertices in a Breadth First Search."""
        queue = collections.deque()
        visited = set()
        queue.append(v)
        while queue:
            v = queue.popleft()
            print("Neighbors:", v, self.neighbors(v))
            if v not in visited:
                for u in self.neighbors(v):
                    if v not in visited:
                        queue.append(u)
                fn(v)
                visited.add(v)

    def connected(self, v):
        L = []
        self.bfs(v, L.append)
        return L


if __name__ == "__main__":
    G = Graph()
    G.add_vertex(5)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 5)
    print(G.connected(5))
    G.dfs(1, print)