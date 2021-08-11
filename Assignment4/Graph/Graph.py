
# ----------------------------------------------------------------------------------------
#	Constructs a graph data structure.
#
#	(c) 2020 Arjang Fahim
#   Rifat Hasan
#   Mark Arias
#
#	Date: 4/10/2020
#	email: fahim.arjang@csulb.edu
#   version: 1.0.0
# ----------------------------------------------------------------------------------------


import pandas as pd
from Data.LoadData import LoadData


class Graph(object):
    """ Constructs a graph data structure. """

    def __init__(self, data_file_path=""):

        ld = LoadData(data_file_path)
        self.data = ld.LoadData_Pandas()
        self.columns_count = ld.ColumnsCount()

        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def graph_length(self):
        return self.columns_count

    def graph_build(self):
        """ This method construct graph from a data file """

        for row in range(self.columns_count):
            self.add_vertex(row)
            for column in range(self.columns_count):
                if self.data.loc[row, column] != 0:
                    self.add_edge(row, column, self.data.loc[row, column])

    def add_vertex(self, node):

        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):

        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):

        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

        # The line below will be enabled if the graph is not directed
        # self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def graph_summary(self):
        print("\n****   Graph Summary   ****")
        print("The number of nodes in the graph is: ", self.columns_count)

        for v in self.vert_dict.values():
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                visited = w.get_visited()
                print('( %s , %s, %3d, %s)' %
                      (vid, wid, v.get_weight(w), visited))

        print("\n****   Adjacent Nodes  ****")
        for v in self.vert_dict.values():
            print('g.vert_dict[%s]=%s' %
                  (v.get_id(), self.vert_dict[v.get_id()]))

    # checks which node has the most connections for degree heuristic
    def most_connected(self):
        mostCnode = None
        neighborCount = 0
        for v in self.vert_dict.values():
            # add neighbor count if neighbor is found in connections
            if neighborCount < len(v.get_connections()):
                neighborCount = len(v.get_connections())
                mostCnode = v

        return mostCnode
# -------------------[End of class]-------------------------------------------------------


class Vertex:
    """ keeps a node information """

    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        # self.c_list = color_list.copy()
        self.color = None
        self.neighbor_count = 0
        # self.color_wheel = {3:'orange', 2: 'green', 1: 'blue', 0: 'red'}
        self.color_wheel = {2: 'green', 1: 'blue', 0: 'red'}
        # self.color_wheel = {1: 'blue', 0: 'red'}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
        self.neighbor_count = self.neighbor_count + 1

    # getters and setter methods
    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def set_visited(self, visited):
        self.visited = visited

    def set_color(self, color_id):
        self.color = color_id

    def get_color(self):
        return self.color

    def get_visited(self):
        return self.visited

    def get_neighbor_count(self):
        return self.neighbor_count

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
