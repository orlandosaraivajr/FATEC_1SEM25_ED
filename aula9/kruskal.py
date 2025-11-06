# ---- 1. Grafo ponderado estático (não direcionado) ----
graph = {
    'A': {'B': 3, 'S': 2},
    'B': {'A': 3},
    'S': {'A': 2, 'G': 5, 'C': 4},
    'C': {'S': 4, 'D': 1, 'E': 5, 'F': 1},
    'D': {'C': 1},
    'G': {'S': 5, 'F': 2, 'H': 3},
    'H': {'G': 3, 'E': 4},
    'E': {'H': 4, 'C': 5},
    'F': {'C': 1, 'G': 2}
}

# ---- 2. Converter o grafo em uma lista de arestas únicas ----
edges = []
added = set()

for u in graph:
    for v, peso in graph[u].items():
        if (v, u) not in added:  # evita duplicar arestas A-B e B-A
            edges.append((peso, u, v))
            added.add((u, v))

print("Arestas ponderadas fixas:")
for peso, u, v in edges:
    print(f"{u} - {v} (peso={peso})")

# ---- 3. Estruturas auxiliares (Union-Find) ----
parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    raiz1 = find(v1)
    raiz2 = find(v2)
    if raiz1 != raiz2:
        if rank[raiz1] < rank[raiz2]:
            parent[raiz1] = raiz2
        else:
            parent[raiz2] = raiz1
            if rank[raiz1] == rank[raiz2]:
                rank[raiz1] += 1

# ---- 4. Algoritmo de Kruskal ----
def kruskal(vertices, edges):
    for v in vertices:
        make_set(v)

    mst = []
    edges.sort()  # ordena por peso crescente

    for peso, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, peso))
    return mst

# ---- 5. Executar ----
vertices = list(graph.keys())
mst = kruskal(vertices, edges)

print("\nÁrvore Geradora Mínima (Kruskal):")
peso_total = 0
for u, v, peso in mst:
    print(f"{u} - {v} (peso={peso})")
    peso_total += peso

print(f"\nPeso total da MST: {peso_total}")
