#
# Recursive implementation of depth-first search
#
# Input:  a graph G = (V,E) in adjacency-list representation,
#         and a vertex s in V.
# Output: a vertex is reachable  from s iff it is marked
#         as "explored"
#
#         recursive_DFS
#         All vertices are marked "unexplored" prior to engaging algorithm.
#
#         mark s as explored
#         for each edge (s,v) is s adjacency list:
#           if v is unexplored:
#             recursive_DFS(G,v)

# A simple adjacency list for a test graph (the graph is directed)
#
# We use a dictionary structure:
#   node : list of adjacent nodes
#
graph = {                  # corresponding edges:
    'A' : ['B', 'C'],      # A-->B, A-->C
    'B' : ['D', 'E'],      # B-->D, B-->E
    'C' : ['F'],           # C-->F
    'D' : [],              # none
    'E' : ['F'],           # E-->F
    'F' : []               # none
}

explored_vertices = set() # set of explored vertices

def resursive_DFS(explored, graph, vertex):
    if vertex not in explored:
        print(vertex)
        explored.add(vertex)
        for neighbor in graph[vertex]:
            resursive_DFS(explored, graph, neighbor)

# test
resursive_DFS(explored_vertices, graph, 'A')
