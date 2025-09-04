import array
import random
import time

# Criando um array de inteiros ('i')
numeros = array.array('i')

# Preenchendo com 1 milhão de números aleatórios entre 1 e 1.000.000
for _ in range(1_000_000):
    numeros.append(random.randint(1, 1_000_000))

print("Array com 1 milhão de números gerado!")

# Pede um número ao usuário
alvo = int(input("Digite o número que deseja procurar: "))

# Medindo tempo de busca
inicio = time.time()

# Verificando se o número existe no array
if alvo in numeros:
    print(f"O número {alvo} foi encontrado no array!")
else:
    print(f"O número {alvo} NÃO foi encontrado no array.")

fim = time.time()
print(f"Tempo de busca: {fim - inicio:.8f} segundos")
