import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from visual_tree import animate_traversal

class Node:
    def __init__(self, key, color="#bbbbbb"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def build_heap_tree(heap):
    n = len(heap)
    nodes = [Node(heap[i]) for i in range(n)]

    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    
    return nodes[0] if nodes else None

def get_color_gradient(n):
    """Generate n colors ranging from dark to light."""
    base_color = np.array(mcolors.hex2color("#1296F0"))
    colors = [mcolors.to_hex((1 - i / n) * base_color) for i in range(n)]
    return colors

def dfs_collect_steps(node, colors, index, steps):
    if node:
        node.color = colors[index[0]]
        steps.append((node, node.color))  # Збираємо кроки для анімації
        index[0] += 1
        dfs_collect_steps(node.left, colors, index, steps)
        dfs_collect_steps(node.right, colors, index, steps)

def bfs_collect_steps(root, colors, steps):
    queue = [root]
    index = 0
    while queue:
        current = queue.pop(0)
        if current:
            current.color = colors[index]
            steps.append((current, current.color))  # Збираємо кроки для анімації
            index += 1
            queue.append(current.left)
            queue.append(current.right)

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання
if __name__ == "__main__":
    heap = [10, 7, 5, 3, 2, 4, 1]
    root = build_heap_tree(heap)

    print("Первинне дерево:")
    draw_tree(root)

    # Обхід в глибину
    colors_dfs = get_color_gradient(len(heap))
    dfs_steps = []
    dfs_index = [0]
    dfs_collect_steps(root, colors_dfs, dfs_index, dfs_steps)
    animate_traversal(dfs_steps)  # Анімація обходу в глибину

    # Обхід в ширину
    root = build_heap_tree(heap)  # Перезібрати дерево для нового обходу
    colors_bfs = get_color_gradient(len(heap))
    bfs_steps = []
    bfs_collect_steps(root, colors_bfs, bfs_steps)
    animate_traversal(bfs_steps)  # Анімація обходу в ширину
