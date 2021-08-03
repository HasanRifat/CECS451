# Project 3
# Mark Arias
# Rifat Hasan
# CECS 451

from forest_module import Tree
import csv


# -------------------------------------------------------------------------
# tree.txt file reader code

# load a tree layout file and return it
def load_tree_file(file_name):
    f = open(file_name)
    tree_file = f.read()
    f.close()
    return tree_file


# parse tree_file
def parse_tree_file(tree_file):
    parsed_tree = []
    lines = tree_file.splitlines()
    for line in lines:
        print(line)
    return parsed_tree


# build minimax tree from input file and return it
def build_minimax_tree(file_name):
    mini_max_tree = Tree()

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:

            # length of csv entries in the file
            row_length = len(row)
            # if player is max or minimzer is specified in entry 0
            player_type = row[0]
            # parent of nodes specified in entry 1
            parent_node = row[1]

            if row_length == 3:  # size of row length of row with root
                parsed_data = row[2]
                split_data = parsed_data.split("=")
                node = split_data[0]
                node_value = split_data[1]
                # add nodes to the tree in format ( node, parent, value of current node, player type)
                mini_max_tree.add_node(
                    node.strip(), "", node_value, player_type)
            else:                                           # all other conditions with multiple children nodes
                # this controls the range of iteration
                for i in range(2, row_length):
                    # take data entry from row i entry
                    temp_data = row[i]
                    # break apart input data spit by equals sign
                    temp_data_split = temp_data.split("=")
                    # take the node name
                    curr_node = temp_data_split[0]
                    curr_node_value = temp_data_split[1]    # take node value
                    # add nodes to the tree in format ( node, parent, value of current node, player type)
                    mini_max_tree.add_node(
                        curr_node.strip(), parent_node.strip(), curr_node_value, player_type)

    return mini_max_tree


# -------------------------------------------------------------------------
# main code
if __name__ == '__main__':
    print("Project 3")
    # file below just prints out contents of input txt file


    choice = 0
    while choice != 1 or 2:
        choice = int(input("\nEnter 1 or 2 for corresponding tree: "))

        if choice == 1:
            # loads corresponding file into program
            tree_file = load_tree_file("tree1.txt")
            print("****   Contents of input file   ****")
            # parses the text file to read and manipulate contents
            parse_tree_file(tree_file)
            print()
            mini_max_tree = build_minimax_tree("tree1.txt")
            # outputs the value and letter of each node based on DFS
            mini_max_tree.DFS_traversal()
            print("\nMinimax Algorithm:")
            # finds best move for player based on starting node, depth, and maximizing player
            best_move = mini_max_tree.minimax("A", 2, "max")
            break
        elif choice == 2:
            tree_file = load_tree_file("tree2.txt")
            print("****   Contents of input file   ****")
            parse_tree_file(tree_file)
            print()
            mini_max_tree = build_minimax_tree("tree2.txt")
            mini_max_tree.DFS_traversal()
            print("\nMinimax Algorithm:")
            best_move = mini_max_tree.minimax("A", 4, "max")
            break
        else:
            # asks user for another input if previous input was a wrong number
            print("Invalid entry, try again")
    # prints the best move based on user input
    print("Path values to best move possible: ")
    print(best_move)

    print("****    minimax algorithm with pruning    ****")
    if choice == 1:
        best_move_prune = mini_max_tree.pruning_minimax(
            "A", 2, -1000, 1000, "max")
    elif choice == 2:
        # need to pass in value for alpha and beta below, use -1000 and 1000 as proxies for plus/minus infinity
        best_move_prune = mini_max_tree.pruning_minimax(
            "A", 4, -1000, 1000, "max")
    print("Pruned algo best move: " + str(best_move_prune))
