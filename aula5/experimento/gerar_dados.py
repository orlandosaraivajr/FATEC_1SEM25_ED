from faker import Faker
import pickle

fake = Faker("pt_BR")
# N = 1_000_000
N = 1_000

lista = []
dicionario_nome = {}
dicionario_cpf = {}

for _ in range(N):
    nome = fake.name()
    telefone = fake.phone_number()
    cpf = fake.cpf()
    
    # adiciona na lista
    lista.append((nome, telefone, cpf))
    
    dicionario_nome[nome] = (nome, telefone, cpf)
    dicionario_cpf[cpf] = (nome, telefone, cpf)

print("Dados gerados com sucesso!")


# --- Salvando a lista em arquivo binário ---
with open("dados_lista.bin", "wb") as f:
    pickle.dump(lista, f)


with open("dados_dict_cpf.bin", "wb") as f:
    pickle.dump(dicionario_cpf, f)

with open("dados_dict_nome.bin", "wb") as f:
    pickle.dump(dicionario_nome, f, protocol=pickle.HIGHEST_PROTOCOL)

print("Lista gravada no arquivo 'dados.bin'.")



