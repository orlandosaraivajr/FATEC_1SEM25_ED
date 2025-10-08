# Lista de tuplas: (nome, idade, altura, peso)
pessoas = [
    ("Carlos", 28, 1.75, 72.0),
    ("Ana", 22, 1.68, 60.5),
    ("Bruno", 35, 1.80, 85.3),
    ("Daniela", 30, 1.65, 58.2),
    ("Eduardo", 28, 1.78, 77.4)
]

print("=== Lista original ===")
for p in pessoas:
    print(p)

# Ordenar por nome (crescente)
pessoas.sort(key=lambda x: x[0])
print("\n=== Ordenado por nome (crescente) ===")
for p in pessoas:
    print(p)

# Ordenar por nome (decrescente)
pessoas.sort(key=lambda x: x[0], reverse=True)
pessoas = sorted(pessoas, key=lambda x: x[0], reverse=True)
print("\n=== Ordenado por nome (decrescente) ===")
for p in pessoas:
    print(p)

# Ordenar por idade (crescente)
pessoas.sort(key=lambda x: x[1])
print("\n=== Ordenado por idade (crescente) ===")
for p in pessoas:
    print(p)

# Ordenar por idade (decrescente)
pessoas.sort(key=lambda x: x[1], reverse=True)
print("\n=== Ordenado por idade (decrescente) ===")
for p in pessoas:
    print(p)
