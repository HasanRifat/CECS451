import math


class Tree(object):
    def __init__(self):
        self.node_dict = {}
        self.num_node = 0
        self.root = None

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

    def max_value(state, a, b, depth):
        if (depth == 0):
            return state.value
        for s in state.children_list:
            a = max(a, min_value(s, a, b, depth-1))
            if a >= b:
                return a

    def min_value(state, a, b, depth):
        if (depth == 0):
            return state.value
        for s in state.children_list:
            b = min(b, max_value(s, a, b, depth-1))
            if b >= a:
                return b

    def minmax(self):
        self.minimax(self.root, 2, True, node=0)

    # start of normal minimax algorithm
    # TODO a way to find depth without hard coding it in
    # TODO implement DFS into function
    def minimax(self, root, depth, player, node):
        for i in depth:
            print(i)
        if (depth % 2) == 0:
            value = math.inf
            print("even (maximizing player)")
            for node in root.children_list:
                value = max(value, minimax(node, depth-1, False))
            return value

        else:
            print("odd (minimizing player)")
            value = math.inf
            for node in root.children_list:
                value = min(value, minimax(node, depth-1, True))
            return value

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

    def findDepth(node):
        if node is None:
            return 0
        else:
            leftDepth = findDepth(node.left)
            rightDepth = findDepth(node.right)

            if (leftDepth > rightDepth):
                return leftDepth + 1
            else:
                return rightDepth + 1


class Node:
    def __init__(self, id, parent_node, value):
        self.id = id
        self.parent_node = parent_node
        self.visited = False
        # list of successors
        self.children_list = []
        # holding value of nodes for every min/max layer
        self.value = value

        self.alpha = -math.inf
        self.beta = math.inf

        self.isPruned = False

    def setAlpha(self, a):
        self.alpha = a

    def setBeta(self, b):
        self.beta = b

    def getAlpha(self):
        return self.alpha

    def getBeta(self):
        return self.beta

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


t = Tree()
t.add_node("A", "", None)
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

# tree below
#             A
#       /     |     \
#   B         C        D
# 3 12 8    2 4 6   14 5 2

t.DFS_traversal()
# print(t.minmax())
