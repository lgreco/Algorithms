"""
Naive implementation of Dijkstra's shortest-path algorithm. This implementation
serves as a "conversation starter" to justify the need for using a min-heap, as
well as a more structured approach to capturing and representing a graph.
                                               leo@cs.luc.edu
"""

# The graph is modeled as a dict of dicts. The outer dict's key-value pairs
# are the graph vertices and their adjacency lists. The adjacency lists are
# dicts too, whose key-value pairs are the adjacent vertices and the length
# of the edge to them. For example, the key-value pair:
#       'A': { 'B':1, 'C':3 },
# means that vertex A has two adjacent vertices (B and C) and the lengths
# of the edges are 1 and 3 for A-B and A-C respectively.

graph = {
    'A': { 'B':1, 'C':3 },
    'B': { 'D':3},
    'C': { 'D':1, 'F':8},
    'D': { 'E':1},
    'E': { 'F':2},
    'F': {}
}
# TRY a different graph of your own. In the dict above, each line represents a vertex and
# its adjacency list:
#       'A': { 'B':1, 'C':3 }
#       ---  ----------------
#        |          |
#        |          +----------> Node B is adjacent to A and the edge A->B has length 1
#       This node                Node C is adjacent to A and the edge A->C has length 3
#       has an
#       adjacency
#       list described           =======================================================
#       by dict:                 | You may add another vertex adjacent to A; let's say |
#       { 'B':1, 'C':3 }         | that you want to add a vertex called K with an edge |
#       This adjacency           | from A->K of length 5. The dict entry for A will    |
#       dict (ok, list)          | become:                                             |
#       describes all the        |         'A': { 'B':1, 'C':3, 'K':5 }                |
#       outgoing edges           |                              ^^^^^                  |
#       emanating from           | You will also need to add an entry for node K in    |
#       vertex A.                | the adjacency dict:                                 |
#                                |         'K': {}                                     |
#                                | This says that vertex K has no outgoing edges. You  |
#                                | may add outgoing edges for K if you wish, as long   |
#                                | you pay attention to not create a cyclical graph.   |
#                                =======================================================



# Algorithm input: a graph in the dict-of-dicts representation and a starting vertex
# Algorithm output: a dict called distance, showing the distance of each vertex from the starting vertex.

starting_vertex = 'C'  # This can be any vertex in the graph. *** TRY A DIFFERENT VALUE AND SEE WHAT HAPPENS.

unvisited = set() # A set to contain all unvisited vertices
distance = {} # This will be the final product, listing distances from the starting vertex

import sys # we need this to access the value of the largest integer available in python
infinity = sys.maxsize; # The largest number available to represent infinity

# At the beginning we need to mark all vertices as not visited. We add them to the set unvisited.
# Also, we need to assign a distance value to them: 0 for the starting vertex, infinity for the rest.
for vertex in graph.keys():
    unvisited.add(vertex)
    if vertex == starting_vertex:
        distance[vertex] = 0;
    else:
        distance[vertex] = infinity

# Set up the main loop of the algorithm
current_vertex = starting_vertex
continue_loop = True

# The main loop
while continue_loop:
    neighbors = graph[current_vertex] # Find the adjacent vertices of the current vertex
    for neighbor in neighbors: # Look at each adjacent vertex
        if neighbor in unvisited: # If it has not been visited before
            # find its distance from the starting vertex through the current vertex
            new_distance = distance[current_vertex] + neighbors[neighbor]
            #              ------------------------   -------------------
            #              distance of current        # length of edge
            #              vertex from the            # from current vertex
            #              starting vertex            # to its adjacent vertex
            if new_distance < distance[neighbor]: # If computed distance less than what's stored
                distance[neighbor] = new_distance # Store newly computed distance for this adjacent node
    unvisited.remove(current_vertex) # Remove current vertex from unvisited.
    # select the next current vertex
    min = infinity
    for vertex in unvisited: # Searc through every vertex in unvisited
        if distance[vertex] < min: # Looking of the one with the smallest distance from the starting vertex
            current_vertex = vertex # Make it the current vertex
            min = distance[vertex] # And update the value of the shortest distance
    # At this point we have either a new current vertex (to continue the while loop) or
    # the set of unvisited vertices is empty, or if there are still vertices in it, they
    # remain at infinite distance from the starting vertex.
    if len(unvisited)==0 or min==infinity: # If no more unvisited vertices, or remaining ones at infinite distance
        continue_loop = False # Cause while loop to end

# Display results
print("\nDistances from starting point",starting_vertex)
for vertex in distance.keys():
    print("\tTo vertex", vertex,": ", end='')
    if distance[vertex] == infinity:
        print(u'\u221E') # Unicode for infinity symbol 221E
    else:
        print(distance[vertex])