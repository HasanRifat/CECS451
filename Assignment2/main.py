# Project 2
# Mark Arias
# ID : 012 416 064
# Rifat Hasan
# ID: 025538368
# CECS 451
# Code help contributions and sources:
# data structures in datastruct module courtesy of Arjang Fahim
# design of maze parsing and DFS / BFS courtesy of :
# favtutor.com
# geeksforgeeks.com
# learnpythonwithrune.org

# -------------------------------------------------------------------------
# import pandas as pd
# import numpy as np
import queue

# class and method definitions
# Definition of a graph object
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

    # this is professors method for constructing the graph
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

        # print("The number of nodes in the graph is: ", self.columns_count)

        for v in self.vert_dict.values():
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print("( %s , %s, %3d)" % (vid, wid, v.get_weight(w)))

        for v in self.vert_dict.values():
            print("g.vert_dict[%s]=%s" % (v.get_id(), self.vert_dict[v.get_id()]))


# -------------------[End of class]-------------------------


class Vertex:
    """ keeps a node information """

    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + " adjacent: " + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


# -------------------[End of class]--------------------------------

# maze loader from input file
def load_maze(file_name):
    f = open(file_name)
    maze = f.read()
    f.close()
    return maze


# convert maze into readable array
def convert_maze(maze):
    converted_maze = []
    lines = maze.splitlines()
    for line in lines:
        converted_maze.append(list(line))
    return converted_maze


# make the maze print in a readable way
def print_maze(maze):
    for row in maze:
        for item in row:
            print(item, end="")
        print()


# find the starting point of the maze
def find_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "P":
                return row, col


# find the end point of the maze
def find_endpoint(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == ".":
                return row, col


# helper method to check for valid position
def is_valid_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] in " .":  # adding a space before the . got this to work
        return True
    return False


# method to solve an input maze via a stack ( dfs search)
def solve_maze_dfs(maze, start):
    # use python list as stack
    stack = []
    numNodes = 0
    fringe = 0
    # add entry point (as tuple)
    stack.append(start)

    # go through stack as long as there are elements
    while len(stack) > 0:
        nodesExpanded = 0
        nodesExpanded = len(stack) + nodesExpanded
        pos_r, pos_c = stack.pop()  # pop out coordinates from the stack of tuples
        fringe += 1
        print("Current Position", pos_r, pos_c)

        if maze[pos_r][pos_c] == ".":  # end of maze reached
            print("Maze end reached")
            print("Path cost: " + str(numNodes))
            print("Nodes Expanded: " + str(nodesExpanded))
            print("Maximum Size of Fringe: " + str(fringe))
            return True

        if maze[pos_r][pos_c] == "+":
            # already visited location
            continue
        fringe += 1
        # mark position as visited
        maze[pos_r][pos_c] = "+"
        numNodes += 1
        # check for all possible positions to move to, and add to stack if possible
        if is_valid_position(maze, pos_r - 1, pos_c):  # check left
            stack.append((pos_r - 1, pos_c))
            fringe += 1
        if is_valid_position(maze, pos_r + 1, pos_c):  # check right
            stack.append((pos_r + 1, pos_c))
            fringe += 1
        if is_valid_position(maze, pos_r, pos_c - 1):  # check down
            stack.append((pos_r, pos_c - 1))
            fringe += 1
        if is_valid_position(maze, pos_r, pos_c + 1):  # check up
            stack.append((pos_r, pos_c + 1))
            fringe += 1

        # to follow the maze

        print("Stack:", stack)
        print_maze(maze)
        fringe += 1
    # path not found
    return False


# BFS search method for maze
def solve_maze_bfs(maze, start):

    numNodes = 0
    fringe = 0
    # create a queue for use in bfs
    queuebfs = queue.Queue()
    nodesExpanded = 0
    nodesExpanded = len(queuebfs.queue) + nodesExpanded
    queuebfs.put(start)  # put the starting position in the queue

    while not (queuebfs.empty()):

        pos_r, pos_c = queuebfs.get()
        fringe += 1
        print("Current Position", pos_r, pos_c)

        if maze[pos_r][pos_c] == ".":  # end of maze reached
            print("Maze end reached!")
            print("Path cost: " + str(numNodes))
            print("Nodes Expanded: " + str(nodesExpanded))
            print("Maximum Size of Fringe: " + str(fringe))
            return True

        if maze[pos_r][pos_c] == "+":
            # already visited location
            continue

        # mark current position as visited
        maze[pos_r][pos_c] = "+"
        numNodes += 1
        # check for all possible positions to move to, and add to queue if possible
        if is_valid_position(maze, pos_r - 1, pos_c):  # check left
            queuebfs.put((pos_r - 1, pos_c))
            fringe += 1
        if is_valid_position(maze, pos_r + 1, pos_c):  # check right
            queuebfs.put((pos_r + 1, pos_c))
            fringe += 1
        if is_valid_position(maze, pos_r, pos_c - 1):  # check up
            queuebfs.put((pos_r, pos_c - 1))
            fringe += 1
        if is_valid_position(maze, pos_r, pos_c + 1):  # check down
            queuebfs.put((pos_r, pos_c + 1))
            fringe += 1

        print("Current positions in queue:", queuebfs.qsize())
        print_maze(maze)

        # path not found
    return False


# Main code
if __name__ == "__main__":
    print("Project 2")

    # load in the maze
    maze = load_maze("mazes/smallMaze.lay")
    maze = convert_maze(maze)
    print_maze(maze)

    # find starting point of the maze
    start = find_start(maze)
    print("Starting coordinates: (Row, Column)  ** zero start index **")
    print(start)

    # find end point of the maze
    endPoint = find_endpoint(maze)
    print("End coordinates: (Row, Column)  ** zero start index **")
    print(endPoint)

    # solve the maze
    print(solve_maze_dfs(maze, start))