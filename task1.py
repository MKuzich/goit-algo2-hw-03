import networkx as nx

G = nx.DiGraph()

edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

G.add_weighted_edges_from(edges, weight="capacity")

G.add_edge("Джерело", "Термінал 1", capacity=float("inf"))
G.add_edge("Джерело", "Термінал 2", capacity=float("inf"))

for i in range(1, 15):
    G.add_edge(f"Магазин {i}", "Сток", capacity=float("inf"))

flow_value, flow_dict = nx.maximum_flow(G, "Джерело", "Сток", flow_func=nx.algorithms.flow.edmonds_karp)

print("Максимальний потік:", flow_value)

results = []
for term in ["Термінал 1", "Термінал 2"]:
    for sklad in flow_dict[term]:
        for magaz in flow_dict[sklad]:
            flow = flow_dict[sklad][magaz]
            if "Магазин" in magaz and flow > 0:
                results.append((term, magaz, flow))

print("\nТермінал\tМагазин\t\tФактичний Потік (одиниць)")
for row in results:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}")