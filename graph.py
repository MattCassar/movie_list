import numpy as np

class Graph:
    def __init__(self, edges={}, vertices=set(), adjacency_matrix=None, vertex_to_index={}):
        self.edges = edges
        self.vertices = vertices
        self.adjacency_matrix = adjacency_matrix
        self.vertex_to_index = vertex_to_index
        self._out_of_sync = False


    def add_edge(self, edge):
        if len(edge) < 2 or len(edge) > 4:
            raise ValueError("Edge must have two or three entries")

        elif len(edge) == 2:
            v1, v2, w = edge[0], edge[1], 1

        elif len(edge) == 3:
            v1, v2, w = edge[0], edge[1], edge[2]

        if v1 not in self.edges:
            self.edges[v1] = {}
            self.vertices.add(v1)

        if v2 not in self.edges:
            self.edges[v2] = {}
            self.vertices.add(v2)

        if v2 in self.edges[v1]:
            raise ValueError("Edge from {} to {} already exists".format(v1, v2))

        if v1 in self.edges[v2]:
            raise ValueError("Edge from {} to {} already exists".format(v2, v1))

        self.edges[v1][v2] = w
        self.edges[v2][v1] = w
        self._out_of_sync = True


    def get_edge_weight(self, v1, v2):
        if v1 in self.edges:
            if v2 in self.edges[v1]:
                return self.edges[v1][v2]

        return None


    def create_adjacency_matrix(self):
        if not self._out_of_sync:
            return

        self.adjacency_matrix = np.zeros((len(self.vertices), len(self.vertices)))
        self.create_vertex_to_index()
        for v in self.vertices:
            for v2 in self.edges[v]:
                i, j = self.vertex_to_index[v], self.vertex_to_index[v2]
                w = self.edges[v][v2]
                self.adjacency_matrix[i, j], self.adjacency_matrix[j, i] = w, w

        self._out_of_sync = False


    def create_vertex_to_index(self):
        vertices = sorted(list(self.vertices))
        for i, vertex in enumerate(vertices):
            self.vertex_to_index[vertex] = i


    def update_edge(self, v1, v2, w):
        if not self._out_of_sync:
            i, j = self.vertex_to_index[v1], self.vertex_to_index[v2]
            self.adjacency_matrix[i, j], self.adjacency_matrix = w, w
        else:
            self._out_of_sync = True

        self.edges[v1][v2] = w
        self.edges[v2][v1] = w
