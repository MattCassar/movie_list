from graph import Graph

g = Graph()
vertices = list("abcdefghijklmnopqrstuvwxyz")

g.add_edge(("a", "b", 3))
g.add_edge(("a", "c", 1))
g.add_edge(("b", "d", 4))
g.add_edge(("b", "c", 2))
g.add_edge(("c", "c", 1))
g.add_edge(("d", "d", 3))
g.create_adjacency_matrix()
g.add_edge(("a", "e", .5))
g.create_adjacency_matrix()
print(g.adjacency_matrix)