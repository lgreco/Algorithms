# A list of adjacency lists for a graph G = (V,E)


class Graph:

    """
    Create a graph for the number of vertices specified. The graph
    object comprises a list with as many elements, initially set
    to None.
    """
    def __init__(self, how_many_vertices):
        self.V = how_many_vertices
        self.graph = [None] * self.V


    # Add an edge between two vertices ... this is a bit
    # tricky for an undirected graph, between any two adjacent
    # nodes force two entries, for example:
    #     A ---- edge ---- B
    # means that A is adjacent to B (therefore B needs to be
    # in A's adjacency list) and B is adjacent to A (therefore A
    # needs to be in B's adjacency list).

    def add_edge(self, source_vertex, destination_vertex):

        # Add destination to the adjacency list of the source node
        node = adjacency_node(destination_vertex)
        node.next = self.graph[source_vertex]
        print("Source node: ", source_vertex)
        print("Destination node: ", destination_vertex)
        if (node.next != None):
            print("Destination's .next points to node: ", node.next.vertex)
        self.graph[source_vertex] = node

        # Add source to the adjacency list of the destination node
        node = adjacency_node(source_vertex)
        node.next = self.graph[destination_vertex]
        self.graph[destination_vertex] = node


    # display routine

    def display_adjacency_list(self):
        for vertex in range(self.V):
            print("Vertex {} is adjacent to ".format(vertex), end=" ... ")
            temp = self.graph[vertex]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

class adjacency_node:           #  public Node(data) {
    def __init__(self, data):   #    this.vertex = data;
        self.vertex = data      #    next = null;
        self.next = None        #  }

# main()
if __name__ == "__main__":
    V = 3
    graph = Graph(V)
    graph.add_edge(0,1)
    graph.add_edge(0,2)

    graph.display_adjacency_list()
