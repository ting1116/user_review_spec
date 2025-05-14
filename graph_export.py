import matplotlib.pyplot as plt
import networkx as nx

def build_recommendation_graph(user_id: str, user_phone_name: str, recommendations: dict) -> nx.DiGraph:
    """
    建立推薦圖譜（使用 NetworkX）：
    - user → 原手機（purchased）
    - 原手機 → 面向（feedback）
    - 面向 → 推薦手機（recommended）
    
    參數：
    - user_id：使用者 ID（如 "U001"）
    - user_phone_name：原始手機名稱（如 "Aphone 11"）
    - recommendations：來自 recommend.py 的推薦結果 dict（aspect → df）
    """
    G = nx.DiGraph()

    # 加入節點
    G.add_node(user_id, type="user")
    G.add_node(user_phone_name, type="device")

    # user → user_phone
    G.add_edge(user_id, user_phone_name, label="purchased")

    for aspect, recs in recommendations.items():
        G.add_node(aspect, type="aspect")
        G.add_edge(user_phone_name, aspect, label="feedback")

        for _, row in recs.iterrows():
            rec_name = row["name"]
            G.add_node(rec_name, type="device")
            G.add_edge(aspect, rec_name, label="recommended")

    return G

def draw_graph(G, focus_product=None, title="Recommendation Graph"):
    """
    畫出推薦圖譜 G，節點大小與顏色依據類型自動調整。
    - focus_product: 若提供，該手機節點會畫大一點。
    - title: 圖標題（預設為英文）
    """
    plt.figure(figsize=(12, 7))
    pos = nx.spring_layout(G, seed=42, k=0.7)

    color_map = []
    size_map = []

    for node, attr in G.nodes(data=True):
        ntype = attr.get("type", "default")
        if ntype == "user":
            color_map.append("skyblue")
            size_map.append(1500)
        elif ntype == "aspect":
            color_map.append("orange")
            size_map.append(1200)
        else:  # product/device
            color_map.append("lightgreen")
            size_map.append(1800 if node == focus_product else 1600)

    nx.draw(G, pos, with_labels=True,
            node_color=color_map, node_size=size_map,
            font_size=11, font_weight='bold', arrows=True)

    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_color="gray", font_size=10)

    plt.title(title, fontsize=14)
    plt.axis("off")
    plt.show()


# U001
# ↓ 
# Aphone 11
# ↓
# battery ───→ Bphone X
#          └──→ Cphone Pro
# camera ───→ Bphone X
#
