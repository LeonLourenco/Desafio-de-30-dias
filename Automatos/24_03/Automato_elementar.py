import numpy as np
import matplotlib.pyplot as plt

""" 
geração = vetor(N) (N é o número máximo de células)
nova_geração = vetor(N)
evolução =  matriz(MAX, N) (MAX é o número de gerações)
Inicializar geração (setar configurações iniciais)
para i = 1 até MAX:
    evolução[i,:] = geração
    # Percorre cada célula da geração atual
    para j = 1 até N
        Aplicar regra de transição na célula j, gerando nova_geração
    geração = nova_geração

Plotar resultados

"""
def converte_binario(numero=int):
    binario = bin(numero)
    binario = binario[2:]
    if len(binario) < 8:  
        zeros = [0] * (8 - len(binario))
        binario = zeros + list(binario)
    else:
        binario = list(binario)
    return binario


# Inicio do Script
MAX = 75
N = 150
geracao = np.zeros(N)
nova_geracao = np.zeros(N)
regra = int(input("Entre com o número da regra: "))
codigo = converte_binario(regra)

# Matriz em que cada linha armazena uma geração do autômato
matriz_evolucao = np.zeros((MAX, len(geracao)))

# Define geração inicial
geracao[len(geracao)//2] = 1

# Laço principal: atualiza as gerações
for i in range(MAX):
    matriz_evolucao[i,:] = geracao
    # Percorre células da geração atual
    for j in range(len(geracao)):
        if (geracao[j-1] == 0 and geracao[j] == 0 and geracao[((j+1) % len(geracao))] == 0 ): # o % no len final serve para pegar o ultimo elemento do vetor e usar como vizinho o elemento 0
            nova_geracao[j] = int(codigo[7])
        elif (geracao[j-1] == 0 and geracao[j] == 0 and geracao[((j+1) % len(geracao))] == 1 ):
            nova_geracao[j] = int(codigo[6])
        elif (geracao[j-1] == 0 and geracao[j] == 1 and geracao[((j+1) % len(geracao))] == 0 ):
            nova_geracao[j] = int(codigo[5])
        elif (geracao[j-1] == 0 and geracao[j] == 1 and geracao[((j+1) % len(geracao))] == 1 ):
            nova_geracao[j] = int(codigo[4])
        elif (geracao[j-1] == 1 and geracao[j] == 0 and geracao[((j+1) % len(geracao))] == 0 ):
            nova_geracao[j] = int(codigo[3])
        elif (geracao[j-1] == 1 and geracao[j] == 0 and geracao[((j+1) % len(geracao))] == 1 ):
            nova_geracao[j] = int(codigo[2])
        elif (geracao[j-1] == 1 and geracao[j] == 1 and geracao[((j+1) % len(geracao))] == 0 ):
            nova_geracao[j] = int(codigo[1])
        elif (geracao[j-1] == 1 and geracao[j] == 1 and geracao[((j+1) % len(geracao))] == 1 ):
            nova_geracao[j] = int(codigo[0])
    geracao = nova_geracao.copy() # se não usar copy ambos vetores tornam-se o mesmo
    
# Plota matriz resultante como imagem
plt.figure(1)
plt.axis('off')
plt.imshow(matriz_evolucao, cmap="gray")
plt.savefig('Automata.png', dpi=300)
plt.show()