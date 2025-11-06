import heapq

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

def dijkstra(graph, origem):
    dist = {v: float('inf') for v in graph}
    dist[origem] = 0
    anterior = {v: None for v in graph}

    heap = [(0, origem)]  # (distância, vértice)

    while heap:
        dist_atual, u = heapq.heappop(heap)

        if dist_atual > dist[u]:
            continue  # ignora entradas antigas no heap

        for vizinho, peso in graph[u].items():
            nova_dist = dist[u] + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                anterior[vizinho] = u
                heapq.heappush(heap, (nova_dist, vizinho))

    return dist, anterior


origem = 'A'
distancias, anteriores = dijkstra(graph, origem)

print(f"\n--- Dijkstra a partir de {origem} ---")
for v in sorted(graph.keys()):
    print(f"Distância até {v}: {distancias[v]}")

def caminho_para(destino):
    caminho = []
    atual = destino
    while atual:
        caminho.append(atual)
        atual = anteriores[atual]
    caminho.reverse()
    return caminho

print("\nExemplo: Caminho mínimo de A até H:")
print(" → ".join(caminho_para('H')))
