import sys


class Node:
    def __init__(self, level_node):
        self.char = ''
        self.level_pair = level_node
        self.parents_num = -10
        self.level_diff = -7


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class lvl_num_pair:
    def __init__(self, pair_lvl):
        self.pair_lvl = pair_lvl
        self.pair_num = -1


class QuadTree:

    def __init__(self):
        self.tree = []
        self.max_height = 0
        self.node_count = 0

    def add_node(self, node_instance):
        self.tree.append(node_instance)

    def print_leaf(self, leaf_print, max_tree_depth, tree_matrix, start_point):
        diff = max_tree_depth - getattr(leaf_print, 'level_pair.pair_lvl')

        edge_length = pow(2, diff - 1)

        initial_y = getattr(start_point, 'y')
        initial_x = getattr(start_point, 'x')
        for x in range(edge_length):
            for y in range(edge_length):
                tree_matrix[getattr(start_point, 'x')][getattr(start_point, 'y')] = leaf_print.char
                setattr(start_point, 'y', getattr(start_point, 'y') + 1)
            setattr(start_point, 'y', initial_y)
            setattr(start_point, 'x', getattr(start_point, 'x') + 1)

        if getattr(leaf_print, 'level_pair.pair_num') == 0:
            setattr(start_point, 'y', initial_y + edge_length)
            setattr(start_point, 'x', initial_x)

        elif getattr(leaf_print, 'level_pair.pair_num') == 1:
            setattr(start_point, 'x', initial_x + edge_length)
            setattr(start_point, 'y', initial_y)

        elif getattr(leaf_print, 'level_pair.pair_num') == 2:
            setattr(start_point, 'y', initial_y - edge_length)
            setattr(start_point, 'x', initial_x)

        elif getattr(leaf_print, 'level_pair.pair_num') == 3:

            if getattr(leaf_print, 'parents_num') == 2:
                if getattr(leaf_print, 'level_diff') != 0:
                    setattr(start_point, 'y', initial_y - (edge_length * pow(2, getattr(leaf_print, 'level_diff'))))
                    setattr(start_point, 'x', initial_x - (edge_length * pow(2, getattr(leaf_print, 'level_diff')) - 1))
                else:
                    setattr(start_point, 'y', initial_y - edge_length * 2)
                    setattr(start_point, 'x', initial_x - edge_length)

            elif getattr(leaf_print, 'parents_num') == 0:
                if getattr(leaf_print, 'level_diff') != 0:
                    setattr(start_point, 'y', initial_y + (edge_length * pow(2, getattr(leaf_print, 'level_diff'))))
                    setattr(start_point, 'x', initial_x - (edge_length * pow(2, getattr(leaf_print, 'level_diff')) - 1))
                else:
                    setattr(start_point, 'x', initial_x - edge_length)
                    setattr(start_point, 'y', initial_y + (2 * edge_length))

            elif getattr(leaf_print, 'parents_num') == 1:
                setattr(start_point, 'y', initial_y)
                setattr(start_point, 'x', initial_x + edge_length)
            elif getattr(leaf_print, 'parents_num') == 3:
                setattr(start_point, 'x', initial_x - pow(2, getattr(a, 'level_diff') + 1) - 1)
                setattr(start_point, 'y', initial_y - pow(2, getattr(a, 'level_diff') + 1))

        return start_point


if __name__ == '__main__':
    qt = QuadTree()
    start_po = Point(0, 0)
    max_depth = 0
    plus_count = 0
    level = 0
    number = 0
    removed_lvl_count = 0
    list_lvl = []
    po_num = 0
    current_pair = lvl_num_pair(0)
    list_systems_stack = []
    line = sys.stdin.readline().replace('\n', '')
    if len(line) == 1:
        print("".join(line[0]))
    else:
        for i in line:
            if i == '+':
                new_lvl = lvl_num_pair(level)

                pair = lvl_num_pair(level)
                current_pair = pair

                list_lvl.append(new_lvl)

                level += 1
                if max_depth < level:
                    max_depth = level
            else:
                a = Node(level)
                setattr(list_lvl[len(list_lvl) - 1], 'pair_num',
                        getattr(list_lvl[len(list_lvl) - 1], 'pair_num') + 1)
                setattr(a, 'level_pair.pair_lvl', getattr(list_lvl[len(list_lvl) - 1], 'pair_lvl'))
                setattr(a, 'level_pair.pair_num', getattr(list_lvl[len(list_lvl) - 1], 'pair_num'))
                setattr(a, 'char', i)

                po_num += 1
                removed_lvl_count = 0
                for bullshit in reversed(list_lvl):
                    if getattr(bullshit, 'pair_num') == 3:
                        level -= 1
                        list_lvl.pop()
                        removed_lvl_count += 1
                        if list_lvl:
                            setattr(list_lvl[len(list_lvl) - 1], 'pair_num',
                                    getattr(list_lvl[len(list_lvl) - 1], 'pair_num') + 1)

                if list_lvl:
                    setattr(a, 'parents_num', getattr(list_lvl[len(list_lvl) - 1], 'pair_num'))

                setattr(a, "level_diff", removed_lvl_count)

                qt.add_node(a)



    if len(qt.tree) !=0:
        matrix = [['0' for x in range(pow(2, max_depth))] for y in range(pow(2, max_depth))]
        for leaf in qt.tree:
            start_po = qt.print_leaf(leaf, max_depth, matrix, start_po)

        for row in matrix:
            print(''.join(row))
