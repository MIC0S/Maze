import os
from colored import fore
from time import sleep


def cls():
    os.system('clear')  # 'cls' if os.name in ('nt', 'dos') else 'clear'


class Node:
    def __init__(self, parent=None, position=None):
        self.parent, self.position = parent, position
        self.g, self.h, self.f = 0, 0, 0

    def __eq__(self, other): return self.position == other.position


class AStar:
    def __init__(self):
        pass

    def move(self, maze, start, end):
        return self.path(maze, start, end)[1]

    def path(self, maze, start, end):
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = [start_node]
        closed_list = []

        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
            children = []
            children_coords = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze) - 1) or \
                        node_position[1] < 0:
                    continue
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
                new_node = Node(current_node, node_position)
                children.append(new_node)
                children_coords.append(node_position)
            for child in children:
                if child in closed_list:
                    continue
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                open_list.append(child)

    def path_render(self, maze, start, end):

        print(f"{start} / {end}")
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = [start_node]
        closed_list = []

        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                print(path[::-1])
                return path[::-1]
            children = []
            children_coords = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze) - 1) or \
                        node_position[1] < 0:
                    continue
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
                new_node = Node(current_node, node_position)
                children.append(new_node)
                children_coords.append(node_position)
            for child in children:
                if child in closed_list:
                    continue
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue
                open_list.append(child)
            '''
            display = ''
            for i in range(len(maze[0])):
                for j in range(len(maze[0])):
                    if Node(None, (i, j)) in closed_list and Node(None, (i, j)) in open_list:
                        display += f"{fore.YELLOW}B "
                    elif Node(None, (i, j)) in closed_list:
                        display += f"{fore.YELLOW}C "
                    elif Node(None, (i, j)) in open_list:
                        display += f"{fore.BLUE}O "
                    elif maze[i][j] == 1:
                        display += f"{fore.RED}# "
                    elif maze[i][j] == 0:
                        display += f"{fore.WHITE}  "
                    else:
                        display += f"{fore.WHITE}& "
                display += '\n'
                
            sleep(0.1)
            cls()
            
            print(f"{fore.WHITE}{display}\nClosed:{len(closed_list)} / Opened:{len(open_list)}\n{fore.WHITE}{current_node.position}\n{children_coords}")
            '''
