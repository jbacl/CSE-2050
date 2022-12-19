class Graph_ES:
    def __init__(self, V=(), E=()):
        self._V = set()
        self._E = set()

        for v in V: self.add_vertex(v)
        for (u, v) in E: self.add_edge((u, v))

    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        self._V.add(v)

    def remove_vertex(self, v):
        if v not in self._V:
            raise KeyError("This vertex not in graph")

        self._V.remove(v)

    def add_edge(self, e):
        self._E.add(e)
    
    def remove_edge(self, e):
        if e not in self._E:
            raise KeyError("This edge not in graph")

        self._E.remove(e)
    
    def vertices(self):
        return iter(self._V)

    def edges(self):
        return iter(self._E)

    def _neighbors(self, v):
        n_set = set()
        for (u, w) in self.edges():
            if u == v:
                n_set.add(w)

        return n_set


class Graph_AS:
    def __init__(self, V=(), E=()):
        self._V = set()
        self._nbrs = {}

        for v in V: self.add_vertex(v)
        for e in E: self.add_edge(e)

    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def remove_vertex(self, v):
        if v not in self._V:
            raise KeyError("This vertex not in graph")

        self._V.remove(v)

    def add_edge(self, e):
        self._nbrs[e[0]].add(e[1])
    
    def remove_edge(self, e):
        if e[1] not in self._nbrs[e[0]]:
            raise KeyError("This edge not in graph")

        self._nbrs[e[0]].remove(e[1])

    def vertices(self):
        return iter(self._V)
    
    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield (u, v)

    def _neighbors(self, v):
        return iter(self._nbrs[v])
