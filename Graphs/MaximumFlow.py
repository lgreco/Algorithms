import collections

class Graph(object):
    """Instantiates a graph object based on an adjacency matrix supplied
    in the form of a list of lists."""

    def __init__(self, adjacency_matrix):
        self.graph = adjacency_matrix  # residual graph
        self.row = len(adjacency_matrix)

    def bfs(self, s, t, path):
        """
        Breadth-first search of the graph.
        Returns true if there is a path from source 's' to sink 't' in
        residual graph. The path is stored in path[]"""

        # Mark all the vertices as not visited
        visited = [False] * self.row

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    path[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    # Returns the maximum flow from s to t in the given graph
    def Ford_Fulkerson(self, source, target):

        # This array is filled by BFS and to store path
        s_t_path = [-1] * self.row

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, target, s_t_path):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = target
            while s != source:
                # the path flow is the capacity of the edge with the min capacity.
                path_flow = min(path_flow, self.graph[s_t_path[s]][s])
                s = s_t_path[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = target
            while v != source:
                u = s_t_path[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = s_t_path[v]

        return max_flow

# Sample adjacency matrix given as a list of lists; one list per node;
# the list contains the edge capacities from the node to the other nodes.
# For example, the second element of the 3rd list is the capacity of
# the edge from node(2) to node(1).

# Node:   0   1   2   3   4   5   # node
graph = [[0, 16, 13,  0,  0,  0], # 0
         [0,  0, 10, 12,  0,  0], # 1
         [0,  4,  0,  0, 14,  0], # 2
         [0,  0,  9,  0,  0, 20], # 3
         [0,  0,  0,  7,  0,  4], # 4
         [0,  0,  0,  0,  0,  0]] # 5

# Instantiate a Graph object using the adjacency list above
g = Graph(graph)

# Declare source and target vertices
source = 0; # source
target = 5; # target

# compute the maximum flow between source and target
mf = g.Ford_Fulkerson(source, target)
print(mf)