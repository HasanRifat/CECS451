
# --------------------------------------------------------------------------------------------------------
# Tree data structure
class Tree(object):
    def __init__(self):

        self.node_dict = {}
        self.num_node = 0
        self.root = None

    def add_node(self, node_id, parent_id, value, player_type):
        if len(parent_id) == 0:
            parent = None
            new_v = Node(node_id, parent, value, player_type)
            self.root = new_v

        else:
            parent = self.node_dict[parent_id]
            new_v = Node(node_id, parent, value, player_type)
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

    def reset_visited_values_dfs(self, root):
        for node_item in root.children_list:
            if node_item.visited:
                self.reset_visited_values_dfs(node_item)
                node_item.visited = False

    def reset_util_dfs(self):
        print(" Visited values reset")
        self.reset_visited_values_dfs(self.root)

    def DFS_util(self, root):

        for node_item in root.children_list:
            if node_item.visited == False:
                self.DFS_util(node_item)
                node_item.visited = True

        print(root.get_id() + " [ " + root.get_value() + " ]")
        # print(root.get_value())

        return

    def DFS_traversal(self):
        print("****    DFS Traversal of Tree    ****")
        self.DFS_util(self.root)

    # minimax algorithm to return optimum player move in zero sum game
    def minimax(self, position, depth, maximizing_player):
        if depth == 0:  # reached base case, bottom of tree
            #print((self.node_dict[position].get_id() ) + ": " + str(self.node_dict[position].get_value()))
            return self.node_dict[position].get_value()

        if maximizing_player == "max":
            max_eval = -1000  # approx of - infinity
            node = self.node_dict[position]
            children = self.node_dict[position].get_children_node()
            for child in children:
                # print(child.get_id())
                # print(child.get_value())
                eval = self.minimax(child.get_id(), depth -
                                    1, child.get_player_type())
                max_eval = max(int(max_eval), int(eval))
                # print out values of max cases
                print(child.get_id() + "[ " + str(eval) + " ]")
            return max_eval

        else:
            min_eval = 1000  # approx of + infinity
            children = self.node_dict[position].get_children_node()
            for child in children:
                # print(child.get_id())
                eval = self.minimax(child.get_id(), depth -
                                    1, child.get_player_type())
                min_eval = min(int(min_eval), int(eval))
                # print out values of min cases
                print(child.get_id() + "[ " + str(eval) + " ]")
            return min_eval

    # minimax algorithm to return optimum player move in zero sum game, with node pruning
    def pruning_minimax(self, position, depth, alpha, beta, maximizing_player):
        if depth == 0:  # reached base case, bottom of tree
            return self.node_dict[position].get_value()

        if maximizing_player == "max":
            max_eval = -1000  # approx of - infinity
            children = self.node_dict[position].get_children_node()
            for child in children:
                eval = self.pruning_minimax(
                    child.get_id(), depth - 1, alpha, beta, child.get_player_type())
                max_eval = max(int(max_eval), int(eval))
                alpha = max(int(alpha), int(eval))
                if beta <= alpha:
                    print(child.get_id() + " [ Pruned ] ")
                    break
                # print out values of max cases
                print(child.get_id() + "[ " + str(eval) + " ] : not pruned")
            return max_eval

        else:
            min_eval = 1000  # approx of + infinity
            children = self.node_dict[position].get_children_node()
            for child in children:
                # print(child.get_id())
                eval = self.pruning_minimax(
                    child.get_id(), depth - 1, alpha, beta, child.get_player_type())
                min_eval = min(int(min_eval), int(eval))
                beta = min(int(beta), int(eval))
                if beta <= alpha:
                    print(child.get_id() + " [ Pruned ] ")
                    break
                # print out values of min cases
                print(child.get_id() + "[ " + str(eval) + " ] : not pruned")
            return min_eval


# --------------------------------------------------------------------------------------------------------
# class to represent a node within Tree Data struct
class Node:
    def __init__(self, id, parent_node, value, player_type):
        self.id = id
        self.player_type = player_type  # max or minimizing player label
        self.value = value
        self.parent_node = parent_node
        self.visited = False
        self.children_list = []

    def add_child(self, child_id, child_node):
        if child_id not in self.children_list:
            self.children_list.append(child_node)

    def get_id(self):
        return self.id

    # return the value stored at the node
    def get_value(self):
        return self.value

    # set value of node
    def set_value(self, val):
        self.value = val

    # return value of max or min player
    def get_player_type(self):
        return self.player_type

    def get_parent(self):
        return self.parent_node

    def get_children_node(self):
        return self.children_list
