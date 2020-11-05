
# Topological sorting based on recursive DFS
# (Homework #5: find the bug)

# Iterative wrapper
def topological_sorting(graph):
    explored = set()
    for vertex in graph:
        if vertex not in explored:
            DFS_topo(explored, graph, vertex)

# Recursive ordering
def DFS_topo(e, G, v):
    e.add(v) # mark vertex v as explored
    for adjacent_vertex in G[v]: # go through v's adjacency list
        if adjacent_vertex not in e: # if adjacent node not explored
            DFS_topo(e, G, adjacent_vertex) # recurse
    L.append(v) # add vertex to ordering stack

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
    'B' : [ 'D'],
    'C' : ['D'],
    'D' : []
}

#yet another graph
yag = {
    'F': [],
    'B' : ['C'],
    'C' : ['D', 'E'],
    'D' : ['E'],
    'E' : [],
    'A': ['B', 'C']
}

L = []

topological_sorting(yag)
for task in range(len(L),0,-1):
    print(L[task-1])
