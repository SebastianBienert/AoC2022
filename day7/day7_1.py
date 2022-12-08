
import os
import re 
input = [x.strip() for x in open("day7.txt", "r").readlines()]

CMD_TYPE = "CMD"
OUTPUT_TYPE = "OUTPUT"

FOLDER = "FOLDER"
FILE = "FILE"

def parse_command(line):
    line_split = line.split()
    cmd = line_split[1]
    args = line_split[2:]
    return (CMD_TYPE, cmd, args)


def parse_output(line):
    line_split = line.split()
    isFile = line_split[0].isnumeric()
    if isFile:
        size = int(line_split[0])
        name = line_split[1]
        return (OUTPUT_TYPE, name, size, FILE)
    else:
        name = line_split[1]
        return (OUTPUT_TYPE, name, 0, FOLDER)
    
parsed_input = [parse_command(x) if x.startswith('$') else parse_output(x) for x in input]

class Node:
    def __init__(self, path, type, parent, children, size):
        self.parent = parent
        self.children = children
        self.type = type
        self.path = path
        self.size = size
        
    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        size += self.size
        return size
  
def _get_children(start_index, data, parent):
    result = []
    pointer = start_index
    current_action = data[pointer]
    while current_action[0] == OUTPUT_TYPE:
        path = os.path.normpath((os.path.join(parent.path, current_action[1])))
        result.append(Node(path, current_action[3], parent, [], current_action[2]))
        pointer += 1
        if pointer < len(data):
            current_action = data[pointer]
        else:
            return result
    return result

def _find_node(node, path):
    if node == None:
        return None
    if node.path == path:
        return node
    elif node.children is None:
        return None
    else:
        for child in node.children:
            child_node = _find_node(child, path)
            if child_node is not None:
                return child_node
        return None
    
    
def _get_folder_sizes(node):
    if node == None:
        return []
    if node.type == FOLDER:
        if node.children is None:
            return [(node, node.get_size())]
        else:
            childrens = [(node, node.get_size())]
            for child in node.children:
                child_nodes = _get_folder_sizes(child)
                childrens.extend(child_nodes)
            return childrens
    return []
    
pointer = 0
current_path = ""
root = None

while pointer < len(parsed_input):
    action = parsed_input[pointer]
    if action[0] == CMD_TYPE:
        if action[1] == "cd":
            current_path = os.path.normpath(os.path.join(current_path, action[2][0]))
        if action[1] == "ls":
            node = _find_node(root, current_path)
            if node is None:
                node = Node(current_path, FOLDER, None, [], 0)
                
            children = _get_children(pointer + 1, parsed_input, node)
            node.children = children
            pointer += len(children)
            
            if root == None:
                root = node
            
    pointer += 1

folder_sizes = _get_folder_sizes(root)
filtered_folder_sizes = [folder for folder in folder_sizes if folder[1] <= 100000]
result = sum(x[1] for x in filtered_folder_sizes)
print(result)