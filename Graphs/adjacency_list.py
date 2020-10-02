# A list of adjacency linked lists for a graph G = (V,E)


class Graph:

    # Create a graph for the number of vertices specified. The graph
    # object comprises a list with as many elements, initially set to None.
    #
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
    #
    def edge_between(self, source_vertex, destination_vertex):

        # Add destination to the adjacency list of the source node
        node = adjacency_node(destination_vertex)
        node.next = self.graph[source_vertex]
        self.graph[source_vertex] = node

        # Add source to the adjacency list of the destination node
        node = adjacency_node(source_vertex)
        node.next = self.graph[destination_vertex]
        self.graph[destination_vertex] = node


    # display routine
    #
    def display_adjacency_list(self):
        # loop over vertex
        for vertex_label in range(self.V):
            print("Vertex {} is adjacent to ".format(vertex_label), end=" ... ")
            # get the head vertex for this label
            current_vertex = self.graph[vertex_label]
            # follow the trail
            while current_vertex:
                print(" {} ".format(current_vertex.vertex), end="")
                current_vertex = current_vertex.next
            print(" \n")

                                #  JAVA EQV constructor for linked list Node.
class adjacency_node:           #  public Node(data) {
    def __init__(self, data):   #    this.vertex = data;
        self.vertex = data      #    next = null;
        self.next = None        #  }

# main()
if __name__ == "__main__":
    V = 4
    graph = Graph(V)
    graph.edge_between(0, 1)
    graph.edge_between(0, 2)
    graph.edge_between(1, 2)
    graph.edge_between(2, 3)

    graph.display_adjacency_list()
