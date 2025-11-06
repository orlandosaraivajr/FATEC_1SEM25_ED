import heapq

# --- Mesmo grafo ---
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

def prim(graph, inicio):
    visitado = set([inicio])
    arestas = []
    heap = []

    # Adiciona arestas iniciais
    for vizinho, peso in graph[inicio].items():
        heapq.heappush(heap, (peso, inicio, vizinho))

    while heap:
        peso, u, v = heapq.heappop(heap)
        if v not in visitado:
            visitado.add(v)
            arestas.append((u, v, peso))
            for prox, w in graph[v].items():
                if prox not in visitado:
                    heapq.heappush(heap, (w, v, prox))

    return arestas

# --- Executa Prim ---
inicio = 'A'
mst = prim(graph, inicio)

print(f"\n--- Árvore Geradora Mínima (Prim) iniciando em {inicio} ---")
peso_total = 0
for u, v, peso in mst:
    print(f"{u} - {v} (peso={peso})")
    peso_total += peso
print(f"\nPeso total da MST: {peso_total}")
