
"""
   A  B  C  D  E  F
A  -  1  3  -  -  -
B  -  -  -  3  -  -
C  -  -  -  1  -  8
D  -  -  -  -  1  -
E  -  -  -  -  -  2
F  -  -  -  -  -  -
"""

graph = {
    'A': { 'B':1, 'C':3 },
    'B': { 'D':3},
    'C': { 'D':1, 'F':8},
    'D': { 'E':1},
    'E': { 'F':2},
    'F': {}
}

# narrate the graph
for vertex in graph.keys():
    print("Node", vertex,"has the following neighbors: ", end="")
    neighbors = graph[vertex]
    for neighbor in neighbors:
        print("vertex",neighbor, "at distance", neighbors[neighbor], end="; ")
    print()

# initiate the algorithm:
# declare starting vertex;
# mark all vertices as unvisited;
# set all distances from starting vertex to infinity.

import sys
starting_vertex = 'B'
unvisited = set()
distance = {}
infinity = sys.maxsize

for vertex in graph.keys():
    unvisited.add(vertex)
    if ( vertex == starting_vertex):
        distance[vertex] = 0
    else:
        distance[vertex] = infinity

# prepare for the loop
current_vertex = starting_vertex
continue_loop = True

while continue_loop:
    neighbors = graph[current_vertex]
    for neighbor in neighbors:
        if neighbor in unvisited:
            new_distance = distance[current_vertex] + neighbors[neighbor]
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
    unvisited.remove(current_vertex)
    min = sys.maxsize
    for vertex in unvisited:
        if distance[vertex] < min:
            current_vertex = vertex
            min = distance[vertex]
    if len(unvisited)==0 or min==sys.maxsize:
        continue_loop=False

print()
print(distance)