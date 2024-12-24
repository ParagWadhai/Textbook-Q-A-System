from anytree import Node, RenderTree
import json

def create_hierarchical_tree():
    """Creates a hierarchical tree for a textbook."""
    root = Node("Textbook")
    chapter1 = Node("Chapter 1: Introduction", parent=root)
    Node("Section 1.1: Basics", parent=chapter1)
    Node("Section 1.2: Advanced Topics", parent=chapter1)
    chapter2 = Node("Chapter 2: Applications", parent=root)
    Node("Section 2.1: Case Study", parent=chapter2)
    return root

def serialize_tree(root_node, output_file):
    """Saves a hierarchical tree as a JSON file."""
    def node_to_dict(node):
        return {
            "name": node.name,
            "children": [node_to_dict(child) for child in node.children]
        }
    tree_dict = node_to_dict(root_node)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(tree_dict, file, indent=4)
