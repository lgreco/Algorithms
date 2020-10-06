
# Topological sorting based on recursive DFS

# Iterative wrapper
def topological_sorting(graph):
    explored = set()
    for vertex in graph:
        if vertex not in explored:
            DFS_topo(explored, graph, vertex)

def DFS_topo(e, G, v):
    e.add(v)
    for adjacent_vertex in G[v]:
        if adjacent_vertex not in e:
            DFS_topo(e, G, adjacent_vertex)
    L.append(v)

# Example adjacency list
another_graph = {
    "wash dishes" : ["have lunch"],
    "cook food" : ["have lunch"],
    "go to grocery store" : [ "cook food"],
    "have lunch" : [],
    "wash laundry" : ["dry laundry"],
    "dry laundry" : ["fold laundry"],
    "fold laundry" : [],
    "separate laundry" : ["wash laundry"]
}

# simpler graph
simpler_graph = {
    'A' : [ 'B', 'C'],
    'B' : [ 'E'],
    'C' : [],
    'D' : [ 'E', 'F'],
    'E' : ['F'],
    'F' : []
}

L = []

topological_sorting(simpler_graph)
for task in range(len(L),0,-1):
    print(L[task-1])
