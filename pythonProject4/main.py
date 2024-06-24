import pandas as pd
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

# Verileri yükleme
edges = pd.read_csv('asoiaf-all-edges.csv')
nodes = pd.read_csv('asoiaf-all-nodes.csv')

# Ağ oluşturma
G = nx.Graph()

# Düğümleri ekleme
for _, row in nodes.iterrows():
    G.add_node(row['Id'], label=row['Label'])

# Kenarları ekleme
for _, row in edges.iterrows():
    G.add_edge(row['Source'], row['Target'], weight=row['weight'])

# Topluluk algılama
communities = greedy_modularity_communities(G)
community_map = {node: idx for idx, community in enumerate(communities) for node in community}

# Düğüm özelliklerini belirleme
node_sizes = {node: sum(G[node][neighbor]['weight'] for neighbor in G.neighbors(node)) * 10 for node in G.nodes()}
nx.set_node_attributes(G, node_sizes, 'size')
nx.set_node_attributes(G, community_map, 'community')

# Büyük düğümleri kenarlara yerleştirme
positions = nx.spring_layout(G)
for node, size in node_sizes.items():
    if size > 100:  # Büyük düğümleri belirlemek için bir eşik değeri
        if positions[node][0] > 0:
            positions[node][0] = 1
        else:
            positions[node][0] = -1
        if positions[node][1] > 0:
            positions[node][1] = 1
        else:
            positions[node][1] = -1

# Pozisyon verilerini düz liste olarak saklama
positions_list = {node: position.tolist() for node, position in positions.items()}
nx.set_node_attributes(G, positions_list, 'pos')

# Pozisyon verilerini GEXF formatına uygun hale getirme
positions_list_str = {node: f"{position[0]},{position[1]}" for node, position in positions_list.items()}
nx.set_node_attributes(G, positions_list_str, 'pos')

# GEXF dosyasını kaydetme
nx.write_gexf(G, 'got_network.gexf')