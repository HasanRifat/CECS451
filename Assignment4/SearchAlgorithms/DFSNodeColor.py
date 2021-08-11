# ----------------------------------------------------------------------------------------
#	Simulate DFS algorithm.
#   This version  of DFS, travers a graph in DFS order in recursive
#
#	(c) 2020 Arjang Fahim
#   Rifat Hasan
#   Mark Arias
#
#	Date: 4/10/2020
#	email: fahim.arjang@csulb.edu
#   version: 1.0.0
# ----------------------------------------------------------------------------------------
'''
This is the class to define the custom dfs traversal for the node coloring implementation
'''


class DFSNodeColor(object):

    def __init__(self, graph, size, start_node):

        self.graph = graph
        self.size = size
        # self.start_node = (self.graph.get_most_connected_node()).get_id()
        self.start_node = start_node

    def DFS_util(self, s):
        s.set_visited(True)

        # set the color of the node
        if len(s.color_wheel) != 0:
            # removes from dict and returns as a tuple
            s.color = s.color_wheel.popitem()
        else:
            print("No Colors Left")
            exit()

        # check consistency using MAC
        self.macAlgo(s)
        print(s.get_id(), '----->', s.color[1])

        # simple depth first search to iterate through nodes
        for v in s.adjacent:
            n = self.graph.get_vertex(v.get_id())
            if not n.get_visited():
                self.DFS_util(n)

    def DFS_util2(self, s):
        print(s.get_id())
        node = self.graph.get_vertex(s.get_id())
        for v in node.adjacent:
            n = self.graph.get_vertex(v.get_id())
            if n.get_visited() == False:
                self.DFS_util(n)

    def DFS_recursive(self):
        # s_node = self.graph.get_vertex(self.start_node)
        # self.DFS_util(s_node)
        self.DFS_util(self.start_node)

    # Maintaining Arc Consistency algorithm which updates each connected node after coloring
    def macAlgo(self, vert):
        for node in vert.get_connections():
            n = self.graph.get_vertex(node.get_id())
            # checks if color of vertex is already in color domain
            if vert.color[0] in n.color_wheel.keys():
                del n.color_wheel[vert.color[0]]


# ------------------------[End of DFS class]---------------------------------------------------
