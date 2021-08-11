'''
Project 4
CECS 451 - AI
Professor Fahim
8/4/21
Mark Arias
Rifat Hasan
'''
from Graph.Graph import Graph
from pathlib import Path
from SearchAlgorithms.DFSRec import DFSRec
from SearchAlgorithms.DFSNodeColor import DFSNodeColor

# Converting maze to graph

output_folder = Path("Output/")
data_folder = Path("Data/TextData/")
data = data_folder / "map2.txt"

# build graph
g = Graph(data)
g.graph_build()
size = g.graph_length()

# g.graph_summary()
# print()

# graph with size and 5 verticies
# gets vertex from vertex list
# dfs = DFSNodeColor(g, size, g.get_vertex(3))

# with degree heuristic
dfs = DFSNodeColor(g, size, g.most_connected())
dfs.DFS_recursive()
