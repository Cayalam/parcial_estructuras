import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_node("B")
G.add_node("C")

G.add_edge("A", "B", weight=3)
G.add_edge("B", "C")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "A")


nx.draw(G, with_labels=True, font_color="white", font_size=20, node_color="red", node_size=3000)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, edge_labels)
plt.margins(0.2)
plt.show()