import time
import random
import pickle


# --- Recuperando a lista do arquivo binário ---
with open("dados_lista.bin", "rb") as f:
    lista = pickle.load(f)

with open("dados_dict_nome.bin", "rb") as f:
    dicionario_nome = pickle.load(f)

with open("dados_dict_cpf.bin", "rb") as f:
    dicionario_cpf = pickle.load(f)

# Escolher um nome aleatório da lista para buscar
alvo_nome, alvo_phone, alvo_cpf = random.choice(lista)

print(f"\nBuscando pelo nome: {alvo_nome}")

# --- Busca na lista  ---
inicio = time.time()

# Seu código AQUI

fim = time.time()
print(f"Busca na lista → Telefone: {resultado_lista}")
print(f"Tempo gasto (lista): {fim - inicio:.6f} segundos")

# --- Busca no dicionário ---
inicio = time.time()

# Seu código AQUI

fim = time.time()
print(f"\nBusca no dicionário → Telefone: {resultado_dict}")
print(f"Tempo gasto (dicionário): {fim - inicio:.6f} segundos")

# --- Busca no segundo dicionário  ---
inicio = time.time()


fim = time.time()
print(f"\nBusca no dicionário → Telefone: {resultado_dict}")
print(f"Tempo gasto (dicionário): {fim - inicio:.6f} segundos")
