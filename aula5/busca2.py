import random
import bisect
import time

# Gerar lista com 1 milhão de números aleatórios
lista = [random.randint(1, 1_000_000) for _ in range(1_000_000)]

print("Lista com 1 milhão de elementos criada!")

# Ordenar a lista para usar busca binária
lista.sort()
print("Lista ordenada!")

# Pedir número ao usuário
alvo = int(input("Digite o número que deseja procurar: "))

# Medir tempo de busca
inicio = time.time()

# Usar bisect para encontrar posição onde o número estaria
pos = bisect.bisect_left(lista, alvo)

if pos < len(lista) and lista[pos] == alvo:
    print(f"O número {alvo} foi encontrado na posição {pos}.")
else:
    print(f"O número {alvo} NÃO foi encontrado.")

fim = time.time()
print(f"Tempo de busca: {fim - inicio:.6f} segundos")
