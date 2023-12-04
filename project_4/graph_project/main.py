import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def bfs_shortest_path(graph, start, goal):
    # BASLANGICTAN HEDEFE..
    gecildi = set()
    kuyruk = deque([(start, [start])])

    while kuyruk:
        node, path = kuyruk.popleft()

        if node not in gecildi:
            neighbors = graph.neighbors(node)
            for neighbor in neighbors:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    kuyruk.append((neighbor, path + [neighbor]))

            gecildi.add(node)

    return None  # Hedef düğüme ulaşılamadı


graph = nx.DiGraph()

graph.add_node("S")
graph.add_node("Ü")
graph.add_node("P")
graph.add_node("H")
graph.add_node("A")
graph.add_node("N")
graph.add_node("Y")
graph.add_node("K")
graph.add_node("U")
graph.add_node("T")
graph.add_edge("S", "Ü", weight=2.0)
graph.add_edge("S", "P", weight=5.0)
graph.add_edge("S", "H", weight=7.0)
graph.add_edge("Ü", "A", weight=6.0)
graph.add_edge("P", "Y", weight=6.0)
graph.add_edge("P", "K", weight=4.0)
graph.add_edge("H", "U", weight=4.0)
graph.add_edge("H", "T", weight=1.0)

# metodu cagır.
shortest_path_nodes = bfs_shortest_path(graph, start="S", goal="T")

print(f"En kısa yol: {shortest_path_nodes}")
