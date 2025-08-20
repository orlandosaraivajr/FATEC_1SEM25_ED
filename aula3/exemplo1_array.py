import array

# Criando um array de inteiros (tipo 'i')
numeros = array.array('i', [10, 20, 30, 40, 50])

print("Array inicial:", numeros)

# Acessando elementos
print("Primeiro elemento:", numeros[0])
print("Último elemento:", numeros[-1])

# Inserindo um novo elemento no final
numeros.append(60)
print("Após append(60):", numeros)

# Inserindo em posição específica
numeros.insert(2, 15)  # insere 15 na posição 2
print("Após insert(2, 15):", numeros)

# Removendo um elemento
numeros.remove(30)  
print("Após remover 30:", numeros)

# Iterando sobre o array
print("Elementos no array:")
for n in numeros:
    print(n)
