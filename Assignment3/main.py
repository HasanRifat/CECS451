import math

class Tree(object):
    def __init__(self):
        self.node_dict = {}
        self.num_node = 0
        self.root = None
        # self.value = None

    def add_child(self, child_id, child_node):
        if child_id not in self.children_list:
            self.children_list.append(child_node)

    def add_node(self, node_id, parent_id, value):
        if len(parent_id) == 0:
            parent = None
            new_v = Node(node_id, parent, value)
            self.root = new_v
        else:
            parent = self.node_dict[parent_id]
            new_v = Node(node_id, parent, value)
            parent.add_child(node_id, new_v)

        self.node_dict[node_id] = new_v
        self.num_node += 1

    def get_node(self, node_id):
        if node_id in self.node_dict:
            return self.node_dict[node_id]
        else:
            return None

    def get_nodes(self):
        return self.node_dict.keys()
        
    # start of normal minimax algorithm
    def minimax():
        pass
    
    # start of minimax algorithm with pruning
    def minimax_prune():
        pass

    def DFS_util(self, root):
        for node_item in root.children_list:
            if node_item.visited == False:
                self.DFS_util(node_item)
                node_item.visited = True

        print(root.get_id())

        return

    def DFS_traversal(self):
        self.DFS_util(self.root)


class Node:
    def __init__(self, id, parent_node, value):
        self.id = id
        self.parent_node = parent_node
        self.visited = False
        self.children_list = []
        # holding value of nodes for every min/max layer
        self.value = value 

        self.alpha = -math.inf
        self.beta = math.inf

        self.isPruned = False

    def add_child(self, child_id, child_node):
        if child_id not in self.children_list:
            self.children_list.append(child_node)

    def get_id(self):
        return self.id

    def get_parent(self):
        return self.parent_node

    def get_children_node(self):
        return self.children_list

    def get_children_id(self):
        return self.id

    def get_parent(self):
        return self.parent_node
t = Tree()
t.add_node("A", "", None) # can represent as max or min
t.add_node("B", "A", None)
t.add_node("C", "A", None)
t.add_node("D", "A", None)
t.add_node("B1", "B", 3)
t.add_node("B2", "B", 12)
t.add_node("B3", "B", 8)
t.add_node("C1", "C", 2)
t.add_node("C2", "C", 4)
t.add_node("C3", "C", 6)
t.add_node("D1", "D", 14)
t.add_node("D2", "D", 5)
t.add_node("D3", "D", 2)

t.DFS_traversal()